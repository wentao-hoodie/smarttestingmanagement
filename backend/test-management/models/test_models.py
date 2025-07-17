from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship, declarative_base
import enum
import datetime

Base = declarative_base()

class TestCase(Base):
    __tablename__ = 'test_cases'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    section_id = Column(Integer, nullable=True)
    type_id = Column(Integer, nullable=True)
    priority_id = Column(Integer, nullable=True)
    refs = Column(String(255), nullable=True)
    estimate = Column(String(50), nullable=True)
    milestone_id = Column(Integer, nullable=True)
    created_by = Column(Integer, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)

    steps = relationship('TestStep', back_populates='test_case', cascade="all, delete-orphan")

class TestStep(Base):
    __tablename__ = 'test_steps'

    id = Column(Integer, primary_key=True, index=True)
    step_number = Column(Integer, nullable=False)
    instruction = Column(Text, nullable=False)
    test_case_id = Column(Integer, ForeignKey('test_cases.id'), nullable=False)

    test_case = relationship('TestCase', back_populates='steps')

class TestRun(Base):
    __tablename__ = 'test_runs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    executed_at = Column(DateTime, default=datetime.datetime.utcnow)

    results = relationship('TestResult', back_populates='test_run', cascade="all, delete-orphan")

class TestStatus(enum.Enum):
    PASSED = 'Passed'
    FAILED = 'Failed'
    SKIPPED = 'Skipped'

class TestResult(Base):
    __tablename__ = 'test_results'

    id = Column(Integer, primary_key=True, index=True)
    test_run_id = Column(Integer, ForeignKey('test_runs.id'), nullable=False)
    test_case_id = Column(Integer, ForeignKey('test_cases.id'), nullable=False)
    status = Column(Enum(TestStatus), default=TestStatus.SKIPPED)
    executed_at = Column(DateTime, default=datetime.datetime.utcnow)

    test_run = relationship('TestRun', back_populates='results')
    test_case = relationship('TestCase')
