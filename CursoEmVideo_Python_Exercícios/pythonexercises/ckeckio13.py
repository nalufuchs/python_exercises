"""""
def convert_date(date: str) -> str:
    if len(date) == 10 and date[2] == "/" and date[5] == "/":
        mes = date[3:5]
        dia = date[:2]
        ano = date[6:]
        if mes == '02':
            dia = int(dia)
            if dia >= 29:
                return "Error: Invalid date"
            else:
                dia = str(dia)
        return f'{ano}-{mes}-{dia}'
    else:
        return "Error: Invalid date."

"""""

def convert_date(date: str) -> str:
    try:
        # Split the input string into day, month, and year
        day, month, year = date.split('/')

        # Verificamos se o dia, o mês e o ano são compostos apenas por números.
        # Se algum deles não for um número, isso significa que a entrada está em um formato incorreto.
        # Nesse caso, a função lançará um erro
        if not day.isdigit() or not month.isdigit() or not year.isdigit():
            raise ValueError("Error: Invalid date.")  #raise é = except, mas não exige o try

        # convertendo o número em inteiro:
        day, month, year = int(day), int(month), int(year)


       #se o mês está entre 1 e 12 e se o dia está entre 1 e 31.
        # Isso ajuda a garantir que a data esteja dentro de intervalos válidos.
        # Se essa verificação falhar, a função também lançará um erro.
        if month < 1 or month > 12 or day < 1 or day > 31 or 1900 < year or year > 2100:
            raise ValueError("Error: Invalid date.")  #raise permite frases personalizadas
        if month == 2 and day > 28:
            raise ValueError("Error: Invalid date.")
        # a função construirá uma nova data no formato desejado, que é "yyyy-mm-dd".
        # Os valores de ano, mês e dia são formatados para que
        # tenham sempre dois dígitos para o mês e o dia, e quatro dígitos para o ano.
        output_date = f"{year:04d}-{month:02d}-{day:02d}"

        return output_date
    except (ValueError, IndexError):
        return "Error: Invalid date."




print("Example:")
print(convert_date("01/01/2023"))
print(convert_date("25/12/2021"))
print(convert_date("01/01/2000"))
print(convert_date("15/06/1995"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."