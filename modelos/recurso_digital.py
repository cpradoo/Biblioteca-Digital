from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RecursoDigital(Base):
    __tablename__ = 'recursos_digitales'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    tipo = Column(String(50), nullable=False)
    premium = Column(Boolean, default=False)