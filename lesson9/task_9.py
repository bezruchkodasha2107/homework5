'''
Дан словарь, 
ключ - название страны, значение - список городов, 
на вход поступает город, необходимо сказать из какой он страны
'''

def find_country(city, countries):
    result = filter(lambda country: city in countries[country], countries)
    return list(result)

countries = {
    "Россия": ["Москва", "Санкт-Петербург", "Екатеринбург"],
    "США": ["Нью-Йорк", "Лос-Анджелес", "Чикаго"],
    "Франция": ["Париж", "Марсель", "Лион"]
}

city_to_find = "Москва"


countries_with_city = find_country(city_to_find, countries)
print(f"Город {city_to_find} находится в стране: {', '.join(countries_with_city)}")

