import csv


with open("plinara.csv") as f:
    rows = csv.reader(f, delimiter="\t")
    for row in rows:
        plinomjer, opis, datum, stanje = row
        stanje = int(stanje)
        day, month, year = map(int, datum.split("."))
        match opis:
            case "PROCJENA":
                pass
            case "DOJAVA":
                pass
            case "REKLAMACIJA":
                pass
            case "OČITANO":
                pass
            case "STORNO":
                pass
            case "DEMONTIRANO":
                pass
            case "PROCJENA OPSKRBLJIVAČA":
                pass

        # print(plinomjer, opis, day, month, year, stanje)
