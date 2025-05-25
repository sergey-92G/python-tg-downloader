import logging
from pathlib import Path

from domain.models import Config
from application.auth_service import authorize_user, logout_user
from interfaces.telegram_client import create_telegram_client
from interfaces.export_channels import export_channel_media_and_chat
from interfaces.export_private import export_private_chat
from interfaces.export_groups import export_group_chat
from interfaces.list_channel_files import list_and_download_channel_files
from infrastructure.config_handler import save_config, load_config

CONFIG_PATH = Path("config.json")


def input_api_data() -> Config:
    api_id = int(input("Enter API ID: "))
    api_hash = input("Enter API Hash: ")
    phone = input("Enter phone number (+...): ")
    config = Config(api_id=api_id, api_hash=api_hash, phone_number=phone)
    save_config(config)
    return config

async def main_menu():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    config = load_config()

    while True:
        print("\nMenu:")
        print("1. Enter API Data")
        print("2. Connect")
        print("3. Export from Channel")
        print("4. Export from Private Chat")
        print("5. Export from Group Chat")
        print("6. Logout (Telegram session)")
        print("7. List & Download Files from Channel")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                config = input_api_data()
            except Exception as e:
                print(f"Invalid input: {e}")
        elif choice == "2":
            if config is not None:
                client = create_telegram_client(config)
                await authorize_user(config, client)
            else:
                print("No config found. Please enter API data first.")
        elif choice == "3":
            if config is not None:
                await export_channel_media_and_chat(config)
            else:
                print("Config not loaded.")
        elif choice == "4":
            if config is not None:
                await export_private_chat(config)
            else:
                print("Config not loaded.")
        elif choice == "5":
            if config is not None:
                await export_group_chat(config)
            else:
                print("Config not loaded.")
        elif choice == "6":
            if config is not None:
                client = create_telegram_client(config)
                await logout_user(config, client)
            else:
                print("Config not loaded.")
        elif choice == "7":
            if config is not None:
                await list_and_download_channel_files(config)
            else:
                print("Config not loaded.")
        elif choice == "8":
            print("👋 Выход.")
            break
        else:
            print("Invalid option.")
