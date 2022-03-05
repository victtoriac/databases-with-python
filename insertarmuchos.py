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

users=[
    ('user1','password','user1@hotmail.com'),
    ('user2','password','user2@hotmail.com'),
    ('user3','password','user3@hotmail.com'),
    ('user4','password','user4@hotmail.com')
    ]

if __name__=='__main__':
    try:
        connect=pymysql.Connect(host='localhost',port=3306,user='root',passwd='totito99010.',db='pythondb')

        cursor=connect.cursor() #metodo cursor retorna obj de tipo cursor
        #cursor.execute(drop_table_users) lo ejecutaria antes de crearla
        #cursor.execute(users_table)

        query="INSERT INTO users(username,password,email) VALUES(%s,%s,%s)"
        
        for user in users:
            cursor.execute(query,user)
        
        connect.commit() #para confirmar los cambios
        
    
    except pymysql.err.OperationalError as err:
        print('no se pudo realizar la conexion')
        print(err)
    
    finally:
        cursor.close()
        connect.close()
        print('conexion finalizada ok')