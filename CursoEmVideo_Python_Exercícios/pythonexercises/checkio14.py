date = "01/01/2003"  #isso tem que dar 2003 - 01 - 01
dia, mes, ano = date.split("/")

if len(date) == 10 and date[2] == "/" and date[5] == "/":
    mes = int(date[3:5])
    dia = int(date[:2])
    ano = int(date[6:])
    if dia > 31 or dia < 1 or mes > 12 or mes < 1 or ano > 1900 or ano > 2100:
        print("Error: Invalid date.")
    else:
        if mes == 2 and dia > 28:
            print("Error: Invalid date.")
        print(f"{ano:04d}{mes:02d}{dia:02d}")


