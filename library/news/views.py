from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import News
from .forms import NewsForm

def listNews(request):
    news = News.objects.all()
    return render(request, 'news/list.html', {'news': news})


def detailsNews(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/details.html', {'news': news})


def editNews(request, pk=None):
    if pk:
        post = get_object_or_404(News, pk=pk)
        action = 'update'
    else:
        post = None
        action = 'add'

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            if action == 'add':
                messages.success(request, f'Post {new_post.title} został pomyślnie opublikowany.')
            else:
                messages.success(request, f'Post {new_post.name} został pomyślnie zaktualizowany.')
        
            return redirect('listNews')
        else:
            messages.error(request, 'Coś poszło nie tak')
    else:
        form = NewsForm(instance=post)

    return render(request, 'news/form.html', {'form': form})


def deleteNews(request, pk):
    news = get_object_or_404(News, pk=pk)
    news_title = news.title

    try:
        news.delete()
        messages.success(request, f'Post "{news_title}" został pomyślnie usunięty.')
    except Exception as e:
        messages.error(request, f'Niestaty nie udało się usunąć post "{news_title}": {str(e)}')

    return redirect('listNews')


def uploadFiles(request, news_id):
    news = News.objects.get(id=news_id)
    
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        file_type = request.POST.get('file_type')
        
        for f in files:
            NewsFile.objects.create(
                news=news,
                file=f,
                file_type=file_type
            )
        
        messages.success(request, 'Plik pomyślnie wgrany.')
        return redirect('detailsComposition', id=news_id)
    else:
        form = UploadFileForm()
    
    return render(request, 'composition/uploadFiles.html', {'form': form, 'composition': composition})
