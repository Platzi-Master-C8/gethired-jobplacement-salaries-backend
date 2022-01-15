from sqlalchemy import delete, update


class BaseController(object):

    session = None
    model_class = None

    def __init__(self, session):
        self.session = session

    def create(self, data):
        new_object = self.model_class(**data)
        self.session.add(new_object)
        self.session.commit()

    def get(self, object_id):
        db_object = self.session.query(self.model_class).filter_by(id=object_id).first()
        return db_object

    def filter(self, filters=None):
        db_objects = self.session.query(self.model_class)
        if filters:
            db_objects = db_objects.filter_by(**filters)
        return db_objects or list()

    def update(self, object_id, data):
        update(self.model_class)

    def delete(self, object_id) -> None:
        delete(self.model_class).where(self.model_class.c.id == object_id)
