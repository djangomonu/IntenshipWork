from django.shortcuts import render, redirect
from .forms import reportForm
from .models import myForm
from django.contrib.auth.decorators import login_required

# from django.

# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'mainForms/dashboard.html')


@login_required
def displayForm(request):
    if request.method == 'POST':
        form = reportForm(request.POST)
        if form.is_valid():
            formData = myForm(
                Location=form.cleaned_data.get('Location'),
                Incident_desc=form.cleaned_data.get('Incident_desc'),
                DateOfAcci=form.cleaned_data.get('DateOfAcci'),
                TimeOfAcci=form.cleaned_data.get('TimeOfAcci'),
                incident_loc=form.cleaned_data.get('incident_loc'),
                initial_seve=form.cleaned_data.get('initial_seve'),
                suspected_cause=form.cleaned_data.get('suspected_cause'),
                immediate_act=form.cleaned_data.get('immediate_act'),
                incident_type=form.cleaned_data.get('incident_type'),
                reporeted_by=request.user,
            )
            formData.save()
            return redirect('incidentList')
    form = reportForm()
    context = {
        'form': form,
        'title': 'Incident Report Form',
    }
    return render(request, 'mainForms/form.html', context)


@login_required
def incidentList(request):

    list = myForm.objects.filter(reporeted_by=request.user)
    context = {
        'incident_list': list,
        'title': 'Incident List',
    }
    return render(request, 'mainForms/IncidentList.html', context)
