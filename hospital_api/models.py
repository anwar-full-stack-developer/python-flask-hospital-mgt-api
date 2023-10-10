from app_init import db, mar

# department or speciality
class DoctorDepartment(db.Model):
    __tablename__ = "doctor_departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    details = db.Column(db.String(255))


class DoctorDepartmentSchema(mar.SQLAlchemyAutoSchema):
    id = mar.auto_field()
    name = mar.auto_field()
    details = mar.auto_field()

    class Meta:
        model = DoctorDepartment
        fields = ('id', 'name', 'details')
        load_instance = True


doctorDepartmentSchema = DoctorDepartmentSchema()
doctorDepartmentSchemaList = DoctorDepartmentSchema(many=True)

class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    # department = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    details = db.Column(db.String(255))
    department_id = db.Column(db.Integer, db.ForeignKey('doctor_departments.id'))
    department = db.relationship("DoctorDepartment", backref="doctors")


class DoctorSchema(mar.SQLAlchemyAutoSchema):
    department = mar.auto_field()
    class Meta:
        model = Doctor
        load_instance = True
        fields = ('id', 'name', 'title', 'phone', 'details', 'department_id', 'department')
        include_fk = True


doctorSchema = DoctorSchema()
doctorListSchema = DoctorSchema(many=True)


class PatientBooking(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(255))
    booked_or_visited = db.Column(db.Boolean)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    address = db.Column(db.String(255))
    
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    doctor = db.relationship("Doctor", backref="patients")


class PatientBookingSchema(mar.SQLAlchemyAutoSchema):
    doctor = mar.auto_field()
    class Meta:
        model = PatientBooking
        load_instance = True
        fields = ('id', "serial_number", "booked_or_visited", "name", "phone", "address", "doctor_id", "doctor")
        include_fk = True


patientBookingSchema = PatientBookingSchema()
patientBookingListSchema=PatientBookingSchema(many=True)



class Prescription(db.Model):
    __tablename__ = "prescriptions"

    id = db.Column(db.Integer, primary_key=True)
    issue_date_time = db.Column(db.DateTime)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    address = db.Column(db.String(255))
    # optional to mention
    symptoms = db.Column(db.String(255))
    # Medecine advice, rules, next visit etc
    medecine_advice = db.Column(db.String(255))

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    doctor = db.relationship("Doctor", backref="prescriptions")


class PrescriptionSchema(mar.SQLAlchemyAutoSchema):
    doctor = mar.auto_field()
    class Meta:
        model = Prescription
        load_instance = True
        fields = ('id', "issue_date_time", "name", "phone", "address", "doctor_id", "doctor", "symptoms", "medecine_advice")
        include_fk = True


prescriptionSchema = PrescriptionSchema()
prescriptionListSchema = PrescriptionSchema(many=True)