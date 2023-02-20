import pandas as pd
import sqlite3

#Import data_1 csv and aggregate product count into product_quantity column
data_1_url = 'https://raw.githubusercontent.com/Ay-slim/forage-walmart-task-4/main/data/shipping_data_1.csv'
shipment_id_and_product_df = pd.read_csv(data_1_url)
shipment_id_and_product_df['product_quantity'] = shipment_id_and_product_df.groupby('shipment_identifier')['product'].transform('count')
unique_shipment_and_product_df = shipment_id_and_product_df.drop_duplicates()

data_2_url = 'https://raw.githubusercontent.com/Ay-slim/forage-walmart-task-4/main/data/shipping_data_2.csv'
warehouse_and_driver_df = pd.read_csv(data_2_url)

#Merge data_2 with processed data_1 data to align it with data_0 format
merged_shipment_and_warehouse_data = unique_shipment_and_product_df.merge(warehouse_and_driver_df, on='shipment_identifier').drop('shipment_identifier', axis='columns')

data_0_url = 'https://raw.githubusercontent.com/Ay-slim/forage-walmart-task-4/main/data/shipping_data_0.csv'
prepped_shipment_and_warehouse_data = pd.read_csv(data_0_url)

#Concatenate processed data_1 and data_2 with data_0
db_data = pd.concat([merged_shipment_and_warehouse_data, prepped_shipment_and_warehouse_data], axis=0)

#Insert into sqlite DB and read to confirm insertion
conn = sqlite3.connect('walmartdb')
conn.execute("CREATE TABLE shipments(origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier)")
db_data.to_sql('shipments', conn, if_exists='replace', index=False)
conn.commit()
cur = conn.cursor()
res = cur.execute("SELECT * FROM shipments")
res.fetchall()
conn.close()