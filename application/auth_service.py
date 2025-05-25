from telethon import TelegramClient
from telethon.errors import (
    PhoneNumberInvalidError, PhoneCodeInvalidError,
    SessionPasswordNeededError, FloodWaitError, AuthKeyUnregisteredError, RPCError
)

from getpass import getpass
import logging
from domain.models import Config
from application.error_reporter import log_rpc_error, log_exception
from infrastructure.config_handler import save_config

async def authorize_user(config: Config, client: TelegramClient):
    try:
        await client.start()

        if await client.is_user_authorized():
            me = await client.get_me()
            logging.info("✅ Уже авторизован как %s (id: %d)", me.username or me.first_name, me.id)
            return

        logging.info("🔑 Требуется вход. Отправка кода на %s", config.phone_number)
        await client.send_code_request(config.phone_number)
        code = input("Введите код из Telegram: ")

        try:
            await client.sign_in(config.phone_number, code)
        except SessionPasswordNeededError:
            password = getpass("Включена двухфакторная аутентификация. Введите пароль: ")
            await client.sign_in(password=password)

        me = await client.get_me()
        logging.info("✅ Авторизация успешна: %s (id: %d)", me.username or me.first_name, me.id)

        session_str = client.session.save() # type: ignore
        if session_str:
            config.session_str = session_str
            print("✅ session_str создан:", session_str[:50], "...")
        else:
            print("❌ session_str не сгенерирован")
        save_config(config)
        logging.info("💾 Сессия сохранена")

    except PhoneNumberInvalidError:
        logging.error("❌ Неверный номер телефона.")
    except PhoneCodeInvalidError:
        logging.error("❌ Неверный код.")
    except SessionPasswordNeededError:
        logging.error("🔐 Необходим пароль 2FA.")
    except FloodWaitError as e:
        logging.error("⏳ Слишком много запросов. Подождите %d секунд.", e.seconds)
        log_rpc_error(e)
    except AuthKeyUnregisteredError:
        logging.error("🧨 Сессия повреждена. Сброс session_str.")
        config.session_str = None
        save_config(config)
        print("Пожалуйста, перезапустите процесс входа.")
        log_rpc_error(AuthKeyUnregisteredError())
    except RPCError as e:
        logging.error("⚠️ RPC ошибка: %s", e)
        log_rpc_error(e)
    except Exception as e:
        logging.exception("Ошибка авторизации: %s", e)
        log_exception("authorize_user", e)
    # finally:
    #     if client.is_connected():
    #         await client.disconnect()

async def logout_user(config: Config, client: TelegramClient):
    try:
        await client.start()

        if not await client.is_user_authorized():
            print("❌ Нет активной сессии.")
            return

        await client.log_out()
        print("🔒 Сессия Telegram завершена.")

        config.session_str = None
        save_config(config)
        logging.info("🗑 session_str удалён из config.json")

    except Exception as e:
        logging.exception("Ошибка при выходе: %s", e)
        log_exception("logout_user", e)
    finally:
        if client.is_connected():
            await client.disconnect()
