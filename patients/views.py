from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import PatientForm
from .models import Patient

def index(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('patients:index')
        else:
            messages.error(request, 'There was an error adding the patient.')
    else:
        form = PatientForm()

    patients = Patient.objects.all()
    paginator = Paginator(patients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'form': form, 'page_obj': page_obj})

def detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'detail.html', {'patient': patient})

def edit(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient details updated successfully!')
            return redirect('patients:detail', patient_id=patient.id)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'edit.html', {'form': form})

def delete(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
        return redirect('patients:index')
    return render(request, 'delete_confirm.html', {'patient': patient})