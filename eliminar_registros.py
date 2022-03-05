from xmlrpc.client import DateTime
from sqlalchemy import FLOAT, create_engine
from sqlalchemy import MetaData #objetos catalogo de tablas 
from sqlalchemy import Table, Column,Integer,String,DateTime #para crear objs de tipo tabla 
from datetime import datetime
import json
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import desc, asc
from sqlalchemy import and_, or_, not_

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
        #Listar en consola en forma DESC el nombre de los 10 primeros usuario
        #cuyo genero sea F y posean por pais Portugal o Indonesia. 

        with open('MOCK_DATA.json') as file:
            
            connect.execute(users.insert(),json.load(file))
        
        delete_query=users.delete(users.c.id==1)
        print(delete_query)

        result=connect.execute(delete_query)
        print(result.rowcount)

        select_query=select([users.c.id,users.c.name]).where(users.c.id==2)
        result=connect.execute(select_query)
        user=result.fetchone()
        print(user)