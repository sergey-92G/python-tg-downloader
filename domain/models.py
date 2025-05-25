from pydantic import BaseModel, field_validator
import re

class Config(BaseModel):
    api_id: int
    api_hash: str
    phone_number: str
    session_str: str | None = None  # добавлено

    @field_validator("phone_number")
    def validate_phone(cls, v: str) -> str:
        if not re.match(r"^\+\d{10,15}$", v):
            raise ValueError("Phone number must be in international format (+XXXXXXXXXXX)")
        return v
