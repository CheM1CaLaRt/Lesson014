import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# URL страницы для парсинга
url = "https://www.divan.ru/category/svet"

# Открытие страницы
driver.get(url)

# Подождать, пока страница полностью загрузится
time.sleep(3)

# Нахождение всех элементов с информацией о светильниках
lights = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

# Открытие файла для записи данных в CSV
with open('lights.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'URL'])  # Заголовки столбцов

    # Парсинг информации о каждом светильнике и запись в CSV файл
    for light in lights:
        name = light.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = light.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = light.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        writer.writerow([name, price, url])

# Закрытие браузера
driver.quit()

print("Данные успешно сохранены в CSV файл.")