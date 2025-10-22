
from date_extractor import extract_dates, read_file

def run_tests():

    print("Начинаем тестирование")
    print("=" * 50)
    
    # 1
    print("\n1. Тест основной функции:")
    text = "События произошли 4 октября 1957 года и 12 апреля 1961 года."
    expected = ["04/10/1957", "12/04/1961"]
    result = extract_dates(text)
    
    print(f"   Текст: '{text}'")
    print(f"   Ожидалось: {expected}")
    print(f"   Получено:  {result}")
    
    if result == expected:
        print("Все в порядке")
    else:
        print("У нас проблема")
    
    # 2
    print("\n2. Если в тексте нет даты:")
    
    zerodates_result = extract_dates("Это текст без дат.")
    print(f"   Текст без дат: {zerodates_result} (ожидается: [])")
    
    # 3
    print("\n3. Тест с файлом:")
    try:
        content = read_file("original_text.txt")
        file_dates = extract_dates(content)
        
        expected_dates = [
            "04/10/1957", "12/04/1961", "16/06/1963", 
            "21/07/1969", "19/04/1971"
        ]
        
        print(f"   Найдено дат в файле: {len(file_dates)}")
        print(f"   Ожидалось: {expected_dates}")
        print(f"   Получено:  {file_dates}")
        
        if file_dates == expected_dates:
            print("Все в порядке")
        else:
            print("У нас проблема")
            
    except FileNotFoundError:
        print("Файл 'original_text.txt' не найден, файловый тест невыполним")
    
    # 4
    print("\n4. Тест на формат дат:")
    original_format = "5 мая 2020 года и 10 декабря 1999 года"
    result_format = extract_dates(original_format)
    expected_format = ["05/05/2020", "10/12/1999"]
    
    print(f"   Текст: '{original_format}'")
    print(f"   Ожидалось: {expected_format}")
    print(f"   Получено:  {result_format}")
    
    if result_format == expected_format:
        print("С форматом все в порядке")
    else:
        print("С форматом есть проблема")

def main():
    """Основная функция тестирования"""
    try:
        run_tests()
        print("\n" + "=" * 50)
        print("Тестирование пройдено")
    except Exception as e:
        print(f"\n Произошла ошибка: {e}")

if __name__ == "__main__":
    main()