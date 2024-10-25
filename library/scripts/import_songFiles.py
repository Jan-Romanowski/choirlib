import os
import sys
import django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from composition.models import Composition, CompositionFile

def main():
    # Путь к директории с файлами
    files_directory = os.path.join(settings.MEDIA_ROOT, 'compositions')

    try:
        # Перебор всех папок в указанной директории
        for folder in os.listdir(files_directory):
            folder_path = os.path.join(files_directory, folder)
            if os.path.isdir(folder_path):
                # Получаем номер произведения из имени папки
                try:
                    composition_number = int(folder)
                    # Перед строкой с get_object_or_404
                    print(f'Обрабатываем папку: {folder}, номер произведения: {composition_number}')

                    composition = get_object_or_404(Composition, number=composition_number)

                    # Перебор всех файлов в папке
                    for filename in os.listdir(folder_path):
                        if filename.endswith(('.mp3', '.wav', '.pdf')):  # Проверяем только файлы нужных форматов
                            # Определение типа файла
                            file_type = filename.split('.')[-1]
                            file_record = CompositionFile(
                                composition=composition,
                                file=os.path.join('compositions', str(composition.number), filename),
                                file_type=file_type
                            )
                            file_record.save()
                            print(f'Файл {filename} успешно добавлен для произведения {composition.name}.')

                except ValueError:
                    print(f'Не удалось преобразовать имя папки в номер произведения: {folder}')

    except FileNotFoundError:
        print("Директория с файлами не найдена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
