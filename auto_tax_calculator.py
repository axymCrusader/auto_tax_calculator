from datetime import datetime

engine_capacity = int(input('Введите мощность автомобиля: '))

car_price = float(input('Введите цену автомобиля: '))

registration_year = int(input('Введите год регистрации автомобиля: '))
registration_month = int(input('Введите месяц регистрации автомобиля: '))
registration_day = int(input('Введите день регистрации автомобиля: '))

vehicle_year = int(input('Введите год выпуска автомобиля: '))
vehicle_month = int(input('Введите месяц выпуска автомобиля: '))
vehicle_day = int(input('Введите день выпуска автомобиля: '))
    

avance_pay = [0,0,0]
tax_rate = 0.0
increasing_coefficient = 0.0
auto_tax = 0.0
i = 0
j = 3
month = 0
current_year = datetime.now().year

tax_rate = (2.5 if engine_capacity <= 100 else
    3.5 if engine_capacity > 100 and engine_capacity <= 150 else
    5 if engine_capacity > 150 and engine_capacity <= 200 else
    7.5 if engine_capacity > 200 and engine_capacity <= 250 else
    15 if engine_capacity > 250 else
    15
)

increasing_coefficient = (1.1 if car_price > 3 and car_price <= 5 and current_year - vehicle_year <= 3 else
            2 if car_price > 5 and car_price <= 10 and current_year - vehicle_year <= 5 else
            3 if car_price > 10 and car_price < 15 and current_year - vehicle_year <= 10 else
            5 if car_price > 15 and current_year - vehicle_year <= 20 else
            5
)

month = registration_month
if (registration_day <= 15):
    month -= 1

month_count = ((12 - month) / 12)

auto_tax = engine_capacity * tax_rate * month_count * increasing_coefficient

while j <= 9:
    if month - j < 0:
        avance_pay[i] = 1 / 4.0 * tax_rate * engine_capacity * ((j - month) / 3.0) * increasing_coefficient
        month = j
        i += 1
    else:
        i += 1

    j += 3

auto_tax = auto_tax - avance_pay[0] - avance_pay[1] - avance_pay[2]

print(f"Авансовые платеж 1: {avance_pay[0]} RUB")
print(f"Авансовые платеж 2: {avance_pay[1]} RUB")
print(f"Авансовые платеж 3: {avance_pay[2]} RUB")
print(f"транспортный налог: {auto_tax} RUB")






