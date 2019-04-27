from flask import Flask, request
from docx import Document
from docx.shared import Inches

# Create the Flask app.
app = Flask(__name__)

# Set the route to 'gen-docs' and only accept POST requests
@app.route('/gen-docs', methods=['POST'])
def gen_docs():
    # Create document variables to hold processing status.
    # By default they are set to not being requested.
    # If the document is requested it will be processed successfully or unsuccessfully.
    # The string will be updated either way.
    adjudication_form = 'document was not requested.'
    announcing_sheet = 'document was not requested.'
    festival_certificates = 'document was not requested.'
    master_judge_repertoire = 'document was not requested.'
    master_judge_schedule = 'document was not requested.'
    results_sheet = 'document was not requested.'
    room_schedules = 'document was not requested.'
    session_assignments = 'document was not requested.'
    session_labels = 'document was not requested.'
    teacher_master = 'document was not requested.'

    # Read the incoming JSON data and store it in 'data'
    req_data = request.get_json()

    # Determine if the JSON object has data, if it does...process it.
    try:
        if (req_data is not None):
                # -----------------
                # Adjudication Form
                # -----------------
            if (req_data['documents']['2019_upper_festival_adjudication_form'] == True):
                adjudication_form = create_adjudication_form(req_data)
                # ----------------
                # Announcing Sheet
                # ----------------
            if (req_data['documents']['2019_upper_festival_announcing_sheet'] == True):
                announcing_sheet = create_announcing_sheet(req_data)
                # ---------------------
                # Festival Certificates
                # ---------------------
            if (req_data['documents']['2019_upper_festival_certificates'] == True):
                festival_certificates = create_festival_certificates(req_data)
                # -----------------------
                # Master Judge Repertoire
                # -----------------------
            if (req_data['documents']['2019_upper_festival_master_judge_repertoire'] == True):
                master_judge_repertoire = create_master_judge_repertoire(req_data)
                # ---------------------
                # Master Judge Schedule
                # ---------------------
            if (req_data['documents']['2019_upper_festival_master_judge_schedule'] == True):
                master_judge_schedule = create_master_judge_schedule(req_data)
                # -------------
                # Results Sheet
                # -------------
            if (req_data['documents']['2019_upper_festival_results_sheet'] == True):
                results_sheet = create_results_sheet(req_data)
                # --------------
                # Room Schedules
                # --------------
            if (req_data['documents']['2019_upper_festival_room_schedules'] == True):
                room_schedules = create_room_schedules(req_data)
                # -------------------
                # Session Assignments
                # -------------------
            if (req_data['documents']['2019_upper_festival_session_assignments'] == True):
                session_assignments = create_session_assignments(req_data)
                # --------------
                # Session Labels
                # --------------
            if (req_data['documents']['2019_upper_festival_session_labels'] == True):
                session_labels = create_session_labels(req_data)
                # --------------
                # Teacher Master
                # --------------
            if (req_data['documents']['2019_upper_festival_teacher_master'] == True):
                teacher_master = create_teacher_master(req_data)
    except Exception as err:
        return f'Something Went Wrong \n Error Details Below \n, {err}'
    else:
        return f'''\n
                   01. Adjudication Form: {adjudication_form} \n
                   02. Announcing Sheet: {announcing_sheet} \n
                   03. Festival Certificates: {festival_certificates} \n
                   04. Master Judge Repertoire: {master_judge_repertoire} \n
                   05. Master Judge Schedule: {master_judge_schedule} \n
                   06. Results Sheet: {results_sheet} \n
                   07. Room Schedules: {room_schedules} \n
                   08. Session Assignments: {session_assignments} \n
                   09. Session Labels: {session_labels} \n
                   10. Teacher Master: {teacher_master} \n
        '''

def create_adjudication_form(data):
    try:
        #
        #
        # This document still needs to be built...
        #
        #
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_announcing_sheet(data):
    try:
        # Create Document
        document = Document()
        # Upper Festival Title
        document.add_heading(data['event']['event_name'], level=0)
        # # Festival Subheading
        # document.add_heading('Announcing Sheet', level=1)
        # # Day, Time, Session Number, Room
        # document.add_heading(str(data['event']['sessions']['friday']['day'])), level=1)
        # # Add Class Type
        # document.add_heading(str(data['event']['sessions']['friday']['class_type'])), level=1)
        # # Add Level
        # document.add_heading(str(data['event']['sessions']['friday']['levels'])), level=1)
        # Write/Save Document
        document.save('./documents/announcing_sheet.docx')

        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_festival_certificates(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_master_judge_repertoire(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_master_judge_schedule(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_results_sheet(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_room_schedules(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_session_assignments(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_session_labels(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def create_teacher_master(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


if __name__ == '__main_':
    app.run(debug=True, port=4321) #run app in debug mode on port 4321
