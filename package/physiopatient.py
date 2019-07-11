from flask_restful import Resource, Api, request
from package.model import conn




class PhysioPatients(Resource):
    """It contain all the api carryign the activity with aand specific patient"""

    def get(self):
        """Api to retive all the patient from the database"""

        patients = conn.execute("SELECT * FROM physiopatient ORDER BY pat_name ASC").fetchall()
        return patients



    def post(self):
        """api to add the physiopatient in the database"""

        patientInput = request.get_json(force=True)
        pat_name=patientInput['pat_name']
        pat_date=patientInput['pat_date']
        pat_address = patientInput['pat_address']
        pat_ph_no = patientInput['pat_ph_no']
        pat_amount = patientInput['pat_amount']
        patientInput['phypat_id']=conn.execute('''INSERT INTO physiopatient(pat_name,pat_date,pat_address,pat_ph_no,pat_amount)
            VALUES(?,?,?,?,?)''', (pat_name,pat_date,pat_address,pat_ph_no,pat_amount)).lastrowid
        conn.commit()
        return patientInput

class PhysioPatient(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrive details of the patient by it id"""

        patient = conn.execute("SELECT * FROM physiopatient WHERE phypat_id=?",(id)).fetchall()
        return patient
        
        

    def delete(self,id):
        """api to delete the patient by its id"""

        conn.execute("DELETE FROM physiopatient WHERE phypat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by it id"""

        patientInput = request.get_json(force=True)
        pat_name=patientInput['pat_name']
        pat_date=patientInput['pat_date']
        pat_address = patientInput['pat_address']
        pat_ph_no = patientInput['pat_ph_no']
        pat_amount = patientInput['pat_amount']
        conn.execute('''UPDATE physiopatient SET pat_name=?,pat_date=?,pat_address=?,pat_ph_no=?,pat_amount=? WHERE phypat_id=?''',
                     (pat_name,pat_date,pat_address,pat_ph_no,pat_amount,id)).fetchall()
        conn.commit()
        return patientInput
    
