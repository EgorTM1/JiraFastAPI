from sqlalchemy import select
from src.db.db import session_maker


class SQLAlchemy:
    model = None


    def add_one(self, data) -> int:
        with session_maker() as session:
            data_info = data.model_dump()
            add_item = self.model(**data_info)

            session.add(add_item)
            session.flush()
            session.commit()

            return add_item.id


    def find_all(self):
        with session_maker() as session:
            query = select(self.model)

            res = session.execute(query)
            result = [row[0].to_read_model() for row in res.all()]

            return result
        
    def delete_one(self, id: int):
        with session_maker() as session:
            del_obj = session.get(self.model, id)

            session.delete(del_obj)
            session.commit()

            return {'message': 'good'}
        