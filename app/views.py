from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject, Student, Teacher


# Create your views here.

def subject(request):
    subjects = Subject.objects.all()
    response = ''
    for subject in subjects:
        print(subject.name)
        response = response + ' ' + subject.name

    print('estoy llamando al index')
    return HttpResponse(response)


def students(request):
    response = get_students
    return JsonResponse(response)

def get_students():
    students = Student.objects.all()
    response = {}
    for student in students:
        print(student.first_name, student.last_name)
        response[student.id] = {
            'Full name:': '{} {}' .format(student.first_name, student.last_name),
        }
        enrollments = student.enrollment_set.all()
        student_enrollment = []

        for enrollment in enrollments:
            avg_enrollment = 0
            notes = enrollment.note_set.all()
            for note in notes:
                avg_enrollment = avg_enrollment + note.value

            avg_enrollment = avg_enrollment / len(notes)
            student_enrollment.append(
                {
                    'name' : enrollment.subject.name,
                    'average' : avg_enrollment
                }
            )
        response[student.id]['enrollments'] = student_enrollment
    return response

def index(request):
    students = Student.objects.all()
    context = {
        'students' : students
    }
    return render(request, 'index.html', context)


def teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers' : teachers
    }
    return render(request, 'teachers.html', context)

def list_person(request, person):
    if person == 'students':
        students = Student.objects.all()

        context = {
            'title' : person,
            'students' : students
        }
        return render(request, 'students.html', context)

    elif person == 'teachers':
        teachers = Teacher.objects.all()

        context = {
            'title' : person,
            'teachers' : teachers
        }
    return render(request, 'teachers.html', context)
