import pymysql 



#drop_table_users="""DROP TABLE IF EXISTS users""" SI QUISIERA BORRARLA

'''users_table="""CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(50) NOT NULL, 
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
'''

'''users=[
    ('user5','password','user5@hotmail.com'),
    ('user6','password','user6@hotmail.com'),
    ('user7','password','user7@hotmail.com'),
    ('user8','password','user8@hotmail.com')
    ]'''

if __name__=='__main__':
    try:
        connect=pymysql.Connect(host='localhost',port=3306,user='root',passwd='totito99010.',db='pythondb')

        cursor=connect.cursor() #metodo cursor retorna obj de tipo cursor
        #cursor.execute(drop_table_users) lo ejecutaria antes de crearla
        #cursor.execute(users_table)

        #query="INSERT INTO users(username,password,email) VALUES(%s,%s,%s)"
        
        #for user in users:
            #cursor.execute(query,user)
        #cursor.executemany(query,users)

        #connect.commit() #para confirmar los cambios
        query="DELETE FROM users WHERE id=%s"
        cursor.execute(query,(5,)) #borro el id numero 5
        connect.commit() #INSERT, UPDATE O DELETE LLEVAN COMMIT 
    
    except pymysql.err.OperationalError as err:
        print('no se pudo realizar la conexion')
        print(err)
    
    finally:
        cursor.close()
        connect.close()
        print('conexion finalizada ok')