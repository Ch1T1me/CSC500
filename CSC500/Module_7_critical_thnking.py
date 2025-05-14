# Creating Python Programs 
'''
Key-Value Pairs: Room Number
'''
room_number = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411
}

'''
Key-Value Pairs: Instructors
'''
instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

'''
Key-Value Pairs: Meeting Time
'''
meeting_time = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# create function to handle the mapping 
def courseInfo():
    course_number = input(
        'Enter course number (CSC101, CSC102, CSC103, NET110, COM241):\n')
    
    # use try/except to only allow user to select within the choices
    try:
        room = room_number[course_number]
        instructor = instructors[course_number]
        time = meeting_time[course_number]
        
        # print statements
        print(f'Room Number: {room}')
        print(f'Course Instructor: {instructor}')
        print(f'Meeting Time: {time}')
    except KeyError:
        # user can choose from given courses
        print('Invalid option. Please select a valid option')
        print('Courses: CSC101, CSC102, CSC103, NET110, COM241') 

# call the function
courseInfo()