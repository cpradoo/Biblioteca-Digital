from sqlalchemy import Column, Integer, String
from modelos.base import Base


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=True)
    nivel_suscripcion = Column(String(10), nullable=False, default='gratuita')