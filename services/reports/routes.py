from app import app, db
from flask import request, abort
from .models.report import Report
import re

EMAIL_PATTERN = re.compile('.+@.+\..+')
PASSPORT_PATTERN = re.compile('[0-9]{4} [0-9]{6}')
def isNone(a):
    return a is None or a == ''
@app.post('/reports/add/')
def add_report():
    organization = request.form.get('organization', None, str)
    target = request.form.get('target', None, str)
    author = request.form.get('author', None, str)
    email = request.form.get('email', None, str)
    content = request.form.get('content', None, str)
    passport = request.form.get('passport', None, str)
    if len(filter(isNone, [organization, author, email, content, passport])) != 0:
        abort(400)
    if not EMAIL_PATTERN.match(email):
        abort(400)
    if not PASSPORT_PATTERN.match(passport):
        abort(404)
    db.session.add(Report(
        organization=organization.lower(),
        target=target,
        target_organization=isNone(target),
        email=email,
        content=content
    ))



