import csv
import os
import sys
import django
from django.shortcuts import get_object_or_404

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from folder.models import Folder
from composition.models import Composition

def main():
    csv_file_path = os.path.join(os.path.dirname(__file__), 'song.csv')

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)  # Стандартный DictReader
            for row in csv_reader:
                # Обработка возможных пустых значений
                id_song = row.get('id_song', 'N/A').strip()
                name_song = row.get('name_song', 'N/A').strip()
                count_p = row.get('count_p', 'N/A').strip() if row.get('count_p') not in ('', 'NULL') else 'N/A'
                author = row.get('author', 'N/A').strip()
                id_folder = row.get('id_folder', 'N/A').strip()
                one_voice = row.get('one_voice', 'N/A').strip() if row.get('one_voice') not in ('', 'NULL') else 'N/A'
                actual = row.get('actual', 'N/A').strip() if row.get('actual') not in ('', 'NULL') else 'N/A'
                note = row.get('note', 'N/A').strip() if row.get('note') not in ('', 'NULL') else 'N/A'
                views = row.get('views', 'N/A').strip()

                folderFromDB = get_object_or_404(Folder, id=id_folder)

                composition = Composition(
                    name=name_song,
                    author=author,
                    number=id_song,
                    folder=folderFromDB,
                    isActual=False
                )
                
                # Сохранение объекта в базе данных
                composition.save()

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()