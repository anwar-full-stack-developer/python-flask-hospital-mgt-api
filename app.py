import app_init

from task_api.resources import TaskList
from book_api.resource import AuthorList, AuthorDetail
from book_api.resource import BookList, BookDetail
from hospital_api.resource import DoctorDepartmentDetail, DoctorDepartmentList
from hospital_api.doctor_resource import DoctorResource, DoctorListResource
from hospital_api.patient_booking_resource import PatientBookingResource, PatientBookingListResource
from hospital_api.prescription_resource import PrescriptionResource, PrescriptionListResource


db=app_init.db
# do not use this
# app=app_init.connex_app
# use this ...
app=app_init.app
api = app_init.api


# Create the endpoints.

# Additional / Bonus API
# api.add_resource(TaskList, '/tasks')
api.add_resource(AuthorList, '/authors')
api.add_resource(AuthorDetail, '/author/<id>')
api.add_resource(BookList, '/books')
api.add_resource(BookDetail, '/book/<id>')

# Hospital api
api.add_resource(DoctorDepartmentList, '/hospital/departments')
api.add_resource(DoctorDepartmentDetail, '/hospital/department/<id>')

api.add_resource(DoctorListResource, '/hospital/doctors')
api.add_resource(DoctorResource, '/hospital/doctor/<id>')

api.add_resource(PatientBookingListResource, '/hospital/patients-booking')
api.add_resource(PatientBookingResource, '/hospital/patient-booking/<id>')

api.add_resource(PrescriptionListResource, '/hospital/prescriptions')
api.add_resource(PrescriptionResource, '/hospital/prescription/<id>')



if __name__ == '__main__':
    # Create the database tables.
    with app.app_context():
        db.create_all()
    # Start the Flask development web server.
    app.run(host="0.0.0.0", port=8000, debug=True)
