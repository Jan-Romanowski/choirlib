from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Composition, CompositionFile
from .forms import CompositionForm, UploadFileForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_filters(request):
    if request.method == 'POST':
        only_actual = request.POST.get('onlyActual') == 'on'
        only_with_files = request.POST.get('onlyWithFiles') == 'on'
        only_without_files = request.POST.get('onlyWithoutFiles') == 'on'
        only_without_folder = request.POST.get('onlyWithoutFolder') == 'on'

        # Сохраните фильтры в сессии
        request.session['filters'] = {
            'onlyActual': only_actual,
            'onlyWithFiles': only_with_files,
            'onlyWithoutFiles': only_without_files,
            'onlyWithoutFolder': only_without_folder,
        }

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)

def search_compositions(request):
    query = request.GET.get('query', '')
    compositions = Composition.objects.filter(name__icontains=query)

    return render(request, 'compositions_table.html', {'compositions': compositions})

def listComposition(request):
    query = request.GET.get('q')
    compositions = Composition.objects.all()
    
    if query:
        compositions = compositions.filter(
            Q(name__icontains=query) | Q(author__icontains=query)
        )

    paginator = Paginator(compositions, 10)  # Показывать 10 произведений на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'composition/list.html', {'page_obj': page_obj, 'compositions': page_obj.object_list})


def detailsComposition(request, id):
    composition = get_object_or_404(Composition, id=id)
    return render(request, 'composition/details.html', {'composition': composition})

@permission_required('composition.add_composition', raise_exception=True)
@permission_required('composition.change_composition', raise_exception=True)
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

@permission_required('composition.delete_composition', raise_exception=True)
@permission_required('composition.delete_compositionfile', raise_exception=True)
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


@permission_required('composition.add_compositionfile', raise_exception=True)
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

@permission_required('composition.delete_compositionfile', raise_exception=True)
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

@permission_required('composition.change_composition', raise_exception=True)
def checkAsActual(request, id):
    composition = get_object_or_404(Composition, id=id)
    composition.isActual = not composition.isActual
    composition.save()
    messages.success(request, f'Utwór "{composition.name}" zaznaczony jako {"Aktualny" if composition.isActual else "Nieaktualny"}.')
    return redirect('listComposition')

