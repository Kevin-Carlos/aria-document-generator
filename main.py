from flask import Flask, request
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_BREAK

# Create the Flask app.
app = Flask(__name__)

# Set the route to 'gen-docs' and only accept POST requests
@app.route('/create-documents', methods=['POST'])
def generateDocuments():
    # Create document variables to hold processing status.
    # By default they are set to not being requested.
    # If the document is requested it will be processed successfully or unsuccessfully.
    # The string will be updated either way.
    adjudicationForm = 'document was not requested.'
    announcingSheet = 'document was not requested.'
    certificates = 'document was not requested.'
    masterJudgeRepertoire = 'document was not requested.'
    masterJudgeSchedule = 'document was not requested.'
    resultsSheet = 'document was not requested.'
    roomSchedules = 'document was not requested.'
    sessionAssignments = 'document was not requested.'
    sessionLabels = 'document was not requested.'
    teacherMaster = 'document was not requested.'

    # Read the incoming JSON data and store it in 'data'
    reqData = request.get_json()

    # Determine if the JSON object has data, if it does...process it.
    try:
        if (reqData is not None):
                # -----------------
                # Adjudication Form
                # -----------------
            if (reqData['documents']['adjudicationForm'] == True):
                adjudicationForm = createAdjudicationForm(reqData)
                # ----------------
                # Announcing Sheet
                # ----------------
            if (reqData['documents']['announcingSheet'] == True):
                announcingSheet = createAnnouncingSheet(reqData)
                # ---------------------
                # Festival Certificates
                # ---------------------
            if (reqData['documents']['certificates'] == True):
                festivalCertificates = createCertificates(reqData)
                # -----------------------
                # Master Judge Repertoire
                # -----------------------
            if (reqData['documents']['masterJudgeRepertoire'] == True):
                masterJudgeRepertoire = createMasterJudgeRepertoire(reqData)
                # ---------------------
                # Master Judge Schedule
                # ---------------------
            if (reqData['documents']['masterJudgeSchedule'] == True):
                masterJudgeSchedule = createMasterJudgeSchedule(reqData)
                # -------------
                # Results Sheet
                # -------------
            if (reqData['documents']['resultsSheet'] == True):
                resultsSheet = createResultsSheet(reqData)
                # --------------
                # Room Schedules
                # --------------
            if (reqData['documents']['roomSchedules'] == True):
                roomSchedules = createRoomSchedules(reqData)
                # -------------------
                # Session Assignments
                # -------------------
            if (reqData['documents']['sessionAssignments'] == True):
                sessionAssignments = createSessionAssignments(reqData)
                # --------------
                # Session Labels
                # --------------
            if (reqData['documents']['sessionLabels'] == True):
                sessionLabels = createSessionLabels(reqData)
                # --------------
                # Teacher Master
                # --------------
            if (reqData['documents']['teacherMaster'] == True):
                teacherMaster = createTeacherMaster(reqData)
    except Exception as err:
        return f'Something Went Wrong \n Error Details Below \n, {err}'
    else:
        return f'''\n
                   01. Adjudication Form: {adjudicationForm} \n
                   02. Announcing Sheet: {announcingSheet} \n
                   03. Festival Certificates: {certificates} \n
                   04. Master Judge Repertoire: {masterJudgeRepertoire} \n
                   05. Master Judge Schedule: {masterJudgeSchedule} \n
                   06. Results Sheet: {resultsSheet} \n
                   07. Room Schedules: {roomSchedules} \n
                   08. Session Assignments: {sessionAssignments} \n
                   09. Session Labels: {sessionLabels} \n
                   10. Teacher Master: {teacherMaster} \n
        '''

