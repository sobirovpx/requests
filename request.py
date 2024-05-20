import requests
import psycopg2


url = 'https://dummyjson.com/users/'

r = requests.get(url)

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='0060',
                        host='localhost',
                        port=5432)

create_table_users_query = """create table users(
        id serial primary key ,
        firstname varchar(55) ,
        lastname varchar(55) ,
        maidenname varchar(55) ,
        age int,
        gender varchar(55) ,
        email varchar(55) 
);"""

cur = conn.cursor()
cur.execute(create_table_users_query)
conn.commit()

insert_into_query = """insert into users (firstname, lastname, maidenname, age, gender, email)

    values (%s,%s,%s,%s,%s,%s);

"""

for user in r.json()['users']:
    cur.execute(insert_into_query, (
        user['firstName'], user['lastName'], user['maidenName'], user['age'], user['gender'],
        user['email']))
    conn.commit()
