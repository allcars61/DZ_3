from engine import db
from dz_3_6_1 import Publisher, Book, Shop, Stock, Sale


publisher_name = input("Введите имя издателя: ")
publisher = db.query(Publisher).filter(Publisher.name == publisher_name).first()

if publisher:
    sales = db.query(Book.title, Shop.name, Sale.price, Sale.date_sale).\
        join(Stock).join(Shop).join(Sale).\
        filter(Book.publisher_id == publisher.id).\
        order_by(Sale.date_sale.desc())

    for sale in sales:
        print(f"{sale[0]} | {sale[1]} | {sale[2]} | {sale[3]}")
else:
    print("Издатель не найден")