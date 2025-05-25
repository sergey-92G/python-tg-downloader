import os
import asyncio
from telethon import TelegramClient
from telethon.errors import RPCError
from telethon.tl.types import Channel
from telethon.tl.custom.message import Message
from datetime import datetime
from pathlib import Path
from interfaces.telegram_client import create_telegram_client
from domain.models import Config
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

async def export_channel_media_and_chat(config: Config):
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
        print("🔍 Получение списка каналов...")

        channels = []
        async for dialog in client.iter_dialogs():
            if isinstance(dialog.entity, Channel) and dialog.entity.broadcast:
                channels.append(dialog)

        if not channels:
            print("❌ Каналы не найдены.")
            return

        print("\n📜 Список каналов:")
        for idx, ch in enumerate(channels, 1):
            print(f"{idx}. {ch.name}")

        selected = int(input("\nВведите номер канала: ")) - 1
        channel = channels[selected]
        print(f"\n✅ Выбран канал: {channel.name}")

        download_dir = DOWNLOAD_ROOT / "channels" / channel.name.replace(" ", "_")
        ensure_dir(download_dir)

        try:
            messages = await client.get_messages(channel, limit=None)
        except RPCError as e:
            log_rpc_error(e)
            print(f"⚠️ Ошибка загрузки сообщений: {e}")
            return

        print(f"📝 Загружено {len(messages)} сообщений")

        save_md = []
        for msg in reversed(messages):
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
        print("❌ Ошибка экспорта канала.")
        log_exception("export_channel_media_and_chat", e)

    finally:
        if client.is_connected():
            await client.disconnect()
