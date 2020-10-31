import datetime

#datetime.date(y,m,d).weekday() returns 0 for mon, 6 for sun

def sunday_counter(first_year,final_year):
    number_of_sundays = 0
    for y in range(first_year,final_year+1):
        for m in range(1,13):
            if datetime.date(y,m,1).weekday() == 6:
                number_of_sundays += 1
    return number_of_sundays

print(f'''{sunday_counter(1901,2000)} Sundays fell on the first of the month during the twentieth century.''')