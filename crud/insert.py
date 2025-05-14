from model.model import record

class InsertOperation:
    async def __init__(self):
        pass

    async def record(self, name: str):
        new_record = record(
            name=name,
        )
        new_record.insert()
        return new_record
