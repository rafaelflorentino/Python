# pip install flask (no terminal)
# pip install textblob
# importando modulos
from flask import Flask,render_template,request,redirect,url_for
import urllib.parse
# realizar o mapeamento objeto relacional -DB First
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from animal import Animal
from avaliacao import Avaliacao
from sqlalchemy.orm import sessionmaker
from textblob import TextBlob
# definindo objeto flask
app = Flask(__name__)

app.secret_key = "df6e83eb7983f75b2561c875cbebc40ab9900624b22c6040f5831ecd6faaea429f043b35bd5a6fae4692fa6c80fdcf060f61207f53eb744ba684f84517fc9881sua chave secreta"
# ==========================================
# senha : @
# tratar o arroba de uma senha
# importe urlib.parse
# =========================================
#              info do bd
user = 'root'
password = urllib.parse.quote_plus('')
host = 'localhost'
database = 'zooflask'
# ==========================================
#           connection string
connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'
# ==========================================
# ==========sqlalchemy-orm-db first=========
# 1. instalar o SQLAlchemy
# 2. crie o motor 

"""
A função create_engine cria uma interface 
que permite a comunicação entre o aplicativo web
e o banco de dados

"""
engine = create_engine(connection_string)

#  Refletindo o Banco de Dados
metadata = MetaData()
metadata.reflect(engine)

"""
-- Cria uma classe base que vai mapear 
-- Automaticamente as tabelas do banco de dados 
-- Que estão descritas no objeto metadata.

"""
Base = automap_base(metadata=metadata) # definindo a classe

"""
--Esse método realiza o mapeamento das tabelas para classes Python, 
--Gera uma classe para cada tabela 
--Pode ser usada para interagir com os dados diretamente.
"""
Base.prepare() # mapeando


# Ligando com a classe
Animal =  Base.classes.animal
Avaliacao = Base.classes.avaliacao

# Criar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)

# criando uma rota para renderizar a pagina
@app.route("/",methods=['GET'])
def pagina_inicial():
    return render_template("index.html")

@app.route("/animal",methods=['POST','GET'])
def mostrar_animal():
    return render_template('animal.html')


@app.route('/novoanimal', methods=['POST','GET'])
def inserir_animal():
    session_db = Session()  # Criar uma nova sessão
    nome_popular = request.form['nome_popular']
    nome_cientifico = request.form['nome_cientifico']
    habitos_noturnos = request.form['habitos_noturnos']
    animal = Animal(nome_popular=nome_popular,
                    nome_cientifico=nome_cientifico,
                    habitos_noturnos=habitos_noturnos) 
    try:
        session_db.add(animal)
        session_db.commit()
    except:
        session_db.rollback()
    finally:
        session_db.close()

    return redirect(url_for('pagina_inicial'))

@app.route('/avaliacao')
def mostrar_pagina():
    return render_template('avaliacao.html')

@app.route('/addavalia',methods=['POST','GET'])
def inserir_avaliacao():
    session_a = Session() # inicia a partida de futebol
    texto = request.form['texto']
    blob_pt = TextBlob(texto)
    polaridade = blob_pt.sentiment.polarity
    avaliacao = Avaliacao(texto=texto,polaridade=polaridade) #bola
    try:
       session_a.add(avaliacao) # passe 
       session_a.commit()  # gol
    except:
       session_a.rollback() #var cancela o gol
    finally:
       session_a.close() # encerramento da partida
    return redirect(url_for('listar_avalia'))


@app.route("/avaliazoo")
def avaliazoo():
    sessao_db = Session()
    avaliacoes = sessao_db.query(Avaliacao).all()
    return render_template('listavalia2.html',avaliacoes=avaliacoes)

@app.route("/listavalia")
def listar_avalia():
    session_db = Session()
    avaliacoes = session_db.query(Avaliacao).all()
     # Consulta todos os registros na tabela Nivel
    return render_template("listavalia2.html",avaliacoes=avaliacoes)

@app.route('/excluir_avalia/<int:id>', methods=['POST','GET'])
def excluir_avalia(id):
    session_db = Session()
    avaliacao = session_db.query(Avaliacao).filter_by(id=id).first()
    if avaliacao:
        try:
            session_db.delete(avaliacao)
            session_db.commit()
        except:
            session_db.rollback()
        finally:
            session_db.close()
    return redirect(url_for('listar_avalia'))


@app.route('/excluiravaliazoo/<int:id>',methods=['POST','GET'])
def excluir_avalia_zoo(id):
    # define uma sessao
    session_del = Session()
    avaliacao = session_del.query(Avaliacao).filter_by(id=id).first()
    if avaliacao:
        try:
            session_del.delete(avaliacao)
            session_del.commit()
        except:
            session_del.rollback()
        finally:
            session_del.close()
    return redirect(url_for('listar_avalia'))



# definindo com o programa principal 
if __name__ == "__main__":
    app.run(debug=True)



