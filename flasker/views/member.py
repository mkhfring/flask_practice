
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required



bp = Blueprint('member', __name__, url_prefix='/')


@bp.route('user', methods=('GET', 'POST'))
def get_member():
    import pudb; pudb.set_trace()  # XXX BREAKPOINT
    pass
