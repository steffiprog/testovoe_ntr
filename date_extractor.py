import re
import spacy

lemmatizer = spacy.load("ru_core_news_sm")

MONTH_DICT = {
    'январь': '01', 'февраль': '02', 'март': '03', 'апрель': '04',
    'май': '05', 'июнь': '06', 'июль': '07', 'август': '08',
    'сентябрь': '09', 'октябрь': '10', 'ноябрь': '11', 'декабрь': '12'
}

def lemmatize_text(text: str) -> str:
    cleaned_text = re.sub(r'(\d+)-[а-яё]+', r'\1', text)
    doc = lemmatizer(cleaned_text)
    lemmas = [token.lemma_.lower() for token in doc if not token.is_punct]
    return " ".join(lemmas)

def extract_dates(original_text: str) -> list[str]:
    new_text = lemmatize_text(original_text)
    pattern = r'(\d{1,2})\s+(\w+)\s+(\d{4})'
    raw_dates = re.findall(pattern, new_text)

    formatted_dates = []
    for day_str, month_name, year_str in raw_dates:
        if month_name in MONTH_DICT:
            formatted_dates.append(f"{int(day_str):02d}/{MONTH_DICT[month_name]}/{year_str}")
    return formatted_dates

def read_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    filename = "original_text.txt"

    try:
        content = read_file(filename)
        found_dates = extract_dates(content)
        print("Найденные даты:")
        for index, date in enumerate(found_dates, start=1):
            print(f"{index}. {date}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
