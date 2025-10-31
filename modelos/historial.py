from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HistorialDescargas(Base):
    __tablename__ = 'historial_descargas'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_recurso = Column(Integer, ForeignKey('recursos_digitales.id'), nullable=False)