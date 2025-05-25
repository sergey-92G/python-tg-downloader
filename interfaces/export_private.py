import asyncio
from telethon import TelegramClient
from telethon.errors import RPCError
from telethon.tl.types import User
from telethon.tl.custom.message import Message
from datetime import datetime
from pathlib import Path
from domain.models import Config
from interfaces.telegram_client import create_telegram_client
from application.error_reporter import log_rpc_error, log_exception

DOWNLOAD_ROOT = Path("download")

def ensure_dir(path: Path):
    if not path.exists():
        print(f"📂 Создание каталога: {path}")
        path.mkdir(parents=True, exist_ok=True)  

def format_message_md(msg: Message) -> str:
    date_str = msg.date.strftime("### %Y-%m-%d\n## %H:%M:%S")
    username = f"@{msg.sender.username}" if hasattr(msg.sender, "username") else "@unknown"
    content = msg.message or ""
    media_tag = " - (media)" if msg.media else ""
    return f"{date_str}\n{username}\n{content}{media_tag}\n\n"

async def export_private_chat(config: Config):
    client = create_telegram_client(config)
    try:
        await client.start()
        if not await client.is_user_authorized():
            print("🔒 Сессия не авторизована. Выполните вход через меню '2. Connect'.")
            return
    except Exception as e:
        print("❌ Ошибка при запуске клиента.")
        log_exception("client_start", e)
        return

    try:
        print("🔍 Получение списка личных чатов...")

        users = []
        async for dialog in client.iter_dialogs():
            if isinstance(dialog.entity, User) and dialog.is_user and not dialog.entity.deleted:
                users.append(dialog)

        if not users:
            print("❌ Личные чаты не найдены.")
            return

        print("\n📜 Список личных чатов:")
        for idx, usr in enumerate(users, 1):
            name = f"{usr.name} ({usr.entity.username})" if usr.entity.username else usr.name
            print(f"{idx}. {name}")

        selected = int(input("\nВведите номер чата: ")) - 1
        user = users[selected]
        print(f"\n✅ Выбран: {user.name}")

        choice = input("💬 Указать диапазон сообщений? (all / <от>:<до>) ").strip()
        if choice == "all":
            from_id, to_id = None, None
        else:
            try:
                parts = choice.split(":")
                from_id, to_id = int(parts[0]), int(parts[1])
            except:
                print("❌ Неверный формат.")
                return

        download_dir = DOWNLOAD_ROOT / "private" / user.name.replace(" ", "_")
        ensure_dir(download_dir)

        try:
            messages = await client.get_messages(user, limit=None)
        except RPCError as e:
            log_rpc_error(e)
            print(f"⚠️ Ошибка загрузки сообщений: {e}")
            return

        print(f"📝 Загружено {len(messages)} сообщений")

        save_md = []
        for msg in reversed(messages):
            if from_id and (msg.id < from_id or msg.id > to_id):
                continue

            save_md.append(format_message_md(msg))

            if msg.media:
                try:
                    print(f"📥 Скачивание медиа: сообщение {msg.id}")
                    await client.download_media(msg, file=download_dir)
                except Exception as e:
                    print(f"⚠️ Ошибка при скачивании медиа (id {msg.id}): {e}")
                    log_exception("download_media", e)

        md_path = download_dir / "chat.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.writelines(save_md)

        print(f"✅ Переписка сохранена: {md_path}")

    except Exception as e:
        print("❌ Ошибка экспорта чата.")
        log_exception("export_private_chat", e)
    finally:
        if client.is_connected():
            await client.disconnect()


# async def export_private_chat(config: Config):
#     client = create_telegram_client(config)
#     try:
#         await client.start()
#         if not await client.is_user_authorized():
#             print("🔒 Сессия не авторизована. Выполните вход через меню '2. Connect'.")
#             return
#     except Exception as e:
#         print("❌ Ошибка при запуске клиента.")
#         log_exception("client_start", e)
#         return

#     try:
#         print("🔍 Получение списка личных чатов...")

#         users = []
#         async for dialog in client.iter_dialogs():
#             if isinstance(dialog.entity, User) and dialog.is_user:
#                 users.append(dialog)

#         if not users:
#             print("❌ Личные чаты не найдены.")
#             return

#         print("\n📜 Список личных чатов:")
#         for idx, usr in enumerate(users, 1):
#             name = f"{usr.name} ({usr.entity.username})" if usr.entity.username else usr.name
#             print(f"{idx}. {name}")

#         selected = int(input("\nВведите номер чата: ")) - 1
#         user = users[selected]
#         print(f"\n✅ Выбран: {user.name}")

#         choice = input("💬 Указать диапазон сообщений? (all / <от>:<до>) ").strip()
#         if choice == "all":
#             from_id, to_id = None, None
#         else:
#             try:
#                 parts = choice.split(":")
#                 from_id, to_id = int(parts[0]), int(parts[1])
#             except:
#                 print("❌ Неверный формат.")
#                 return

#         download_dir = DOWNLOAD_ROOT / "private" / user.name.replace(" ", "_")
#         ensure_dir(download_dir)

#         try:
#             messages = await client.get_messages(user, limit=None)
#         except RPCError as e:
#             log_rpc_error(e)
#             print(f"⚠️ Ошибка загрузки сообщений: {e}")
#             return

#         print(f"📝 Загружено {len(messages)} сообщений")

#         save_md = []
#         for msg in reversed(messages):
#             if from_id and (msg.id < from_id or msg.id > to_id):
#                 continue

#             save_md.append(format_message_md(msg))

#             if msg.media:
#                 try:
#                     print(f"📥 Скачивание медиа: сообщение {msg.id}")
#                     await client.download_media(msg, file=download_dir)
#                 except Exception as e:
#                     print(f"⚠️ Ошибка при скачивании медиа (id {msg.id}): {e}")
#                     log_exception("download_media", e)

#         md_path = download_dir / "chat.md"
#         with open(md_path, "w", encoding="utf-8") as f:
#             f.writelines(save_md)

#         print(f"✅ Переписка сохранена: {md_path}")

#     except Exception as e:
#         print("❌ Ошибка экспорта чата.")
#         log_exception("export_private_chat", e)
#     finally:
#         if client.is_connected():
#             await client.disconnect()
