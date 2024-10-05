from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import News
from .forms import NewsForm, NewsFile, UploadFileForm

def listNews(request):
    news = News.objects.all().order_by('-date_joined')
    return render(request, 'news/list.html', {'news': news})

def showPost(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/post.html', {'news': news})

# Jako Admin
@permission_required('news.change_news', raise_exception=True)
def detailsNews(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/details.html', {'news': news})

@permission_required('news.add_news', raise_exception=True)
@permission_required('news.change_news', raise_exception=True)
def editNews(request, id=None):
    if id:
        news = get_object_or_404(News, id=id)
        action = 'update'
    else:
        news = None
        action = 'add'

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            new_post = form.save()
            if action == 'add':
                messages.success(request, f'Post {new_post.title} został pomyślnie opublikowany.')
            else:
                messages.success(request, f'Post {new_post.title} został pomyślnie zaktualizowany.')
        
            return redirect('listNews')
        else:
            messages.error(request, 'Coś poszło nie tak')
    else:
        form = NewsForm(instance=news)

    return render(request, 'news/form.html', {'form': form, 'news': news})

@permission_required('news.delete_news', raise_exception=True)
def deleteNews(request, id):
    news = get_object_or_404(News, id=id)
    news_title = news.title

    try:
        for file in news.files.all():
            file.file.delete()
            file.delete()

        news.delete()
        messages.success(request, f'Post "{news_title}" został pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć post "{news_title}": {str(e)}')

    return redirect('listNews')

@permission_required('news.add_newsfile', raise_exception=True)
def uploadFiles(request, id):
    news = News.objects.get(id=id)
    
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        file_type = request.POST.get('file_type')
        
        for f in files:
            file_extension = f.name.split('.')[-1].lower()

            NewsFile.objects.create(
                news=news,
                file=f,
                file_type=file_extension
            )
        
        messages.success(request, 'Plik(i) pomyślnie wgrany.')
        return redirect('detailsNews', id=id)
    else:
        form = UploadFileForm()
    
    return render(request, 'news/uploadFiles.html', {'form': form, 'news': news})

def set_main_image(news_file_id):
    try:
        news_file = NewsFile.objects.get(id=news_file_id)
        news = news_file.news

        NewsFile.objects.filter(news=news, is_main=True).update(is_main=False)

        news_file.is_main = True
        news_file.save()

        return news.id
    except NewsFile.DoesNotExist:
        return False

@permission_required('news.change_news', raise_exception=True)
def set_main_image_view(request, news_file_id):
    if request.method == 'POST':
        success = set_main_image(news_file_id)
        if success:
            messages.success(request, 'Główne zdjęcie zostało ustawione pomyślnie.')
        else:
            messages.error(request, 'Nie udało się ustawić głównego zdjęcia.')
    
    return redirect('detailsNews', id=success)

@permission_required('news.change_news', raise_exception=True)
def checkAsActual(request, id):
    news = get_object_or_404(News, id=id)
    news.isActual = not news.isActual
    news.save()
    messages.success(request, f'Post "{news.title}" zaznaczony jako {"Aktualny" if news.isActual else "Nieaktualny"}.')
    return redirect('detailsNews', id=id)

@permission_required('news.delete_newsfile', raise_exception=True)
def deleteNewsFile(request, id):
    file = get_object_or_404(NewsFile, id=id)
    news_id = file.news.id
    
    try:
        file.file.delete()
        file.delete()
        messages.success(request, 'Plik pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Nie dało się usunąć pliku: {e}')
    
    return redirect('detailsNews', id=news_id)


