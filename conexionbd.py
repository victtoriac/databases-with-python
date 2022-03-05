import pymysql




if __name__=='__main__':
    try:
        connect=pymysql.Connect(host='localhost',port=3306,user='root',passwd='totito99010.',db='pythondb')
        
        print('conexion OK')
    
    except pymysql.err.OperationalError as err:
        print('no se pudo realizar la conexion')
        print(err)
    
