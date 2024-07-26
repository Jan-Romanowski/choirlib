from django.shortcuts import render, redirect
from .forms import CompositionForm

def index(request):
    return render(request, 'composition/compositionList.html')

def editComposition(request):
    error = ''
    if request.method == 'POST':
        form = CompositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/composition/list')
        else:
            error = 'Coś poszło nie tak'

    form = CompositionForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'composition/compositionForm.html', data)

def  detailsComposition(request):
    return render(request, 'composition/compositionDetails.html')


