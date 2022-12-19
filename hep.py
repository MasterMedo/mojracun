import json
from datetime import date
from collections import defaultdict
from dateutil.relativedelta import relativedelta
from itertools import count


FIRST_MONTH = date(year=2019, month=10, day=1)
CURRENT_DEBT = 189.61


with open("hep.json") as f:
    data = json.loads(f.read().strip())

akontacija = 0
uplaceno = 0
racun = 0
last_calc_date = FIRST_MONTH
month_amounts = defaultdict(int)
for line in reversed(data["promet_lista"]):
    year, month, day = map(int, line["Datum"][:10].split("-"))
    current_date = date(year=year, month=month, day=1)
    match line["Opis"]:
        case "Akontacija":
            akontacija += round(line["Duguje"], 2)
            month_amounts[current_date] += line["Duguje"]
        case "Uplaćeno":
            uplaceno += line["Potrazuje"]
        case "Račun":
            dates = [current_date]
            for i in count(1):
                tmp_month = current_date - relativedelta(months=i)
                dates.append(tmp_month)
                if tmp_month == last_calc_date:
                    last_calc_date = current_date
                    break

            average = line["Duguje"] / len(dates)
            for x in reversed(dates):
                month_amounts[x] += average

            racun += round(line["Duguje"], 2)

first_date = FIRST_MONTH
initial_debt = round(racun + akontacija - uplaceno - CURRENT_DEBT, 2)
month_amounts[first_date] += initial_debt


while month_amounts:
    print(f"{first_date}: {round(month_amounts.pop(first_date), 2)}")
    first_date += relativedelta(months=1)
