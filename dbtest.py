import psycopg2

try:
    conn = psycopg2.connect("dbname='demodb' user='postgres' host='localhost' password='coconut'")
except:
    print("I am unable to connect to the database")

with conn.cursor() as curs:

    try:
# simple single row system query
        curs.execute("SELECT * FROM public.haircutprices")

        # returns a single row as a tuple
        single_row = curs.fetchone()

        # use an f-string to print the single tuple returned
        print(f"{single_row}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
conn.close()