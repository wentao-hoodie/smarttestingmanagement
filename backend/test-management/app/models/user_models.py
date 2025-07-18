from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text, Boolean
from sqlalchemy.orm import relationship, declarative_base
import datetime

from base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship('Role', back_populates='users')
    test_cases = relationship('TestCase', back_populates='owner')

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship('User', back_populates='role')