from telethon import TelegramClient
from telethon.sessions import StringSession

from domain.models import Config

def create_telegram_client(config: Config) -> TelegramClient:
    try:
        session = StringSession(config.session_str) if config.session_str else StringSession()
    except ValueError:
        print("⚠️ Предупреждение: session_str повреждён. Создаётся новая сессия.")
        session = StringSession()   
    return TelegramClient(
        session=session,
        api_id=config.api_id,
        api_hash=config.api_hash,
        device_model="Windows 11",
        system_version="10.0.22631 vxCUSTOM",
        app_version="4.16.30",
        lang_code="ru",
        system_lang_code="ru"
    )
