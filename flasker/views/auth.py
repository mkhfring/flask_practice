import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import User, db




bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'

    member = User.get_member(password)
    if member:
        error = 'User {} is already registered.'.format(username)


#    elif db.execute(
#        'SELECT id FROM user WHERE username = ?', (username,)
#    ).fetchone() is not None:
#        error = 'User {} is already registered.'.format(username)

    if error is None:
        User.add_member(username, password)

        return redirect(url_for('auth.login'))

    flash(error)

    return render_template('auth/register.html')
