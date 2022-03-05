import psycopg2

drop_table_users="""DROP TABLE IF EXISTS users""" 

users_table="""CREATE TABLE users(
    id SERIAL, 
    username VARCHAR(50) NOT NULL, 
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

users=[
    ('user5','password','user5@hotmail.com'),
    ('user6','password','user6@hotmail.com'),
    ('user7','password','user7@hotmail.com'),
    ('user8','password','user8@hotmail.com')
    ]

if __name__=='__main__':
    try:
        connect=psycopg2.connect("dbname='pythondb' user='postgres' password='postgres' host='127.0.0.1'")

        with connect.cursor() as cursor:
            cursor.execute(drop_table_users)
            cursor.execute(users_table)
            query="INSERT INTO users(username,password,email) VALUES(%s,%s,%s)"
            cursor.executemany(query,users)
            connect.commit()

            query="DELETE FROM users WHERE id=%s"
            cursor.execute(query,(3,))
            connect.commit()

            query="SELECT * FROM users"
            cursor.execute(query)
            for user in cursor.fetchall():
                print(user)


    except psycopg2.OperationalError as err:
        print('no se pudo realizar la conexion')
        print(err)
    finally:
        cursor.close()
        connect.close()
        print('conexion finalizada ok')


