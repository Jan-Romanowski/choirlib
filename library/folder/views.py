from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Folder
from .forms import FolderForm

def listFolder(request):
    folders = Folder.objects.prefetch_related('compositions').all()
    return render(request, 'folder/folderList.html', {'folders': folders})


def detailsFolder(request, id):
    folder = get_object_or_404(Folder, id=id)
    return render(request, 'folder/folderDetails.html', {'folder': folder})


def editFolder(request, pk=None):
    if pk:
        folder = get_object_or_404(Folder, pk=pk)
        action = 'update'  # Действие — обновление
    else:
        folder = None
        action = 'add'  # Действие — добавление

    if request.method == 'POST':
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            new_folder = form.save()
            if action == 'add':
                messages.success(request, f'Teczka {new_folder.name} została pomyślnie dodana do biblioteki.')
            else:
                messages.success(request, f'Teczka {new_folder.name} została pomyślnie zaktualizowana.')
            
            return redirect('listFolder')
        else:
            messages.error(request, 'Coś poszło nie tak')
    else:
        form = FolderForm(instance=folder)

    return render(request, 'folder/folderForm.html', {'form': form})


def deleteFolder(request, pk):
    folder = get_object_or_404(Folder, pk=pk)
    folder_name = folder.name  # сохранить имя для уведомления

    try:
        folder.delete()
        messages.success(request, f'Teczka "{folder_name}" została pomyślnie usunięta.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć teczki "{folder_name}": {str(e)}')

    return redirect('listFolder')