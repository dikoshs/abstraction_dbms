from beanie import Document
from pydantic import Field

class record(Document):
    name: str = Field(max_length=20, min_length=1)

    class Config:
        json_schema_extra = {
            "record": {
                "name": "Adam",
            }
        }

    class Settings:
        name = "records"


__all__ = ["record"]