import psycopg2
from config import config

def connect(query):

    params = config()
    conn = psycopg2.connect(**params)
    with conn:
        with conn.cursor() as cur:

            cur.execute(query)
            if "SELECT" in query:
                for line in cur.fetchall():
                    print line
        
def insert_values(table, columns, values):
    query = "INSERT INTO {0}{1} VALUES{2}".format(table, columns, values)

    connect(query)

def delete_values(table, column, value):
    query = "DELETE FROM {0} WHERE {1} = '{2}'".format(table, column, value)

    connect(query)

def update_values(table, column, value1, value2):
    temp1 = "{0} = '{1}'".format(column, value2)
    temp2 = "{0} = '{1}'".format(column, value1)

    query = "UPDATE {0} SET {1} WHERE {2}".format(table, temp1, temp2)

    connect(query)

def lookup_table(table):
    query = "SELECT * FROM {0}".format(table)
    
    connect(query)

