teachers = []

def subject(name,subject):
    teachers.append({'name': name, 'subject': subject})

def view():
    return teachers
