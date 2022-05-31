from models import Pessoas, Usuarios

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Leonardo', idade=33)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Arruda').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Leonardo').first()
    pessoa.nome = 'Arruda'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_usuario('Bruno', '1234')
    #insere_usuario('Alice', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #exclui_pessoa()
    #consulta_pessoas()
    #altera_pessoa()
