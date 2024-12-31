import pandas as pd

def query_to_dataframe(query_result):
    """Converte o resultado da consulta SQL em um DataFrame pandas"""
    data = [
        {"id": costumer.id, "name": costumer.name, "age": costumer.age, "card_number": costumer.card_number, "balance": costumer.balance, "status": costumer.status}
        for costumer in query_result
    ]

    return pd.DataFrame(data)

def costumers_finished(df):
    """Filtra os clientes finalizados"""
    return df[df['status'] == 'Finalizado']
