import psycopg2

db_name = 'n47'
password = '0060'
host = 'localhost'
port = 5432
user = 'postgres'

conn = psycopg2.connect(dbname=db_name,
                        user=user,
                        password=password,
                        host=host,
                        port=port)


cur = conn.cursor()
# select_data_query = "select * from person;"
# cur.execute(select_data_query)
#
#
# cur.execute(select_data_query)
# persons = cur.fetchall()
# print(persons)
# rows = cur.fetchall()
# print(rows)

select_data = "select * from developer;"
cur.execute(select_data)
data = cur.fetchall()
for row in data:
    data_premium = {'developer_id': row[0],'name':row[1],'surname':row[2],'team':row[3],'programming_language':row[4],'experience_year':row[5],'salary':row[6]}
    print(data_premium)