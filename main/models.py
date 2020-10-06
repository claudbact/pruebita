# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 2. creacion de modelos 
from sqlalchemy import Column, Integer, String
from main.database import Base

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    cod_usuario = Column(String)
    password = Column(String)
    correo_electronico = Column(String)
    rol = Column(Integer)
