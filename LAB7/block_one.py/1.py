import pickle

medals = {
    "США": [46, 37, 38, 43, 47, 41],
    "Китай": [38, 29, 25, 32, 36, 38],
    "Россия": [33, 23, 19, 24, 29, 27],
    "Великобритания": [29, 24, 23, 27, 22, 67],
    "Германия": [26, 24, 30, 23, 31, 27],
    "Япония": [27, 18, 15, 22, 30, 22],
    "Австралия": [17, 25, 22, 20, 24, 20]
}

total_medals = {country: sum(medals[country]) for country in medals}
print("Список стран и количество медалей:")
for country, total in total_medals.items():
    print(f"{country}: {total} медалей")
    
average_medals = {country: sum(medals[country]) / len(medals[country]) for country in medals}
max_country = max(average_medals, key=average_medals.get)
min_country = min(average_medals, key=average_medals.get)
print(f"\nСтрана с максимальным средним числом медалей: {max_country} ({average_medals[max_country]:.2f})")
print(f"Страна с минимальным средним числом медалей: {min_country} ({average_medals[min_country]:.2f})\n") 


for country in medals:
    max_year = medals[country].index(max(medals[country])) + 1
    print(f"{country} завоевала наибольшее количество медалей в {max_year} году.")

# Выделение стран с ростом медалей более чем на 20%
growth_countries = []
for country in medals:
    if ((medals[country][-1] - medals[country][0]) / medals[country][0]) > 0.2:
        growth_countries.append(country)

print("\nСтраны с ростом медалей более чем на 20%:", growth_countries)   

# Сохранение словаря в бинарный файл
with open('data.txt', 'wb') as f:
    pickle.dump(medals, f)

# Чтение данных из бинарного файла
with open('data.txt', 'rb') as f:
    loaded_medals = pickle.load(f)
    print("\nЗагруженные данные из файла:", loaded_medals)