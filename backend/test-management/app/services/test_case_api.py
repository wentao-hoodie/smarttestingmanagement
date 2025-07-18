# In app/services/test_case_api.py

from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Adjust imports to match your project structure
from app import crud, schemas
from app.services import deps

router = APIRouter()

@router.post("/", response_model=schemas.TestCase)
def create_test_case(*, db: Session = Depends(deps.get_db), test_case_in: schemas.TestCaseCreate) -> Any:
    """Create a new test case."""
    test_case = crud.test_case.create(db=db, obj_in=test_case_in)
    return test_case

@router.get("/", response_model=List[schemas.TestCase])
def read_test_cases(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100) -> Any:
    """Retrieve all test cases."""
    return crud.test_case.get_multi(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.TestCase)
def read_test_case(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """Get a specific test case by ID."""
    test_case = crud.test_case.get(db=db, id=id)
    if not test_case:
        raise HTTPException(status_code=404, detail="Test case not found")
    return test_case

@router.put("/{id}", response_model=schemas.TestCase)
def update_test_case(*, db: Session = Depends(deps.get_db), id: int, test_case_in: schemas.TestCaseUpdate) -> Any:
    """Update a test case."""
    test_case = crud.test_case.get(db=db, id=id)
    if not test_case:
        raise HTTPException(status_code=404, detail="Test case not found")
    return crud.test_case.update(db=db, db_obj=test_case, obj_in=test_case_in)

@router.delete("/{id}", response_model=schemas.TestCase)
def delete_test_case(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """Delete a test case."""
    test_case = crud.test_case.get(db=db, id=id)
    if not test_case:
        raise HTTPException(status_code=404, detail="Test case not found")
    return crud.test_case.remove(db=db, id=id)