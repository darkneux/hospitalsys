from django.shortcuts import render
from .models import *
from django.contrib.auth import login,authenticate,logout

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
def core(request):
    return render(request,'index.html')

from django.contrib.auth import authenticate, login

def loginPage(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/addpatient/')
        else:
            # webpage/login/global rather then webpage/global
            error_message = 'Invalid login credentials'
            return render(request, 'login_page.html', {'error_message': error_message})
    else:

        return render(request,'login_page.html')




from django.shortcuts import render
from .models import Patient_Info

def patientList(request):
    patients = Patient_Info.objects.all() # get all patients from the database
    context = {'patients': patients} # pass patients to the context dictionary
    return render(request, 'patient_list.html', context) # render the patient list template with the context data



from django.shortcuts import render, get_object_or_404

def patientInfo(request, patient_id):
    if not request.user.is_authenticated:

        return redirect('/login/')
    patient = get_object_or_404(Patient_Info, patient_ID=patient_id)

    context = {
        'patient': patient,
    }
    return render(request, 'patient_info.html', context)


from django.shortcuts import render, redirect


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Patient_Info

def addPatient(request):

    if not request.user.is_authenticated:

        return redirect('/login/')


    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        nationality = request.POST['nationality']
        insurance_policy_id = request.POST.get('insurance_policy_id')
        nation_card_id = request.POST.get('nation_card_id')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')


        # Create new Patient_Info object
        patient = Patient_Info(
            first_Name=first_name,
            last_Name=last_name,
            sex=sex,
            age=age,
            nationality=nationality,
            insurance_policy_ID=insurance_policy_id,
            Nation_Card_ID=nation_card_id,
            email=email,
            address=address,
            phone=phone,
        )
        patient.save()
        return HttpResponseRedirect('/addpatient/')
    return render(request, 'patient_add.html')
