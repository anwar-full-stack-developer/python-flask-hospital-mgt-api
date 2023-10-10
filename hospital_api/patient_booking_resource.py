#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import PatientBooking, patientBookingSchema, patientBookingListSchema

class PatientBookingListResource(Resource):
    def get(self):
        list = PatientBooking.query.all()
        return patientBookingListSchema.dump(list)
    
    def post(self): 
        data = request.get_json()
        patient = patientBookingSchema.load(data)
        db.session.add(patient)
        db.session.commit()
        return patientBookingSchema.dump(patient), 201


class PatientBookingResource(Resource):
    def get(self, id):
        patientBooking = PatientBooking.query.get(id)
        if patientBooking is not None:
            return patientBookingSchema.dump(patientBooking), 200
        else:
            abort(404, f"PatientBooking with id {id} not found")

    def put(self, id):
        existingPatientBooking = PatientBooking.query.filter(PatientBooking.id == id).one_or_none()
        if existingPatientBooking:
            data = patientBookingSchema.load(request.get_json())
            existingPatientBooking.serial_number = data.serial_number
            existingPatientBooking.booked_or_visited = data.booked_or_visited
            existingPatientBooking.name = data.name
            existingPatientBooking.name = data.name
            existingPatientBooking.phone = data.phone
            existingPatientBooking.address = data.address
            existingPatientBooking.doctor = data.doctor
            db.session.merge(existingPatientBooking)
            db.session.commit()
            return patientBookingSchema.dump(existingPatientBooking), 201
        else:
            abort(404, f"PatientBooking with id {id} not found")

    def delete(self, id):
        patientBooking = PatientBooking.query.get(id)
        if patientBooking:
            db.session.delete(patientBooking)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"PatientBooking with id {id} not found")

