from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import News
from .forms import NewsForm, NewsFile, UploadFileForm

def listNews(request):
    news = News.objects.all()
    return render(request, 'news/list.html', {'news': news})


def detailsNews(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/details.html', {'news': news})


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


def deleteNews(request, id):
    news = get_object_or_404(News, id=id)
    news_title = news.title

    try:
        news.delete()
        messages.success(request, f'Post "{news_title}" został pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć post "{news_title}": {str(e)}')

    return redirect('listNews')

def uploadFiles(request, id):
    news = News.objects.get(id=id)
    
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        file_type = request.POST.get('file_type')
        
        for f in files:
            NewsFile.objects.create(
                news=news,
                file=f,
                file_type=file_type
            )
        
        messages.success(request, 'Plik(i) pomyślnie wgrany.')
        return redirect('detailsNews', id=id)
    else:
        form = UploadFileForm()
    
    return render(request, 'news/uploadFiles.html', {'form': form, 'news': news})
