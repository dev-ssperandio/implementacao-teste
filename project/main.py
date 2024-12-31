from db import session
from db.models import Costumer
from data_processing import query_to_dataframe, costumers_finished


# Consulta ao banco de dados
costumers_query = session.query(Costumer).all()

# Convertendo para DataFrame
df = query_to_dataframe(costumers_query)

# Filtrando dados
df_finished = costumers_finished(df)

# Exibindo os resultados
print("\nDados originais: ")
print(df)

print("\nDados filtrados: ")
print(df_finished)
