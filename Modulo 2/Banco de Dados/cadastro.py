import sqlite3

registro = 'senha.db'

script_alunos = """CREATE TABLE IF NOT EXISTS Alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                email TEXT NOT NULL
            );"""

try:
    with sqlite3.connect(registro) as conn:
        cur = conn.cursor()
        cur.execute(script_alunos)
        conn.commit()
        print("Tabelas Criadas com Sucesso")
except sqlite3.OperationalError as e:
    print("ERRO: ", e)

email = input('Digite seu email: ')
senha = input('Digite sua Senha: ')

sql = "INSERT INTO login (email, senha ) VALUES (?,?)"

try:
    with sqlite3.connect(registro) as conn:
        cur = conn.cursor()
        cur.execute(sql, (email, senha))
        conn.commit()
except sqlite3.OperationalError as e:
    print("ERRO: ", e)

sql = "SELECT * FROM Alunos"


try:
    with sqlite3.connect(registro) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall() 
        print(res)
except sqlite3.OperationalError as e:
    print("ERRO: ", e)