from django.shortcuts import render, redirect
from CRUD.forms import CollegeForm
from formExample.models import College
from django.db.transaction import connections
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView


#from django.db

# Create your views here.
@login_required(login_url='/login')
def create(request):
    form = CollegeForm()

    if request.method == 'POST':
        form=CollegeForm(request.POST)

        if form.is_valid():
            #form.save() # another ORM method
            college = College()
            college.college_name = form.cleaned_data['college_email'].split('@')[0]
            college.college_email = form.cleaned_data['college_email']
            college.college_address = form.cleaned_data['college_address']
            college.college_city = form.cleaned_data['college_city']
            college.save()
            return redirect(index)
            #pass
    return render(request, 'CRUD/create.html', {'form':form})
    #pass

@login_required(login_url='/login')
def update(request):
    id = request.GET['id']
    print(id)
    data = College.objects.get(id=id)
    print(data)
    form = CollegeForm(instance=data)
# instance is populating the data
    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=data)

        if form.is_valid():
            #form.save()
            college = College()
            college.id = id
            college.college_name = form.cleaned_data['college_email'].split('@')[0]
            college.college_email = form.cleaned_data['college_email']
            college.college_address = form.cleaned_data['college_address']
            college.college_city = form.cleaned_data['college_city']
            college.save()

            return redirect(index)
            # pass
    return render(request, 'crud/update.html', {'form': form})


@login_required(login_url='/login')
def delete(request):
    id = request.GET['id']
    data = College.objects.get(id=id)
    data.delete()
    return redirect(index)


def view(request):
    id = request.GET['id']
    data = College.objects.get(id=id)
    #data = College.objects.raw("select * from college")
    #select * from college
    # ORM example

    return render(request,'crud/view.html', {'data':data})


# @login_required(login_url='/login')
def index(request):
    data = College.objects.all()
    #select ^ from college
    return render(request,'crud/index.html', {'data':data})



    #pass
