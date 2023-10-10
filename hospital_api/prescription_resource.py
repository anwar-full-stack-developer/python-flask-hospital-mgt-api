#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import Prescription, prescriptionSchema, prescriptionListSchema

class PrescriptionListResource(Resource):
    def get(self):
        list = Prescription.query.all()
        return prescriptionListSchema.dump(list)
    
    def post(self): 
        # TODO:using patiemt_booking_id, collect Patient Booking information from PatientBookingTable
        
        data = request.get_json()
        prescription = prescriptionSchema.load(data)
        db.session.add(prescription)
        db.session.commit()
        return prescriptionSchema.dump(prescription), 201


class PrescriptionResource(Resource):
    def get(self, id):
        prescription = Prescription.query.get(id)
        if prescription is not None:
            return prescriptionSchema.dump(prescription)
        else:
            abort(404, f"Prescription with id {id} not found")

    def put(self, id):
        existingPrescription = Prescription.query.filter(Prescription.id == id).one_or_none()
        if existingPrescription:
            data = prescriptionSchema.load(request.get_json())
            existingPrescription.name = data.name
            existingPrescription.phone = data.phone
            existingPrescription.address = data.address
            existingPrescription.doctor = data.doctor
            existingPrescription.symptoms = data.symptoms
            existingPrescription.medecine_advice = data.medecine_advice
            db.session.merge(existingPrescription)
            db.session.commit()
            return prescriptionSchema.dump(existingPrescription), 201
        else:
            abort(404, f"Prescription with id {id} not found")

    def delete(self, id):
        prescription = Prescription.query.get(id)
        if prescription:
            db.session.delete(prescription)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"Prescription with id {id} not found")

