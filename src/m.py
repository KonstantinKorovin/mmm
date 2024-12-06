from datetime import datetime, timedelta


'''Напишите функцию, которая принимает список дат в формате списка строк, например ["2022.12.31", "2023.1.7"], 
и возвращает список дат в формате строк через одну неделю, например ["January 7, 2023", "January 14, 2023"]'''


def sort_date(data):
    output_dates = []
    for date in data:
        date_obj = datetime.strptime(date, '%Y.%m.%d')
        new_date_obj = date_obj + timedelta(days=7)
        output_dates.append(new_date_obj.strftime('%B %d, %Y'))
    return output_dates

print(sort_date(["2022.12.31", "2023.1.7"]))



from src.code import add_week_to_dates

def test_add_week_to_dates():
    assert add_week_to_dates(["2022.12.31", "2023.1.7"]) == ["January 7, 2023", "January 14, 2023"]
    assert add_week_to_dates([]) == []