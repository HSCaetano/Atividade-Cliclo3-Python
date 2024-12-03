import sqlite3


conn = sqlite3.connect('imc_database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        peso REAL,
        altura REAL,
        imc REAL,
        data TEXT
    )
''')


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def salvar_imc(nome, peso, altura, imc):
    import datetime
    data_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO pacientes (nome, peso, altura, imc, data) VALUES (?, ?, ?, ?, ?)
    ''', (nome, peso, altura, imc, data_atual))
    conn.commit()


nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)
print(f"O seu IMC é: {imc:.2f}")


salvar_imc(nome, peso, altura, imc)


conn.close()
