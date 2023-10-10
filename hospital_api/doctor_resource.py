#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import Doctor, doctorSchema, doctorListSchema

class DoctorListResource(Resource):
    def get(self):
        list = Doctor.query.all()
        return doctorListSchema.dump(list)
    
    def post(self): 
        data = request.get_json()
        doctor = doctorSchema.load(data)
        db.session.add(doctor)
        db.session.commit()
        return doctorSchema.dump(doctor), 201


class DoctorResource(Resource):
    def get(self, id):
        dep = Doctor.query.get(id)

        if dep is not None:
            return doctorSchema.dump(dep)
        else:
            abort(404, f"Doctor with id {id} not found")

    def put(self, id):
        existingDoctor = Doctor.query.filter(Doctor.id == id).one_or_none()
        if existingDoctor:
            data = doctorSchema.load(request.get_json())
            existingDoctor.name = data.name
            existingDoctor.title = data.title
            existingDoctor.phone = data.phone
            existingDoctor.details = data.details
            existingDoctor.department = data.department
            db.session.merge(existingDoctor)
            db.session.commit()
            return doctorSchema.dump(existingDoctor), 201
        else:
            abort(404, f"Doctor with id {id} not found")

    def delete(self, id):
        doctor = Doctor.query.get(id)
        if doctor:
            db.session.delete(doctor)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"Doctor with id {id} not found")

