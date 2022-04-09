from app import app
from flask import jsonify
from .models import doctor, hospital
Doctor = doctor.Doctor
Hospital = hospital.Hospital

@app.route('/searchhints/hospital/')
@app.route('/searchhints/hospital/<string:hosp>')
def hint_hospital(hosp: str = ''):
    r = Hospital.query.filter(Hospital.display.like(f'%{hosp}%')).all()
    return jsonify([i.display for i in r])
