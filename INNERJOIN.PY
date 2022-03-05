from xmlrpc.client import DateTime
from numpy import delete
from sqlalchemy import FLOAT, Float, ForeignKey, create_engine
from sqlalchemy import MetaData #objetos catalogo de tablas 
from sqlalchemy import Table, Column,Integer,String,DateTime,ForeignKey #para crear objs de tipo tabla 
from datetime import datetime
import json
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import desc, asc
from sqlalchemy import and_, or_, not_
from sqlalchemy import delete
#create_engine seria la conexion 
engine=create_engine('postgresql://postgres:postgres@127.0.0.1/pythonsql')
metadata=MetaData() #este objeto sirve de puente entre nuestra tabla y el gestor 

                                                     
orders=Table(
    'orders', #primer argunmento es el nombre de la tabla
    metadata, #seg argumento objeto de tipo metadata
    Column('id',Integer,primary_key=True)
)

products=Table(
    'products',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('title',String()),
    Column('price',Float(5,2)),
    #la relacion q establezco es 1 a muchos con orders , una orden puede poseer muchos productos 
    #y un producto le pertenece a una orden
    Column('order_id',ForeignKey('orders.id'))
)

if __name__=='__main__':
    

    #creo las tablas
    metadata.drop_all(engine)
    metadata.create_all(engine)

    with engine.connect() as connection:

        #orden  
        insert_query=orders.insert() #como esta tabla orders solo tiene una columna y 
                                     #justo es tmb la pk, no uso values()
        connection.execute(insert_query)

        #ahora creo los productos que se relacionan con la orden q cree arriba
        insert_query=products.insert().values(
            title='iphone',
            price=500.50,
            order_id=1
        )
        connection.execute(insert_query)

        insert_query=products.insert().values(
            title='ipad',
            price=800.00,
            order_id=1
        )
        connection.execute(insert_query)

        insert_query=products.insert().values(
            title='macbook',
            price=2000.00,
            order_id=1
        )
        connection.execute(insert_query)

        select_query=select(
            [
                products.c.title,
                products.c.price
            ]#metodo select_from obligatorio para cualq join
        ).select_from(
            orders.join(products) #join recibe como arg la tabla con la q queremos unir la consulta
        ).where(
            orders.c.id==1
        )

        result=connection.execute(select_query)
        for product in result.fetchall():
            print(product.title,product.price)

        #print(select_query)

        #print(orders.join(products))