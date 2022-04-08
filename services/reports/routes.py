from app import app
from flask import request
@app.post('/reports/add/')
def add_report():
    """read form"""
    request.form.get('')