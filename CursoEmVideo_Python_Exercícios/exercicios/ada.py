#presença >= 60%
#media >= 7
#função:
#lista de dicionarios contendo:
#nome do candidato,
#Média de desempenho
#quantidade de horas de AUSENCIA do treinamento
#funcao deve calcular se o candidato tá qualificado ou nao
#presença calculada considerando q o treinamento teve 60h
#(total de horas - numero de faltas)/total horas * 100

def avaliacao(info_candidatos):
    for candidato in info_candidatos:
        presenca = ((60 - candidato['horas_ausencia']) / 60) * 100
        if presenca >= 60 and candidato['media_desempenho'] >= 7:
            print(f"{candidato['nome']} está qualificado.")
        else:
            print(f"{candidato['nome']} não está qualificado.")

# Exemplo de uso
candidatos = [
    {"nome": "Alice", "media_desempenho": 8, "horas_ausencia": 10},
    {"nome": "Bob", "media_desempenho": 6, "horas_ausencia": 5},
    {"nome": "Charlie", "media_desempenho": 7.5, "horas_ausencia": 15},
]

