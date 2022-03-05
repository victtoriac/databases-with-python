from xmlrpc.client import DateTime
from sqlalchemy import FLOAT, create_engine
from sqlalchemy import MetaData #objetos catalogo de tablas 
from sqlalchemy import Table, Column,Integer,String,DateTime #para crear objs de tipo tabla 
from datetime import datetime
import json

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
        insert_query=users.insert()

        with open('MOCK_DATA.json') as file:
            users=json.load(file) #asi convierto el contenido json a un dic
            connect.execute(insert_query,users)
            #voy a insetar todos los usuarios asi:
            #for user in users:
             #   query=insert_query.values(**user) #** lo uso para q las llaves del dic se tomen como parametros
              #  connect.execute(query)


    