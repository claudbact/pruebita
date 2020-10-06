#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, session, request, redirect
from datetime import datetime
from main.filters import if_session_active_go_home, if_session_not_active_go_login
view = Blueprint('access_bludprint', __name__)

@view.route('/login', methods=['GET'])
@if_session_active_go_home()
def login():
    locals={
        'message': '',
    }
    return render_template(
        'login_sgop.html',
        locals=locals
        ), 200
