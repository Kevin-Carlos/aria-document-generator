import json
import student
from docx import Document
from docx.shared import Inches

student_json_data = '{"1": ["John", "Smith", "16", "A", "B", "C", "Mrs. Wiz", "04/30/2019 at 5:00 PM"]}'

student_dict = json.loads(student_json_data)

def main():
    participant = student.Student(id=list(student_dict.keys())[0], first_name=student_dict['1'][0],
                                  last_name=student_dict['1'][1], age=student_dict['1'][2],
                                  song_1=student_dict['1'][3], song_2=student_dict['1'][4],
                                  song_3=student_dict['1'][4], teacher_name=student_dict['1'][5],
                                  performance_time=student_dict['1'][6])

    # print('ID:', participant.get_id())
    # print('First Name:', participant.get_first_name())
    # print('Last Name:', participant.get_last_name())
    # print('Age:', participant.get_age())
    # print('Song 1:', participant.get_song_1())
    # print('Song 2:', participant.get_song_2())
    # print('Song 3:', participant.get_song_3())
    # print('Teacher Name:', participant.get_teacher_name())
    # print('Performance Time:', participant.get_performance_time())

    createSampleDocument(participant)

def createSampleDocument(student):
    document = Document()

    # Upper Festival Title
    document.add_heading('2019 Upper Festival', level=0)
    # Festival Subheading
    document.add_heading('Announcing Sheet', level=1)
    # Date/Time of Event
    document.add_heading('Saturday, 9:00 am, 1 (Recital Hall)')
    # Add Class Type
    document.add_heading('Master Class')
    # Add Level
    document.add_heading('Level 5')

    # Add Parapgraph 1 -- Judge
    p1 = document.add_paragraph()
    p1.add_run('Judge: \t\t\t\t')
    p1.add_run('Dr. Stephen Pierce, Univ. of Southern California')

    # Add Parapgraph 2 -- Proctor
    p2 = document.add_paragraph()
    p2.add_run('Proctor: \t\t\t')
    p2.add_run('Sonnet Johnson')

    # Add Parapgraph 3 -- Door Monitor
    p3 = document.add_paragraph()
    p3.add_run('Door Monitor: \t\t\t')
    p3.add_run('Catherine Lin')

    # Performance Order
    document.add_heading('Performance Order', level=1)
    # Student 1
    document.add_heading('1. ' + str(student.get_first_name()) + ' ' + str(student.get_last_name()) + '\t\t\t\t\t\t\t Level 5', level=2)
    p4a = document.add_paragraph()
    paragraph_format = p4a.paragraph_format
    paragraph_format.left_indent = Inches(0.5)
    p4a.add_run('Sea Piece \t\t\t\t\t\t\t MacDowell')
    p4b = document.add_paragraph()
    paragraph_format = p4b.paragraph_format
    paragraph_format.left_indent = Inches(0.5)
    p4b.add_run('Sonatina for Piano, 1st movement - Bagpipers \t\t Bartok')

    # Student 2
    document.add_heading('2. ' + str(student.get_first_name()) + ' ' + str(student.get_last_name()) + '\t\t\t\t\t\t\t Level 5', level=2)
    p5a = document.add_paragraph()
    paragraph_format = p5a.paragraph_format
    paragraph_format.left_indent = Inches(0.5)
    p5a.add_run('Minuet G minor (without Trio) \t\t\t\t Stozel')
    p5b = document.add_paragraph()
    paragraph_format = p5b.paragraph_format
    paragraph_format.left_indent = Inches(0.5)
    p5b.add_run('Faded Dreams \t\t\t\t\t\t\t Mier')

    # Student 3
    document.add_heading('3. ' + str(student.get_first_name()) + ' ' + str(student.get_last_name()) + '\t\t\t\t\t\t\t Level 5', level=2)
    p6a = document.add_paragraph()
    paragraph_format = p6a.paragraph_format
    paragraph_format.left_indent = Inches(0.5)
    p6a.add_run('Four Landlers, G Major \t\t\t\t\t Schubert')
    p6b = document.add_paragraph()
    paragraph_format = p6b.paragraph_format
    paragraph_format.left_indent = Inches(0.5)
    p6b.add_run('Winter Splendor \t\t\t\t\t\t Mier')

    document.save('sample.docx')

main()
