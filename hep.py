import json
from datetime import date
from collections import defaultdict
from dateutil.relativedelta import relativedelta
from itertools import count

# from pprint import pprint

with open("hep.json") as f:
    data = json.loads(f.read().strip())

akontacija = 0
uplaceno = 0
racun = -148.78  # početni dug 2019.
last_calc_date = date(year=2019, month=10, day=1)
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

first_date = date(year=2019, month=10, day=1)

while month_amounts:
    print(f"{first_date}: {round(month_amounts.pop(first_date), 2)}")
    first_date += relativedelta(months=1)

dug = round(racun + akontacija - uplaceno, 2)
print(f"{dug=}")
