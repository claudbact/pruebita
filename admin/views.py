#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json,datetime
from flask import Blueprint, render_template, session, request, redirect
from main.models import Country,Objeto
from main.database import engine
from sqlalchemy import select

#objeto que tiene la subaplicacion
view = Blueprint('admin_bludprint', __name__)

@view.route('/country/list')
def country_list():
    resp = None
    status = 200
    try:
        conn = engine.connect()
        stmt = select([Country])
        rs = conn.execute(stmt)
        resp = [dict(r) for r in conn.execute(stmt)]
    except Exception as e:
        resp = [
            'Se ha producido un error en listar los paises',
            str(e)
        ]
        status = 500
    return json.dumps(resp), status



@view.route('/objeto/list')
def objeto_list():
    resp = None
    status = 200
    try:
        conn = engine.connect()
        stmt = select([Objeto])
        rs = conn.execute(stmt)
        lista = []
        for r in conn.execute(stmt):
            print(r.fecha_hallado)
            row = {
            'id': r.id,
            'cod_objeto':r.cod_objeto,
            'nom_objeto':r.nom_objeto,
            'categoria':r.categoria,
            'estado':r.estado,
            'marca':r.marca,
            'fecha_hallado':str(r.fecha_hallado),
            'fecha_dev':str(r.fecha_dev),
            'lugar':r.lugar,
            'nro_anaquel':r.nro_anaquel,
            'caract_esp':r.caract_esp,
            'cod_usu_entrega':r.cod_usu_entrega
            }
            lista.append(row) 
        #resp = [dict(r) for r in conn.execute(stmt)]
        resp=lista
    except Exception as e:
        resp = [
            'Se ha producido un error en listar los paises',
            str(e)
        ]
        status = 500

    return json.dumps(resp),status
