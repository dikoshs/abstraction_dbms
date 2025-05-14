from beanie import Document

class User(Document):
    name: str

    class Config:
        json_schema_extra = {
            "user": {
                "name": "Adam",
            }
        }

    class Settings:
        name = "users"


__all__ = ["User"]