def createAdjudicationForm(data):
    try:
        #
        #
        # This document still needs to be built...
        #
        #
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createAnnouncingSheet(data):
    try:
        # # Create Document
        document = Document()

        for i in data['announcingSheet']:
            if i == 'eventName':
                eventName = data['announcingSheet'].get(i, 'Entry not found.')
            if i == 'documentTitle':
                documentTitle = data['announcingSheet'].get(i, 'Entry not found.')
            if i == 'sessions':
                for j in data['announcingSheet']['sessions']:
                    if j == 'friday':
                        # Get all session data for Friday.
                        friday = data['announcingSheet']['sessions'].get(j, 'No session data for Friday.')
                    if j == 'saturday':
                        # Get all session data for Saturday.
                        saturday = data['announcingSheet']['sessions'].get(j, 'No session data for Saturday.')
                    if j == 'sunday':
                        # Get all session data for Sunday.
                        sunday = data['announcingSheet']['sessions'].get(j, 'No session data for Sunday.')
                        # Process session data for each session taking place on Sunday.
                        for k in range(len(sunday)):
                            # Gather Student-Independent Data
                            day = str(sunday[k]['day'])
                            time = str(sunday[k]['time'])
                            sessionNumber = str(sunday[k]['sessionNumber'])
                            nameOfRoom = str(sunday[k]['nameOfRoom'])
                            location = day + ', ' + time + ', ' + sessionNumber + ', ' + nameOfRoom
                            classType = sunday[k]['classType']
                            levels = sunday[k]['levels']
                            firstJudge = sunday[k]['firstJudge']
                            if sunday[k]['secondJudge'] != '':
                                secondJudge = sunday[k]['secondJudge']
                            else:
                                secondJudge = ''
                            if sunday[k]['thirdJudge'] != '':
                                thirdJudge = sunday[k]['thirdJudge']
                            else:
                                thirdJudge = ''
                            proctorName = sunday[k]['proctorName']
                            doorMonitorName = sunday[k]['doorMonitorName']
                            performanceOrder = sunday[k]['performanceOrder']

                            # Event Title
                            document.add_heading(eventName, level=0)
                            # Title Subheading
                            document.add_heading(documentTitle, level=1)
                            # Day, Time, Session Number, Room
                            document.add_heading(location, level=2)
                            # Add Performance Class Type
                            document.add_heading(classType, level=1)
                            # Add Students Levels
                            document.add_heading(f'Levels: {levels}', level=2)
                            # Add Judges
                            document.add_heading(f'Judge: {firstJudge}', level=3)
                            if sunday[k]['secondJudge'] != '':
                                document.add_heading(f'Judge: {secondJudge}', level=3)
                            if sunday[k]['thirdJudge'] != '':
                                document.add_heading(f'Judge: {thirdJudge}', level=3)
                            # Add Proctor
                            document.add_heading(f'Proctor: {proctorName}', level=3)
                            # Add Door Monitor
                            document.add_heading(f'Door Monitor: {doorMonitorName}', level=3)
                            # Performance Order
                            document.add_heading(f'{performanceOrder}:', level=1)

                            # Print Student Data
                            if sunday[k]['firstStudent'] != '':
                                name = sunday[k]['firstStudent'][0]['studentFullName']
                                level = sunday[k]['firstStudent'][0]['individualLevel']
                                p1 = document.add_paragraph()
                                p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
                                p1.add_run(f'1. {name}')
                                p1.alignment = None
                                p1.add_run(f'\t\t\t\t\t\tLeveL: {level}')

                            print()
                            print(f'END OF PAGE {k + 1}')
                            print()
                            # Page break after each session object is processed.
                            document.add_page_break()

        # # Write/Save Document
        document.save('./documents/announcing_sheet.docx')

        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createCertificates(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createMasterJudgeRepertoire(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createMasterJudgeSchedule(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createResultsSheet(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createRoomSchedules(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createSessionAssignments(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createSessionLabels(data):
    try:
        # !
        # !
        # This document still needs to be built...
        # !
        # !
        return 'document created successfully.'
    except Exception as err:
        return f'document creation failed... \n {err}'


def createTeacherMaster(data):
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
