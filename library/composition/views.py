from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Composition, CompositionFile
from .forms import CompositionForm, UploadFileForm

def listComposition(request):
    compositions = Composition.objects.all()
    return render(request, 'composition/list.html', {'compositions': compositions})


def detailsComposition(request, id):
    composition = get_object_or_404(Composition, id=id)
    return render(request, 'composition/details.html', {'composition': composition})


def editComposition(request, pk=None):
    if pk:
        composition = get_object_or_404(Composition, pk=pk)
        action = 'update'
    else:
        composition = None
        action = 'add'

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

    return render(request, 'composition/form.html', {'form': form})

def deleteComposition(request, pk):
    composition = get_object_or_404(Composition, pk=pk)
    composition_name = composition.name  # сохранить имя для уведомления

    try:
        composition.delete()
        messages.success(request, f'Utwór "{composition_name}" został pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć utwór "{composition_name}": {str(e)}')

    return redirect('listComposition')

def uploadFiles(request, composition_id):
    composition = Composition.objects.get(id=composition_id)
    
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        file_type = request.POST.get('file_type')
        
        for f in files:
            CompositionFile.objects.create(
                composition=composition,
                file=f,
                file_type=file_type
            )
        
        messages.success(request, 'Plik pomyślnie wgrany.')
        return redirect('detailsComposition', id=composition_id)
    else:
        form = UploadFileForm()
    
    return render(request, 'composition/uploadFiles.html', {'form': form, 'composition': composition})

def deleteCompositionFile(request, id):
    file = get_object_or_404(CompositionFile, id=id)
    composition_id = file.composition.id
    
    try:
        file.file.delete()
        file.delete()
        messages.success(request, 'Plik pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Nie dało się usunąć pliku: {e}')
    
    return redirect('detailsComposition', id=composition_id)


def checkAsActual(request, id):
    composition = get_object_or_404(Composition, id=id)
    composition.isActual = not composition.isActual
    composition.save()
    messages.success(request, f'Utwór "{composition.name}" zaznaczony jako {"Aktualny" if composition.isActual else "Nieaktualny"}.')
    return redirect('listComposition')

