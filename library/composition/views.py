from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Composition
from .forms import CompositionForm

def index(request):
    compositions = Composition.objects.all()
    return render(request, 'composition/compositionList.html', {'compositions': compositions})


def detailsComposition(request, id):
    composition = get_object_or_404(Composition, id=id)
    return render(request, 'composition/compositionDetails.html', {'composition': composition})


def editComposition(request, pk=None):
    if pk:
        composition = get_object_or_404(Composition, pk=pk)
        action = 'update'  # Действие — обновление
    else:
        composition = None
        action = 'add'  # Действие — добавление

    if request.method == 'POST':
        form = CompositionForm(request.POST, instance=composition)
        if form.is_valid():
            new_composition = form.save()
            if action == 'add':
                messages.success(request, f'Utwór {new_composition.name} został pomyślnie dodany do biblioteki.')
                messages.warning(request, f'Do ostatnio dodanego utwóru {new_composition.name} został przypisany numer: {new_composition.number}.')
            else:
                messages.success(request, f'Utwór {new_composition.name} został pomyślnie zaktualizowany.')
            
            return redirect('listComposition')
        else:
            messages.error(request, 'Coś poszło nie tak')
    else:
        form = CompositionForm(instance=composition)

    return render(request, 'composition/compositionForm.html', {'form': form})



def deleteComposition(request, pk):
    composition = get_object_or_404(Composition, pk=pk)
    composition_name = composition.name  # сохранить имя для уведомления

    try:
        composition.delete()
        messages.success(request, f'Utwór "{composition_name}" został pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć utwór "{composition_name}": {str(e)}')

    return redirect('listComposition')