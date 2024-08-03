# composition/templatetags/composition_extras.py
from django import template

register = template.Library()

@register.filter
def is_audio(file_type):
    return file_type in ['mp3', 'wav']

@register.filter
def is_pdf(file_type):
    return file_type == 'pdf'

@register.filter
def get_filename_without_extension(path):
    """
    Extracts the filename from a path and removes its extension.
    """
    filename = path.rsplit('/', 1)[-1] if '/' in path else path
    return filename.split('.')[0] if '.' in filename else filename
