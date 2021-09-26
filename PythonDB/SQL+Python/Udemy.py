import MySQLdb

host = 'localhost'
user = 'Carlos'
password = '1475'
db = 'escola_udemy'
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where = None):
    global c
    
    query = 'SELECT ' + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where
    c.execute(query)
    return c.fetchall()





def insert(values, table, fields = None):
    global c, con
    query = "INSERT INTO " + table
    if(fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()


def update (sets, table, where = None):
    global c, con
    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if(where):
        query = query + " where " + where
    c.execute(query)
    con.commit()


def delete(table, where):
    global c, con
    query = "delete from " + table + " where " + where
    c.execute(query)
    con.commit()

    
#update({"Data_nasc":"2021-08-03"}, "alunos", "DRE = 5")


#values = ["DEFAULT, 'Kattya Victoria', '2000-08-25', 'Rua Nove', 'Magé', 'RJ', '03531707780'",
#          "DEFAULT, 'Julho Catnip', '2021-07-25', 'Rua Nove', 'Magé', 'RJ', '16909930060'"]

#insert(values, "alunos")

#delete("alunos", "DRE = 8")
#delete("alunos", "DRE = 9")

result = (select("*", "alunos"))

print(result)
