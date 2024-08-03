import datetime

print('Введи дату своего рождения.')
day = int(input('День: '))
month = int(input('Месяц: '))
year = int(input('Год: '))
today = datetime.date.today()
dateresult = datetime.date(year=year, month=month, day=day)


print(f'Tебе {today.year - year - ((today.month, today.day) < (month, day))} лет!')
print(f'Это было в {dateresult.strftime('%A %d %m %Y')}')

if year % 4 != 0:
    print('Год не високосный.')

elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный.')
    else:
        print('Год не високосный.')
else:
    print('Год високосный.')
