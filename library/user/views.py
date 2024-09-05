from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login, authenticate
from .forms import SignInForm, SignUpForm
from django.contrib import messages
from .models import User
from django.contrib.auth.models import Group
from .forms import UserPermissionsForm

def index(request):
    return render(request, 'user/index.html')


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Konto pomyślnie załozone.')
            return redirect('/user/signIn')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = SignUpForm()

    return render(request, 'user/signUpForm.html', {'form': form})


def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Poprawne dane do logowania.')
                return redirect('/')
            else:
                messages.error(request, f'Nieprawidłowe dane do logowania.')
                form.add_error(None, 'Nieprawidłowe dane do logowania')
    else:
        form = SignInForm()

    return render(request, 'user/signInForm.html', {'form': form})

@permission_required('user.change_user', raise_exception=True)
def manageUsers(request):
    users = User.objects.all()

    context = {
        'users': users,
        'form': UserPermissionsForm(),
    }
    return render(request, 'user/manage_users.html', context)

@permission_required('user.change_user', raise_exception=True)
def detailsUser(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user/details.html', {'user': user})

@permission_required('user.delete_user', raise_exception=True)
def deleteUser(request, id):
    user = get_object_or_404(User, id=id)
    user_name = user.name  # сохранить имя для уведомления

    try:      
        user.delete()

        messages.success(request, f'Konto "{user_name}" zostało pomyślnie usunięte.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć konta "{user_name}": {str(e)}')

    return redirect('manageUsers')

@permission_required('user.change_user', raise_exception=True)
def changeActive(request, id):
    user = get_object_or_404(User, id=id)
    if is_creator(user):
        messages.success(request, f'Nie wolno !')
        return redirect('detailsUser', id=id)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, f'Konto "{user.name} {user.surname}" zaznaczone jako {"Aktywne" if user.is_active else "Nieaktywne"}.')
    return redirect('detailsUser', id=id)

@permission_required('user.change_user', raise_exception=True)
def changeAccessAdminPanel(request, id):
    user = get_object_or_404(User, id=id)
    if is_creator(user):
        messages.success(request, f'Nie wolno !')
        return redirect('detailsUser', id=id)
    user.is_staff = not user.is_staff
    user.save()
    messages.success(request, f'"{user.name} {user.surname}" {"ma dostęp" if user.is_staff else "nie ma dostępu"} do panelu admina.')
    return redirect('detailsUser', id=id)

@permission_required('user.change_user', raise_exception=True)
def changeSuperadmin(request, id):
    user = get_object_or_404(User, id=id)
    if is_creator(user):
        messages.success(request, f'Nie wolno !')
        return redirect('detailsUser', id=id)
    user.is_superuser = not user.is_superuser
    user.save()
    messages.success(request, f'Konto"{user.name} {user.surname}" {"jest teraz" if user.is_superuser else "już nie jest"} superadminem.')
    return redirect('detailsUser', id=id)

@permission_required('user.change_user', raise_exception=True)
def changeGroup(request, id, group):
    user = get_object_or_404(User, id=id)
    if is_creator(user):
        messages.success(request, f'Nie wolno !')
        return redirect('detailsUser', id=id)
    grp = Group.objects.get(name=group)
    user.groups.set([grp])
    
    user.save()
    messages.success(request, f'Użytkownik "{user.name} {user.surname}" został przypisany do nowej grupy.')
    return redirect('detailsUser', id=id)

def is_creator(user):
    return (
        user.name == 'Jan' and 
        user.surname == 'Romanowski' and 
        user.email == 'leonovstarget@gmail.com'
    )
