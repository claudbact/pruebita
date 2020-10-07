#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint, render_template, session, request, redirect

#objeto que tiene la subaplicacion
view = Blueprint('usuario_bludprint', __name__)

@view.route('/inicio', methods=['GET'])
def registro():    
    locals = {
        'message': '',
        
    }
    return render_template(
        'layouts/aplication.html',
        locals=locals # acá seteamos una variable en nuestro template, en el tempalte tiene que coincider con el nombre locals, yy locals es undiccionario que en una de sus lavest tiene 
    ), 200


