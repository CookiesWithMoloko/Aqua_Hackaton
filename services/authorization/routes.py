from app import app
from flask import render_template, session, abort, redirect, url_for


@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/first_check/')
def first_check():
    if not session.get('mode') == 'first_check':
        abort(403)
    return render_template('admin/first.html')

@app.route('/admin/second_check/')
def second_check():
    if not session.get('mode') == 'second_check':
        abort(403)
    return render_template('admin/second.html')

@app.route('/admin/statistics')
def statistics():
    if not session.get('mode') == 'statistics':
        abort(403)
    return render_template('admin/statistics.html')

@app.route('/admin/login/')
@app.route('/admin/login/<string:mode>')
def admin_login(mode: str = None):
    if mode not in ['first_check', 'second_check', 'statistics']:
        abort(404)
    session['mode'] = mode
    return redirect(url_for(f'.{mode}'))
