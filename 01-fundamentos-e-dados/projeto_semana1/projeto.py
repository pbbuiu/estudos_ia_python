import numpy as np
import pandas as pd
import datetime as dt
import sys

#Leitura dos arquivos com proteção de erros
try:
    itemsOrder_df = pd.read_csv("olist_order_items_dataset.csv", na_values=['', ' ', 'N/A', 'Null'], dtype='U')
    orders_df = pd.read_csv("olist_orders_dataset.csv", na_values=['', ' ', 'N/A', 'Null'], dtype='U')
    products_df = pd.read_csv("olist_products_dataset.csv", na_values=['', ' ', 'N/A', 'Null'], dtype='U')
except FileNotFoundError:
    time_now = dt.datetime.now()
    print("Erro: um ou mais arquivos não foram encontrados")
    try:
        with open("logs_erro_etl.txt", "a") as f:
            f.write(f"Data e Hora do erro: {time_now.strftime("%c")}\n")
    except:
        print("Algo deu errado ao tentar acessar o log de erros")
    sys.exit(1)

#Limpeza orders_df {

#Trabalhando apenas com pedidos com order_status 'delivered'
orders_df = orders_df.loc[orders_df['order_status'].str.contains('delivered')]

#Limpando dados NaN 
orders_df.dropna(inplace=True)

# }

#Limpeza products_df {

#Preenchendo produtos com categoria não informada
products_df['product_category_name'] = products_df['product_category_name'].fillna('categoria_nao_informada')

#Preenchendo restante dos dados não informados
products_df.fillna(0, inplace=True)

# }

#Transformando as datas em datetime
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'], format="%Y-%m-%d %H:%M:%S")
orders_df['order_approved_at'] = pd.to_datetime(orders_df['order_approved_at'], format="%Y-%m-%d %H:%M:%S")
orders_df['order_delivered_carrier_date'] = pd.to_datetime(orders_df['order_delivered_carrier_date'], format="%Y-%m-%d %H:%M:%S")
orders_df['order_delivered_customer_date'] = pd.to_datetime(orders_df['order_delivered_customer_date'], format="%Y-%m-%d %H:%M:%S")
orders_df['order_estimated_delivery_date'] = pd.to_datetime(orders_df['order_estimated_delivery_date'], format="%Y-%m-%d %H:%M:%S")

#Mesclando os Datas Frames com base no Id's dos produtos e os Id's dos pedidos
new_df = itemsOrder_df.merge(products_df, on='product_id')
new_df = new_df.merge(orders_df, on='order_id')

#Criando coluna com valor total frete+pedido
new_df['price'] = pd.to_numeric(new_df['price'], errors='coerce')
new_df['freight_value'] = pd.to_numeric(new_df['freight_value'], errors='coerce')
new_df['item_total_value'] = new_df['freight_value'] + new_df['price']

#Criando coluna com o tempo de entrega em dias
new_df['delevered_time'] = (new_df['order_delivered_customer_date'] - new_df['order_purchase_timestamp']).dt.days

#Criando coluna booleana com atraso True
new_df['delayed'] = new_df['order_delivered_customer_date'] > new_df['order_estimated_delivery_date']

#Criando coluna dos impostos
new_df['product_tax'] = new_df['product_category_name'].str.contains('beleza_saude|relogios_presentes')
new_df['product_tax'] = np.where(new_df['product_tax'] == True, new_df['item_total_value']/10,new_df['item_total_value']/20)

#Analise dos resultados 
total_result = new_df['item_total_value'].sum()
mean_freight = round(new_df['freight_value'].mean(), 2)

#Ordenando e separando os top 10 faturamentos por categoria
sort_revenue = new_df[['product_category_name', 'item_total_value']].groupby(['product_category_name']).agg(['sum', 'size', 'mean'])
sort_revenue.sort_values(by=('item_total_value', 'sum'), ascending=False, inplace=True)
top10_revenue = sort_revenue.head(10)

#Porcentagem de atrasos de pedidos por categoria
delayed = new_df[['product_category_name', 'delayed']].groupby(['product_category_name']).agg(['sum', 'mean', 'size'])

#Exportando top 10 faturamentos
top10_revenue.to_csv("relatorio_faturamento_top10.csv")

with open("resumo_executivo.txt", 'w') as f:
    f.write("Total de linhas da tabela unificada:")
    f.write(str(new_df['product_category_name'].count()))
    f.write("\n")
    f.write("Tempo medio de entregas em dias:")
    f.write(str(new_df['delevered_time'].mean()))
    f.write("\n")
    f.write("Faturamento liquido da empresa:")
    f.write(str(new_df['item_total_value'].sum()))
    f.write("\n")
# print(type(new_df['product_category_name'].count()))

# print(orders_df['order_delivered_carrier_date'].head())
# print(orders_df['order_delivered_carrier_date'].dtype)

# print(products_df.isna().sum())
# print(itemsOrder_df.isna().sum())
# print(orders_df.isna().sum())

# print(itemsOrder_df.info())
# print(itemsOrder_df.dtypes)
# print(itemsOrder_df.describe())
# print(itemsOrder_df.head())

# print(orders_df.info())
# print(orders_df.dtypes)
# print(orders_df.describe())
# print(orders_df.head())
# print(orders_df.isna().sum())

# print(products_df.info())
# print(products_df.dtypes)
# print(products_df.describe())
# print(products_df.head())
