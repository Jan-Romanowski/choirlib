from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

class UserAdmin(BaseUserAdmin):
    # Поля, которые будут отображаться в списке пользователей
    list_display = ('email', 'name', 'surname', 'is_staff', 'is_admin')
    
    # Поля, по которым можно будет искать пользователей
    search_fields = ('email', 'name', 'surname')
    
    # Поля, которые будут использоваться в форме редактирования/создания пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'surname')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_regular_user')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Поля, которые будут использоваться при создании нового пользователя через админку
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'password1', 'password2'),
        }),
    )
    
    ordering = ('email',)

# Регистрация модели и её админ-класса
admin.site.register(User, UserAdmin)

# Если вам не нужна стандартная группа пользователей, можете её удалить из админки
admin.site.unregister(Group)
