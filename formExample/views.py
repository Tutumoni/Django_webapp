from django.shortcuts import render
from formExample.forms import FormExample


def staticExample(request):
    return render (request, 'static_example.html')



def form_example(request):

    formObj = FormExample()

    # print(request.GET)
    # print(request.method)

    if request.method == 'POST':
        formObj = FormExample(request.POST)

        if formObj.is_valid():
            #print(request.POST['username'])
            print(request.POST)
            pass

    #print(formObj)
    return render(request, 'form_example.html', {'form':formObj})

