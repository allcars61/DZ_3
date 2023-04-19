from sqlalchemy.orm import sessionmaker, joinedload
from engine import engine
from dz_3_6_1 import Publisher, Book, Shop, Stock, Sale

Session = sessionmaker(bind=engine)
db = Session()

def get_shops(name_or_id):
    query = (
        db.query(
            Book.title,
            Shop.name,
            Sale.price,
            Sale.date_sale
        )
        .join(Stock)
        .join(Shop)
        .join(Sale)
        .join(Book.publisher)
        .options(joinedload(Stock.book))
        .options(joinedload(Book.publisher))
        .filter(
            or_(
                Book.publisher_id == name_or_id,
                Publisher.name == name_or_id
            )
        )
    )
    items = query.all()
    if not items:
        print("Не найдено издательство с таким именем или идентификатором")
        return []

    return [(title, shop_name, price, date_sale.strftime('%d-%m-%Y')) for title, shop_name, price, date_sale in items]

if __name__ == '__main__':
    name_or_id = input("Введите имя или идентификатор издателя: ")
    shops = get_shops(name_or_id)
    for title, shop_name, price, date_sale in shops:
        print(f"{title: <40} | {shop_name: <20} | {price: <8} | {date_sale}")