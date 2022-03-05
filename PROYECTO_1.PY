from email.policy import default
import psycopg2
import os


DROP_USERS_TABLE="""DROP TABLE IF EXISTS users"""

USERS_TABLE="""CREATE TABLE users(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    
    
    )"""

def system_clear(function):
    def wrapper(connect,cursor):


        os.system("cls") #es para limpiar la terminal, el parametro para windows es cls y en mac clear
        function(connect,cursor)

        input("") #el usuario presiona enter 
        os.system("cls") #vuelvo a limpiar la consola
        
    
    wrapper.__doc__=function.__doc__
    return wrapper
@system_clear

def create_user(connect,cursor):
    """A) crear usuario"""

    username=input("ingrese un username: ")
    email=input("ingrese mail: ")

    query="INSERT INTO users(username,email) VALUES(%s,%s)"
    values=(username,email)
    cursor.execute(query,values)
    connect.commit()

    print("usuario creado con exito")
@system_clear

def list_users(connect,cursor):
    """B) listar usuarios"""
    query="SELECT id,username,email FROM users"
    cursor.execute(query)

    for id,username,email in cursor.fetchall():
        print(id,'-',username,'-',email)

    print("Listado de usuarios")

def user_exists(function):
    def wrapper(connect,cursor):
        id=input("ingrese id del usuario que se actualizara: ")
        query="SELECT id FROM users WHERE id=%s"
        cursor.execute(query,(id,))
        user=cursor.fetchone() #none
        if user:
            function(id,connect,cursor)
        else:
            print("ID INEXISTENTE")
    wrapper.__doc__=function.__doc__
    return wrapper 

@system_clear 
@user_exists



def update_user(id,connect,cursor):
    """C) actualizar usuario"""
    
    username=input("ingrese un nuevo username: ")
    email=input("ingrese nuevo mail: ")

    query="UPDATE users SET username=%s, email=%s WHERE id=%s"
    values=(username,email,id)
    cursor.execute(query,values)
    connect.commit()
        
    print("usuario actualizado con exito!")

@system_clear 
@user_exists  

def delete_user(id,connect,cursor):
    """D) eliminar usuario"""
    
    
    query="DELETE FROM users WHERE id=%s"
    cursor.execute(query,(id,))
    connect.commit()
    print("usuario eliminado con exito!")
    
@system_clear 
@user_exists 

   

def default(*args):
    print("OPCION INVALIDA!!!")

if __name__=='__main__':
    options={
        'a': create_user,
        'b': list_users,
        'c': update_user,
        'd': delete_user
    }
    try:
        connect=psycopg2.connect("postgresql://postgres:postgres@127.0.0.1/project_pythondb")

        with connect.cursor() as cursor:
            #cursor.execute(DROP_USERS_TABLE)
            #cursor.execute(USERS_TABLE)
            connect.commit()

            while True:
                for function in options.values(): #asi imprimo uno por uno los valores del dict
                    print(function.__doc__) #imprimo por cada iteracion la documentacion 
                print("scape para salir")

                option=input("seleccione opcion valida: ").lower()

                if option=="scape" or option=="s":
                    break 
                
                function=options.get(option,default)
                function(connect,cursor)


        connect.close()

    except psycopg2.OperationalError as err:
        print('No se pudo realizar la conexion')
        print(err)
