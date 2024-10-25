import csv
import os
import sys
import django
from django.shortcuts import get_object_or_404

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from repertoir.models import Repertoir

def main():
    csv_file_path = os.path.join(os.path.dirname(__file__), 'repertoire.csv')
# "id_folder","name_folder","note"
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)  # Стандартный DictReader
            for row in csv_reader:
                # Обработка возможных пустых значений
                title = row.get('header', 'N/A').strip()
                text = row.get('text', 'N/A').strip()

                repertoir = Repertoir(
                    title=title,
                    text=text
                )
                
                # Сохранение объекта в базе данных
                repertoir.save()

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()