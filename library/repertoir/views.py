from django.shortcuts import render, redirect, get_object_or_404
from .models import Repertoir
from .forms import RepertoirForm
from django.contrib import messages

def listRepertoirs(request):
    repertoirs = Repertoir.objects.prefetch_related('compositions').all()
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
                messages.success(request, f'Repertuar {new_repertoir.name} został pomyślnie dodany do biblioteki.')
            else:
                messages.success(request, f'Repertuar {new_repertoir.name} został pomyślnie zaktualizowany.')
            
            return redirect('listFolder')
        else:
            messages.error(request, 'Coś poszło nie tak')
    else:
        form = RepertoirForm(instance=repertoir)

    return render(request, 'repertoir/form.html', {'form': form})