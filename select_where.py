from xmlrpc.client import DateTime
from sqlalchemy import FLOAT, create_engine
from sqlalchemy import MetaData #objetos catalogo de tablas 
from sqlalchemy import Table, Column,Integer,String,DateTime #para crear objs de tipo tabla 
from datetime import datetime
import json
from sqlalchemy import select

#create_engine seria la conexion 
engine=create_engine('postgresql://postgres:postgres@127.0.0.1/pythonsql')
metadata=MetaData() #este objeto sirve de puente entre nuestra tabla y el gestor 

#users
users= Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),                 #nullable es q no admite nulos
    Column('age',Integer),  #string es varchar ,index indica q la column esta indexada
    Column('country',String(50), nullable=False),
    Column('email',String(50),nullable=False),
    Column('gender',String(50), nullable=False),
    Column('name',String(50), nullable=False)                                                       

)

if __name__=='__main__':
    metadata.drop_all(engine)
    metadata.create_all(engine) #asi conecto las tablas con el gestor 

    with engine.connect() as connect:

        with open('MOCK_DATA.json') as file:
            
            connect.execute(users.insert(),json.load(file))
        
        # DOS FORMAS DE FILTRAR CON WHERE EL PAIS PORTUGAL:
        
        #1)
        #SELECT * FROM users WHERE country='Portugal;
        #select_query=users.select(users.c.country=='Portugal')

        #2) en este podemos especificar q columnas queremos obtener 
        #SELECT id,email,name FROM users WHERE country='Portugal'
        select_query=select([
            users.c.id,
            users.c.email,
            users.c.name
        ]).where(
            users.c.country=="Portugal"
        )
        
        print(select_query)

        result=connect.execute(select_query) #objeto de tipo result proxy
        for user in result.fetchall():
            #print(user) #rowproxy
            print(user.name) #imprimiria solo el listado de nombres por ej
            #como no indique age en el select_query entonces me da un error este print si pusiera user.age