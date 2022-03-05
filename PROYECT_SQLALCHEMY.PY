from xmlrpc.client import DateTime
from sqlalchemy import create_engine
from sqlalchemy import MetaData #objetos catalogo de tablas 
from sqlalchemy import Table, Column,Integer,String,DateTime #para crear objs de tipo tabla 
from datetime import datetime

#create_engine seria la conexion 
engine=create_engine('postgresql://postgres:postgres@127.0.0.1/pythonsql')
metadata=MetaData() #este objeto sirve de puente entre nuestra tabla y el gestor 

#users
users= Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),                 #nullable es q no admite nulos
    Column('username',String(), index=True, nullable=False),  #string es varchar ,index indica q la column esta indexada
    Column('email',String(), nullable=False),
    Column('created_at',DateTime(),default=datetime.now())                                                        

)

if __name__=='__main__':
    metadata.drop_all(engine)
    metadata.create_all(engine) #asi conecto las tablas con el gestor 

    with engine.connect() as connect:
        query_insert=users.insert().values(
            username='user1',
            email='user1@example.com'
        )
        connect.execute(query_insert)

    #print(users.c) #asi accedo a las columnas de la tabla (con el atributo c) 
    #print(users.c) si quisiera ver solo la columna id por ejemplo