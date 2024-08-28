from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Composition, CompositionFile
from .forms import CompositionForm, UploadFileForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required

@permission_required('composition.can_edit_compositions', raise_exception=True)
def listComposition(request):
    query = request.GET.get('q')
    compositions = Composition.objects.all()
    
    if query:
        compositions = compositions.filter(
            Q(name__icontains=query) | Q(author__icontains=query)
        )

    paginator = Paginator(compositions, 3)  # Показывать 10 произведений на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'composition/list.html', {'page_obj': page_obj, 'compositions': page_obj.object_list})


def detailsComposition(request, id):
    composition = get_object_or_404(Composition, id=id)
    return render(request, 'composition/details.html', {'composition': composition})


def editComposition(request, id=None):
    if id:
        composition = get_object_or_404(Composition, id=id)
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

    return render(request, 'composition/form.html', {'form': form, 'composition': composition})

def deleteComposition(request, id):
    composition = get_object_or_404(Composition, id=id)
    composition_name = composition.name  # сохранить имя для уведомления

    try:
        for file in composition.files.all():
            file.file.delete()
            file.delete()
              
        composition.delete()

        messages.success(request, f'Utwór "{composition_name}" został pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć utwór "{composition_name}": {str(e)}')

    return redirect('listComposition')

def uploadFiles(request, id):
    composition = Composition.objects.get(id=id)
    
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        
        for f in files:
            file_extension = f.name.split('.')[-1].lower()

            CompositionFile.objects.create(
                composition=composition,
                file=f,
                file_type=file_extension
            )
        
        messages.success(request, 'Plik pomyślnie wgrany.')
        return redirect('detailsComposition', id=id)
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

