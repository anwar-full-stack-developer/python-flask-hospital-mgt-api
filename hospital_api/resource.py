#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import DoctorDepartment, doctorDepartmentSchema, doctorDepartmentSchemaList

class DoctorDepartmentList(Resource):
    def get(self):
        list = DoctorDepartment.query.all()
        return doctorDepartmentSchemaList.dump(list)
    
    def post(self): 
        data = request.get_json()
        dep = doctorDepartmentSchema.load(data)
        db.session.add(dep)
        db.session.commit()
        return doctorDepartmentSchema.dump(dep), 201


class DoctorDepartmentDetail(Resource):
    def get(self, id):
        dep = DoctorDepartment.query.get(id)

        if dep is not None:
            return doctorDepartmentSchema.dump(dep)
        else:
            abort(404, f"Doctor Department with id {id} not found")

    def put(self, id):
        existingDep = DoctorDepartment.query.filter(DoctorDepartment.id == id).one_or_none()

        if existingDep:
            updateDep = doctorDepartmentSchema.load(request.get_json())
            existingDep.name = updateDep.name
            existingDep.details = updateDep.details
            db.session.merge(updateDep)
            db.session.commit()
            return doctorDepartmentSchema.dump(existingDep), 201
        else:
            abort(404, f"Doctor with id {id} not found")

    def delete(self, id):
        dep = DoctorDepartment.query.get(id)
        if dep:
            db.session.delete(dep)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"Doctor -> Department with id {id} not found")

