# Shared properties
from pydantic import BaseModel


class TestCaseBase(BaseModel):
    title: str
    priority: str = 'Medium' # You can set a default

# Properties to receive on item creation
class TestCaseCreate(TestCaseBase):
    pass # No new fields needed for creation right now

# Properties to receive on item update
class TestCaseUpdate(TestCaseBase):
    pass # Can be identical to create, or have optional fields

# Properties to return to client
class TestCase(TestCaseBase):
    id: int

    class Config:
        orm_mode = True # This magic setting tells Pydantic to read the data even if it is not a dict, but an ORM model