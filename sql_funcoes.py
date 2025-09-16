import sqlite3

# ------------------ CRIAR TABELA -------------------------------
def criarTabela(nomeDB):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    queryTabela = '''CREATE TABLE IF NOT EXISTS "Contatos" (
        "id"            INTEGER,
        "nome"          TEXT,
        "sobrenome"     TEXT,
        "email"         TEXT,
        PRIMARY KEY ("id" AUTOINCREMENT)
    );'''

    cursor.execute(queryTabela)
    conn.commit()
    conn.close()


# ------------------ INSERIR DADOS -------------------------------
def inserirDados(nomeDB, nome, sobrenome, email):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    queryInserir = f'''INSERT INTO Contatos (nome, sobrenome, email)
        VALUES ("{nome}", "{sobrenome}", "{email}");'''
    
    cursor.execute(queryInserir)
    conn.commit()
    conn.close()

# -------------------- ATUALIZAR DADOS ----------------------
def atualizarDados(nomeDB, nome, sobrenome, email, num_registro):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    if len(nome) != 0 and nome != '\r':
        queryUpdate = f'''UPDATE Contatos SET nome="{nome}" 
            WHERE id="{num_registro}";'''
        cursor.execute(queryUpdate)
        conn.commit()

    if len(sobrenome) != 0 and sobrenome != '\r':
        queryUpdate = f'''UPDATE Contatos SET sobrenome="{sobrenome}" 
            WHERE id="{num_registro}";'''
        cursor.execute(queryUpdate)
        conn.commit()

    if len(email) != 0 and email != '\r':
        queryUpdate = f'''UPDATE Contatos SET email="{email}" 
            WHERE id="{num_registro}";'''
        cursor.execute(queryUpdate)
        conn.commit()
    
    conn.close()

# -------------------- APAGAR DADOS ----------------------
def apagarDado(nomeDB, num_registro):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    queryDelete = f'''DELETE FROM Contatos 
        WHERE id="{num_registro}";'''
    
    cursor.execute(queryDelete)

    conn.commit()
    conn.close()

# -------------------- SELECIONAR TUDO ------------------------------------
def selecionarTodosDados(nomeDB):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    querySelectAll = '''SELECT * FROM Contatos;'''
    cursor.execute(querySelectAll)

    dados = cursor.fetchall()

    conn.commit()
    conn.close()

    return dados

# ------------------------- SELECIONAR PARCIAL ----------------
def selecionarDadosParcial(nomeDB, quantidade, inicio):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    querySelect = f'''SELECT * FROM Contatos
        LIMIT {quantidade} OFFSET {inicio};'''
    cursor.execute(querySelect)

    dados = cursor.fetchall()

    conn.commit()
    conn.close()

    return dados