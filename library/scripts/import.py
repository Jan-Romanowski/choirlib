import csv
import os

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

                print(f"ID: {id_song}, Song: {name_song}, Count: {count_p}, Author: {author}, Folder ID: {id_folder}, One Voice: {one_voice}, Actual: {actual}, Note: {note}, Views: {views}")
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()