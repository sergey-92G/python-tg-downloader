from telethon.tl.types import MessageMediaDocument, DocumentAttributeFilename
from telethon.errors import RPCError
from domain.models import Config
from interfaces.telegram_client import create_telegram_client
from application.error_reporter import log_exception, log_rpc_error
from pathlib import Path
import re

DOWNLOAD_ROOT = Path("download/channels")

def extract_channel_name(link: str) -> str | None:
    match = re.search(r"(?:https://t.me/|@)([\w\d_]+)", link)
    return match.group(1) if match else None

async def list_and_download_channel_files(config: Config):
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
        link = input("🔗 Введите ссылку на канал (https://t.me/... или @...): ").strip()
        channel_name = extract_channel_name(link)

        if not channel_name:
            print("❌ Неверный формат ссылки.")
            return

        entity = await client.get_entity(channel_name)

        print(f"📥 Поиск документов в канале: {channel_name}...")
        messages = await client.get_messages(entity, limit=500)
        documents = [msg for msg in messages if isinstance(msg.media, MessageMediaDocument)]

        if not documents:
            print("❌ Файлы не найдены.")
            return

        print(f"\n📋 Найдено {len(documents)} документов:")
        for i, msg in enumerate(reversed(documents), 1):
            name = next(
                (a.file_name for a in msg.document.attributes if isinstance(a, DocumentAttributeFilename)),
                "без_имени"
            )
            size_mb = round(msg.document.size / (1024 * 1024), 2)
            print(f"{i:>3}. {name} ({size_mb} MB)")

        choice = input("\nВведите номера файлов (через запятую) или 'all': ").strip().lower()
        if choice == "all":
            selected = range(1, len(documents) + 1)
        else:
            try:
                selected = [int(x.strip()) for x in choice.split(",") if x.strip().isdigit()]
            except:
                print("❌ Неверный ввод.")
                return

        target_dir = DOWNLOAD_ROOT / channel_name / "files"
        target_dir.mkdir(parents=True, exist_ok=True)

        for idx in selected:
            if not (1 <= idx <= len(documents)):
                print(f"⚠️ Пропуск: неверный номер {idx}")
                continue
            msg = documents[-idx]
            try:
                print(f"⬇️ Скачивание: {idx}")
                await client.download_media(msg, file=target_dir)
            except Exception as e:
                print(f"⚠️ Ошибка при скачивании ({idx}): {e}")
                log_exception("list_channel_files.download", e)

        print(f"✅ Скачано файлов: {len(selected)} → {target_dir}")

    except RPCError as e:
        log_rpc_error(e)
        print(f"❌ RPC ошибка: {e}")
    except Exception as e:
        log_exception("list_channel_files", e)
        print("❌ Ошибка при загрузке файлов.")
    finally:
        if client.is_connected():
            await client.disconnect()
