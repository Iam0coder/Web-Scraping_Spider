import scrapy
import csv

# Определяем разрешенные домены для парсинга. В данном случае это сайт divan.ru
ALLOWED_DOMAINS = ["https://divan.ru"]

# URL, с которого начнется парсинг
START_URLS = ["https://www.divan.ru/category/svet"]


# Создаем класс для нашего паука (spider), который наследует класс scrapy.Spider
class DivannewparsSpider(scrapy.Spider):
    # Имя паука, которое будет использоваться для его запуска
    name = "divannewpars"
    # Разрешенные домены, на которых паук будет работать
    allowed_domains = ALLOWED_DOMAINS
    # URL, с которых паук начнет свою работу
    start_urls = START_URLS

    # Основной метод парсинга, который будет вызван для каждого URL в start_urls
    def parse(self, response):
        # Используем CSS-селектор для нахождения всех нужных элементов на странице
        divans = response.css("div._Ud0k")

        # Открываем CSV-файл для записи данных
        with open("divan.csv", "w", newline="", encoding="utf-8") as file:
            # Создаем объект writer для записи в CSV
            writer = csv.writer(file)
            # Записываем заголовок в CSV-файл
            writer.writerow(["Модель светильника", "Цена", "Ссылка"])

            # Проходим по каждому найденному элементу
            for divan in divans:
                # Извлекаем название светильника с использованием CSS-селектора
                name = divan.css("div.lsooF span::text").get()
                # Извлекаем цену светильника с использованием CSS-селектора
                price = divan.css("div.pY3d2 span::text").get()
                # Извлекаем ссылку на светильник и формируем полный URL
                url = ALLOWED_DOMAINS[0] + divan.css("a").attrib["href"]
                # Создаем список с данными для записи в CSV-файл
                divan = [name, price, url]
                # Записываем данные в CSV-файл
                writer.writerow(divan)
