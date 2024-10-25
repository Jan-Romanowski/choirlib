import csv
import os
import sys
import django
from django.shortcuts import get_object_or_404

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from news.models import News
from datetime import datetime

def main():
    csv_file_path = os.path.join(os.path.dirname(__file__), 'news.csv')
# "id_folder","name_folder","note"
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)  # Стандартный DictReader
            for row in csv_reader:
                # Обработка возможных пустых значений
                id = row.get('id_news', 'N/A').strip()
                header = row.get('header', 'N/A').strip()
                text = row.get('text', 'N/A').strip()
                date = row.get('date_news', 'N/A').strip()
                autor = row.get('autor', 'N/A').strip()

                date_only = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date() if date != 'N/A' else None
                print(f"ID: {id}, header: {header}, text: {text}, date: {date}, autor: {autor}")

                news = News(
                    id = id,
                    title=header,
                    text=text,
                    isActual=False,
                    date_joined=date_only
                )
                news.save()

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()