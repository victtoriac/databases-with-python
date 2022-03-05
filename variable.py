import pymysql
import os

#drop_table_users="""DROP TABLE IF EXISTS users""" SI QUISIERA BORRARLA

users_table="""CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(50) NOT NULL, 
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

user=os.environ.get('user_mysql')
passwd=os.environ.get('password_mysql')
db=os.environ.get('db_mysql')
if __name__=='__main__':
    try:
        connect=pymysql.Connect(host='localhost',port=3306,user,passwd,db)

        cursor=connect.cursor() #metodo cursor retorna obj de tipo cursor
        #cursor.execute(drop_table_users) lo ejecutaria antes de crearla
        cursor.execute(users_table)


        
    
    except pymysql.err.OperationalError as err:
        print('no se pudo realizar la conexion')
        print(err)
    
    finally:
        cursor.close()
        connect.close()
        print('conexion finalizada ok')