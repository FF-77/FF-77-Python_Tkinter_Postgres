import psycopg2

con = psycopg2.connect(
                        user = 'postgres',
                        password = '123',
                        database = 'postgres',
                        port = 5432)


cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS login(
id serial not null,
nome varchar(50),
email varchar(30),
telefone varchar(15));
""")

print('Conectado.....')

