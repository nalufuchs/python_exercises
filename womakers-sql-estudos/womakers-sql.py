import sqlite3

conexao = sqlite3.connect('projeto-sql-dbeaver-womakers')

cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios (id int, nome VARCHAR (100), endereco VARCHAR (100), email VARCHAR (50));')

#cursor.execute('ALTER TABLE usuarios ADD COLUMN telefone int')

cursor.execute('INSERT INTO usuarios (id, nome, endereco, email, telefone) VALUES (1, "Isadora", "França", "isadora@gmail.com", 244355664)')
cursor.execute('INSERT INTO usuarios (id, nome, endereco, email, telefone) VALUES (2, "Felipe", "Brasil", "fefe@gmail.com", 863847389)')
cursor.execute('INSERT INTO usuarios (id, nome, endereco, email, telefone) VALUES (3, "Mariana", "Alemanha", "mari@hotmail.com", 387467954)')
cursor.execute('INSERT INTO usuarios (id, nome, endereco, email, telefone) VALUES (4, "Lucas", "Canadá", "felipe@gmail.com", 986843524)')
conexao.commit()
conexao.close()