from sqlalchemy import delete, update


class BaseController:

    session = None
    model_class = None

    def __init__(self, session):
        self.session = session

    @property
    def base_query(self):
        return self.session.query(self.model_class).filter()

    def create(self, data):
        new_object = self.model_class(**data)
        self.session.add(new_object)
        self.session.commit()

    def get(self, object_id):
        db_object = self.session.get(self.model_class, object_id)
        return db_object

    def filter(self, **filters):
        db_objects = self.session.query(self.model_class)
        if filters:
            db_objects = db_objects.filter_by(**filters)
        return db_objects or list()

    def update(self, updated_object):
        self.session.update(updated_object)
        self.session.commit()

    def delete(self, deleted_object) -> None:
        self.session.query(deleted_object).delete()
        self.session.commit()
