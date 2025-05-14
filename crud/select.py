from model.model import record


class SelectOperation:
    async def __init__(self):
        pass

    async def all_record(self):
        records = record.find_all()
        return records
    
    async def record_by_id(self, record_id):
        record_db = record.find_one(
            record.id == record_id
        )

        if not record_db:
            raise Exception("record not found")
        
        return record_db
    
    async def record_by_name(self, recordname):
        record_db = record.find_one(
            record.id == recordname
        )

        if not record_db:
            raise Exception("record not found")
        
        return record_db