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

if __name__=='__main__':
    try:
        connect=pymysql.Connect(host='localhost',port=3306,user='root',passwd='totito99010.',db='pythondb')

        cursor=connect.cursor() #metodo cursor retorna obj de tipo cursor
        #cursor.execute(drop_table_users) lo ejecutaria antes de crearla
        #cursor.execute(users_table)

        query="INSERT INTO users(username,password,email) VALUES(%s,%s,%s)"
        values=('candela_gpg','password123','candela.vasquez@hotmail.com') 
        #los %s (placeholders) seran reemp por los values de abajo pq es para reutilizar codigo
        cursor.execute(query,values)
        connect.commit() #para confirmar los cambios
        
    
    except pymysql.err.OperationalError as err:
        print('no se pudo realizar la conexion')
        print(err)
    
    finally:
        cursor.close()
        connect.close()
        print('conexion finalizada ok')
