import json
import student
from docx import Document

test_json_data = '{"1": ["John", "Smith", "16", "A", "B", "C", "Mrs. Wiz", "04/30/2019 at 5:00 PM"]}'

test_dict = json.loads(test_json_data)

def main():
    participant = student.Student(id=list(test_dict.keys())[0], first_name=test_dict['1'][0],
                                  last_name=test_dict['1'][1], age=test_dict['1'][2],
                                  song_1=test_dict['1'][3], song_2=test_dict['1'][4],
                                  song_3=test_dict['1'][4], teacher_name=test_dict['1'][5],
                                  performance_time=test_dict['1'][6])

    print('ID:', participant.get_id())
    print('First Name:', participant.get_first_name())
    print('Last Name:', participant.get_last_name())
    print('Age:', participant.get_age())
    print('Song 1:', participant.get_song_1())
    print('Song 2:', participant.get_song_2())
    print('Song 3:', participant.get_song_3())
    print('Teacher Name:', participant.get_teacher_name())
    print('Performance Time:', participant.get_performance_time())

main()
