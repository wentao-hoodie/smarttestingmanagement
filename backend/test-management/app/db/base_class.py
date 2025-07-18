# In app/db/base_class.py

from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    """
    Base class for all SQLAlchemy models in the application.
    It automatically creates a __tablename__ for each model.
    """
    id: any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()