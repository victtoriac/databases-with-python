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

        #asi solo actualizo el nombre del de id=1    
        #update_query=users.update(users.c.id==1).values(
        #    name='cambio de nombre!'
        #)   

        update_query=update(users).values(
            name='Nuevo cambio de nombre 2.0'

        ).where(
            users.c.id==200
        )
        print(update_query)
        #esta funcion (update()) recibe como parametro la tabla q queremos modificar y nos retorna
        #la sentencia sql necesaria para actualizar registros, values() lo uso para aclarar los nuevos
        #valores de las columnas. 
        result=connect.execute(update_query)
        print(
            result.rowcount #asi se cuantos registros fueron actualizados
        )      
            