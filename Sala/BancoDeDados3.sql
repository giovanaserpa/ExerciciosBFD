import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("escola_v2.db")
cursor = conn.cursor()

/* 1. Pegar toda a tabela Aluno*/
cursor.execute("SELECT * FROM Aluno;")
alunos = cursor.fetchall()
print("Tabela Aluno:")
for aluno in alunos:
    print(aluno)

/*2. Média entre nota1 e nota2, ordenando em ordem decrescente e pegando as 10 maiores*/
cursor.execute("""
    SELECT idAluno, nome, (nota1 + nota2) / 2 AS media
    FROM Aluno
    ORDER BY media DESC
    LIMIT 10;
""")
top10 = cursor.fetchall()
print("\nTop 10 maiores médias:")
for aluno in top10:
    print(aluno)

/*# 3. Left Join entre Aluno e Turma*/
cursor.execute("""
    SELECT *
    FROM Aluno
    LEFT JOIN Turma ON Aluno.idTurma = Turma.idTurma;
""")
join_result = cursor.fetchall()
print("\nLeft Join Aluno x Turma:")
for linha in join_result:
    print(linha)

/*4. Filtrar apenas alunos da turma 2*/
cursor.execute("""
    SELECT *
    FROM Aluno
    LEFT JOIN Turma ON Aluno.idTurma = Turma.idTurma
    WHERE Aluno.idTurma = 2;
""")
turma2 = cursor.fetchall()
print("\nAlunos da Turma 2:")
for aluno in turma2:
    print(aluno)

conn.close()
