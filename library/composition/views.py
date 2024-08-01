from django.shortcuts import render, redirect, get_object_or_404
from .models import Composition
from .forms import CompositionForm

def index(request):
    compositions = Composition.objects.all()
    return render(request, 'composition/compositionList.html', {'compositions': compositions})


def detailsComposition(request, id):
    composition = get_object_or_404(Composition, id=id)
    return render(request, 'composition/compositionDetails.html', {'composition': composition})


def editComposition(request):
    error = ''
    if request.method == 'POST':
        form = CompositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listComposition')
        else:
            error = 'Coś poszło nie tak'

    form = CompositionForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'composition/compositionForm.html', data)
