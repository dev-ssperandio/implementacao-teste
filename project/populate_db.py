from db import engine, session
from db.models import Costumer, Base

def populate_database():
    """Popula o banco de dados com dados iniciais"""
    # Cria as tabelas no banco de dados se ainda não existirem
    Base.metadata.create_all(engine)

    # Lista de clientes para inserir
    costumers = [
            Costumer(name="Edelvita", age=17, card_number=12345678901, balance=-150.50, status="Finalizado"), 
            Costumer(name="Ivanessa", age=28, card_number=98765432102, balance=250.50, status="Pendente"), 
            Costumer(name="Sidney", age=20, card_number=12345678903, balance=3880.50, status="Finalizado"), 
            Costumer(name="Vita", age=17, card_number=98765432104, balance=-150.50, status="Pendente"), 
            Costumer(name="Iva", age=58, card_number=12345678905, balance=50.50, status="Finalizado"), 
            Costumer(name="BADI", age=68, card_number=98765432106, balance=-10.50, status="Pendente"),
        ]

    # Adiciona os dados na sessão
    session.add_all(costumers)
    # Salva as alterações
    session.commit()
    print("Dados inseridos com sucesso!")

# Chamar a função ao executar o script:
if __name__ == '__main__':
    populate_database()