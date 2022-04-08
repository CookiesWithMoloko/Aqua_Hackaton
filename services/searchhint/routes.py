from app import app
from .models import doctor, hospital
Doctor = doctor.Doctor
Hospital = hospital.Hospital


@app.route('/searchhints/hospital/<str:hosp>')
def hint_hospital(hosp: str):
    r = Hospital.query.filter(Hospital.display.like(f'%{hosp}%')).all()
    return [i.display for i in r]
