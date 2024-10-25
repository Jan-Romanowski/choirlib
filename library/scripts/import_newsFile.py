import csv
import os
import sys
import django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

BASE_NEWS_FOLDER_PATH = os.path.join(settings.MEDIA_ROOT, 'news')
from news.models import News, NewsFile

# File types to filter
ACCEPTED_FILE_TYPES = ('.png', '.jpg', '.jpeg')

def add_news_files():
    for folder_name in os.listdir(BASE_NEWS_FOLDER_PATH):
        folder_path = os.path.join(BASE_NEWS_FOLDER_PATH, folder_name)
        
        if not os.path.isdir(folder_path):
            continue  # Skip if not a directory
        
        try:
            # Find the News instance by folder name (assuming it matches the news ID)
            news_instance = News.objects.get(id=folder_name)
        except ObjectDoesNotExist:
            print(f"No News entry found for ID {folder_name}")
            continue

        # Add each file in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if not os.path.isfile(file_path):
                continue  # Skip if not a file
            
            # Check if file has an acceptable extension
            ext = os.path.splitext(filename)[1].lower()
            if ext not in ACCEPTED_FILE_TYPES:
                continue
            
            # Determine file type for the NewsFile model
            file_type = ext[1:]  # Remove the dot (e.g., ".jpg" -> "jpg")

            try:
                # Create a NewsFile instance
                news_file = NewsFile(
                    news=news_instance,
                    file=os.path.join('news', folder_name, filename),
                    file_type=file_type,
                    is_main=False  # Set is_main based on your needs
                )
                news_file.save()
                print(f"Added {filename} to News ID {folder_name}")
            except IntegrityError as e:
                print(f"Error adding {filename} to News ID {folder_name}: {e}")

if __name__ == '__main__':
    add_news_files()
