from xmlrpc.client import DateTime
from sqlalchemy import FLOAT, create_engine
from sqlalchemy import MetaData #objetos catalogo de tablas 
from sqlalchemy import Table, Column,Integer,String,DateTime #para crear objs de tipo tabla 
from datetime import datetime
import json
from sqlalchemy import select
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
            
            '''select_query=select(
                [users.c.name]
            ).where(
                users.c.id==1  #puse 1 pq quiero solo el primer registro
            )'''
            select_query=select(
                [users.c.name]
            ).order_by(
                desc(users.c.id)  #quiero solo el ultimo usuario 
            ).limit(1)
                
            result=connect.execute(select_query)    
            
            user= result.fetchone() #one pq uno solo y por eso no uso for pq no hay iteracion es uno solo
            
            print(user) 