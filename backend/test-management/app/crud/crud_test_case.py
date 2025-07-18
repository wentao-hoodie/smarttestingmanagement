from app.crud.base import CRUDBase
from app.schemas.test_case import TestCaseCreate, TestCaseUpdate, TestCase


class CRUDTestCase(CRUDBase[TestCase, TestCaseCreate, TestCaseUpdate]):
    # In the future, you could add specific methods here, like:
    # def find_by_title(self, db, title):
    #     return db.query(TestCase).filter(TestCase.title == title).first()
    pass


test_case = CRUDTestCase(TestCase)