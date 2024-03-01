#27.	Определить суммарную стоимость билетов пассажиров на борту в возрастном интервале мода  5 лет 

import csv
import statistics

with open('C:/Users/Пк/Desktop/13/titanic.csv','r') as file:
    reader = csv.DictReader(file)
    summ_price = 0
    ages = []

    for row in reader:
        age = row['Age']
        if age.isdigit():
            if '.' in age:
                float_age = float(age)
                ages.append(float_age)
            else:
                ages.append(int(age))

    mode_age = statistics.mode(ages)   

    file.seek(0)

    for row in reader:
        age = row['Age']
        if age.isdigit():
            if mode_age-5 <= float(age) <= mode_age+5:
                summ_price += float(row['Fare'])

print(f'Суммарная стоимость билетов равна {summ_price}')

