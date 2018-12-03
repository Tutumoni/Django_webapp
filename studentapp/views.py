from django.shortcuts import render

def helloStudent(request):

    d1 = {
        'name':'xyz',
        'email': 'xyz@gmail.com',
        'l1': [1,2,3,4,5],
        'd2':{'city': 'Bangalore', 'address': 'btm'}
    }
    return render(request, 'student.html', d1)
