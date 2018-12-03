from django.shortcuts import render

# Create your views here.
def helloDjango(request):
    return render(request, 'hello.html')

def helloPython(request):
    return render(request, 'hello_python.html')

