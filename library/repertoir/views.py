from django.shortcuts import render, redirect, get_object_or_404
from .models import Repertoir
from .forms import RepertoirForm
from django.contrib import messages

def listRepertoirs(request):
    repertoirs = Repertoir.objects.all().order_by('-id')
    return render(request, 'repertoir/list.html', {'repertoirs': repertoirs})

def editRepertoir(request, pk=None):
    if pk:
        repertoir = get_object_or_404(Repertoir, pk=pk)
        action = 'update'
    else:
        repertoir = None
        action = 'add'

    if request.method == 'POST':
        form = RepertoirForm(request.POST, instance=repertoir)
        if form.is_valid():
            new_repertoir = form.save()
            if action == 'add':
                messages.success(request, f'Repertuar {new_repertoir.title} został pomyślnie dodany do biblioteki.')
            else:
                messages.success(request, f'Repertuar {new_repertoir.title} został pomyślnie zaktualizowany.')
            
            return redirect('listRepertoirs')
        else:
            messages.error(request, 'Coś poszło nie tak')
    else:
        form = RepertoirForm(instance=repertoir)

    return render(request, 'repertoir/form.html', {'form': form})


def deleteRepertoir(request, pk):
    repertoir = get_object_or_404(Repertoir, pk=pk)
    repertoir_name = repertoir.title  # сохранить имя для уведомления

    try:
        repertoir.delete()
        messages.success(request, f'Teczka "{repertoir_name}" została pomyślnie usunięta.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć teczki "{repertoir_name}": {str(e)}')

    return redirect('listRepertoirs')