from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    nivel_suscripcion = Column(String(10), nullable=False, default='gratuita')
    correo = Column(String(255), nullable=True)
    habilitado = Column(Boolean, default=True)