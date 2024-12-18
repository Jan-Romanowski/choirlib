import csv
import os
import sys
import django
from django.shortcuts import get_object_or_404

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from folder.models import Folder

def main():
    csv_file_path = os.path.join(os.path.dirname(__file__), 'folder.csv')
# "id_folder","name_folder","note"
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)  # Стандартный DictReader
            for row in csv_reader:
                # Обработка возможных пустых значений
                id = row.get('id_folder', 'N/A').strip()
                name_folder = row.get('name_folder', 'N/A').strip()

                folder = Folder(
                    id=id,
                    name=name_folder,
                    colour='#ed9b2f'
                )
                
                # Сохранение объекта в базе данных
                folder.save()

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()