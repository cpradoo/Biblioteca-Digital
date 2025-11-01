from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from modelos.base import Base


class HistorialDescargas(Base):
    __tablename__ = 'historial_descargas'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_recurso = Column(Integer, ForeignKey('recursos_digitales.id'), nullable=False)
    fecha = Column(DateTime, default=datetime.now)
    usuario = relationship("Usuario", backref="descargas")
    recurso = relationship("RecursoDigital", backref="descargas")