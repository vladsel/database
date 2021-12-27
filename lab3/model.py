from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, select, and_, DATETIME, exc
from sqlalchemy.orm import relationship
from config import Session, engine, base
import distutils.util

session = Session()


def connection():
    try:
        # base.metadata.drop_all(engine)
        base.metadata.create_all(engine)
        print("Successfully CONNECTED to database hotel")

    except (Exception, exc.DBAPIError) as _ex:
        print("Impossible to CONNECTED to database hotel\n", _ex)
        session.rollback()


class Category(base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True, nullable=False)
    room_type = Column(String(30), nullable=False)
    allocation_type = Column(String(30), nullable=False)
    eating_type = Column(Boolean, nullable=False)

    def __init__(self, room_type, allocation_type, eating_type, category_id=-1):
        self.room_type = room_type
        self.allocation_type = allocation_type
        self.eating_type = eating_type
        if category_id != -1:
            self.category_id = category_id

    def __repr__(self):
        return "{:^12}{:^15}{:^20}{:^15}".format(self.category_id, self.room_type, self.allocation_type, self.eating_type)

    def __str__(self):
        return f"{'category_id':^12}{'room_type':^15}{'allocation_type':^20}{'eating_type':^15}"
        # return f"""category_id = {self.category_id}, room_type = {self.room_type}, """ \
        #        f"""allocation_type = {self.allocation_type}, eating_type = {self.eating_type}"""


class Hotel(base):
    __tablename__ = 'hotel'
    hotel_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(20), nullable=False)
    restaurant = Column(Boolean, nullable=False)
    city = Column(String(25), nullable=False)
    star = Column(Integer, nullable=False)

    def __init__(self, name, restaurant, city, star, hotel_id=-1):
        self.name = name
        self.restaurant = restaurant
        self.city = city
        self.star = star
        if hotel_id != -1:
            self.hotel_id = hotel_id

    def __repr__(self):
        return "{:^10}{:^15}{:^10}{:^15}{:^5}".format(self.hotel_id, self.name, self.restaurant, self.city, self.star)

    def __str__(self):
        return f"{'hotel_id':^10}{'name':^15}{'restaurant':^10}{'city':^15}{'star':^5}"
        # return f"""hotel_id = {self.hotel_id}, name = {self.name}, """ \
        #        f"""restaurant = {self.restaurant}, city = {self.city}, star = {self.star}"""


class Chambermaid(base):
    __tablename__ = 'chambermaid'
    chambermaid_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    salary = Column(Integer, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)

    def __init__(self, name, phone_number, salary, hotel_id, chambermaid_id=-1):
        self.name = name
        self.phone_number = phone_number
        self.salary = salary
        self.hotel_id = hotel_id
        if chambermaid_id != -1:
            self.chambermaid_id = chambermaid_id

    def __repr__(self):
        return "{:^15}{:^15}{:^15}{:^8}{:^10}".format(self.chambermaid_id, self.name, self.phone_number, self.salary, self.hotel_id)

    def __str__(self):
        return f"{'chambermaid_id':^15}{'name':^15}{'phone_number':^15}{'salary':^8}{'hotel_id':^10}"
        # return f"""chambermaid_id = {self.chambermaid_id}, name = {self.name}, """ \
        #        f"""phone_number = {self.phone_number}, salary = {self.salary}, hotel_id = {self.hotel_id}"""


class Guest(base):
    __tablename__ = 'guest'
    guest_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    patronymic = Column(String(100), nullable=False)
    birthday = Column(DATETIME, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)

    def __init__(self, name, surname, patronymic, birthday, hotel_id, guest_id=-1):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birthday = birthday
        self.hotel_id = hotel_id
        if guest_id != -1:
            self.guest_id = guest_id

    def __repr__(self):
        return "{:^10}{:^15}{:^15}{:^15}\t{}{:^12}".format(self.guest_id, self.name, self.surname, self.patronymic, self.birthday, self.hotel_id)

    def __str__(self):
        return f"{'guest_id':^10}{'name':^15}{'surname':^15}{'patronymic':^15}{'birthday':^12}{'hotel_id':^10}"
        # return f"""guest_id = {self.guest_id}, name = {self.name}, surname {self.surname}, """ \
        #        f"""patronymic = {self.patronymic}, birthday = {self.birthday}, hotel_id = {self.hotel_id}"""


class Room(base):
    __tablename__ = 'room'
    room_id = Column(Integer, primary_key=True, nullable=False)
    arrival_date = Column(DATETIME, nullable=False)
    departure_date = Column(DATETIME, nullable=False)
    category_id = Column(Integer, ForeignKey('category.category_id'), nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotel.hotel_id'), nullable=False)
    number = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, arrival_date, departure_date, category_id, hotel_id, number, price, room_id=-1):
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.category_id = category_id
        self.hotel_id = hotel_id
        self.number = number
        self.price = price
        if room_id != -1:
            self.room_id = room_id

    def __repr__(self):
        return "{:^10}\t  {}\t\t{}{:^22}{:^6}{:^8}{:^10}".format(self.room_id, self.arrival_date, self.departure_date,
                                                            self.category_id, self.hotel_id, self.number, self.price)

    def __str__(self):
        return f"{'room_id':^10}{'arrival_date':^18}{'departure_date':^18}{'category_id':^15}{'hotel_id':^10}{'number':^8}{'price':^8}"
        # return f"""room_id = {self.room_id}, arrival_date = {self.arrival_date}, departure_date {self.departure_date}, """ \
        #        f"""category_id = {self.category_id}, hotel_id = {self.hotel_id}, hotel_id = {self.number}, price = {self.price}"""


class RoomChambermaid(base):
    __tablename__ = 'room/chambermaid'
    room_id = Column(Integer, ForeignKey('room.room_id'), primary_key=True, nullable=False)
    chambermaid_id = Column(Integer, ForeignKey('chambermaid.chambermaid_id'), primary_key=True, nullable=False)

    def __init__(self, room_id, chambermaid_id):
        self.room_id = room_id
        self.chambermaid_id = chambermaid_id

    def __repr__(self):
        return "{:^10}{:^18}".format(self.room_id, self.chambermaid_id)

    def __str__(self):
        return f"{'room_id':^10}{'chambermaid_id':^18}"
        # return f"""room_id = {self.room_id}, chambermaid_id = {self.chambermaid_id}"""


class RoomGuest(base):
    __tablename__ = 'room/guest'
    room_id = Column(Integer, ForeignKey('room.room_id'), primary_key=True, nullable=False)
    guest_id = Column(Integer, ForeignKey('guest.guest_id'), primary_key=True, nullable=False)

    def __init__(self, room_id, guest_id):
        self.room_id = room_id
        self.guest_id = guest_id

    def __repr__(self):
        return "{:^10}{:^10}".format(self.room_id, self.guest_id)

    def __str__(self):
        return f"{'room_id':^10}{'guest_id':^10}"
        # return f"""room_id = {self.room_id}, guest_id = {self.guest_id}"""


def insert(choice: int, data: list) -> bool:
    if len(data) < 2:
        return False
    elem = None
    try:
        match choice:
            case 1:
                elem = Category(*data)
            case 2:
                elem = Chambermaid(*data)
            case 3:
                elem = Guest(*data)
            case 4:
                elem = Hotel(*data)
            case 5:
                elem = Room(*data)
            case 6:
                elem = RoomChambermaid(*data)
            case 7:
                elem = RoomGuest(*data)
        session.add(elem)
        session.commit()
        print("Successfully INSERTED data into table:")
        print(elem)
        return True
    except (Exception, exc.DBAPIError) as _ex:
        print("Impossible to INSERT data into table\n", _ex)
        session.rollback()
        return False


def select_by_key(table: str, key_name: str, key_val: str) -> list:
    try:
        return session.query(eval(f"{table}")).filter(eval(f"{table}.{key_name}") == f"{key_val}").all()
    except (Exception, exc.DBAPIError) as _ex:
        print(f"Impossible to SELECT data from table {table} by key {key_name}\n", _ex)
        session.rollback()
        return []


def select_by_table(table: str, quantity: str = '100', offset: str = '0') -> list:
    try:
        if table == 'RoomGuest':
            return session.query(eval(f"{table}")).order_by(RoomGuest.room_id.asc()).offset(offset).limit(quantity).all()
        elif table == 'RoomChambermaid':
            return session.query(eval(f"{table}")).order_by(RoomChambermaid.room_id.asc()).offset(offset).limit(quantity).all()
        else:
            key_name = table[0].lower() + table[1:] + '_id'
            return session.query(eval(f"{table}")).order_by(eval(f"{table}.{key_name}").asc()).offset(offset).limit(quantity).all()
    except (Exception, exc.DBAPIError) as _ex:
        print(f"Impossible to SELECT data from table {table}", _ex)
        session.rollback()
        return []


def delete(table: str, key_name: str, key_val: str) -> bool:
    try:
        session.query(eval(f"{table}")).filter(eval(f"{table}.{key_name}") == f"{key_val}").delete()
        return True
    except (Exception, exc.DBAPIError) as _ex:
        print(f"Impossible to DELETE data from table {table}", _ex)
        session.rollback()
        return False


def update(choice: int, data: list, id1: int, id2: int = 0) -> bool:
    if len(data) < 2:
        return False
    try:
        match choice:
            case 1:
                session.query(Category).filter_by(category_id=f"{id1}").update(
                    {Category.room_type: data[0], Category.allocation_type: data[1],
                     Category.eating_type: distutils.util.strtobool(data[2])})
            case 2:
                session.query(Chambermaid).filter_by(chambermaid_id=f"{id1}").update(
                    {Chambermaid.name: data[0], Chambermaid.phone_number: data[1], Chambermaid.salary: data[2],
                     Chambermaid.hotel_id: data[3]})
            case 3:
                session.query(Guest).filter_by(guest_id=f"{id1}").update(
                    {Guest.name: data[0], Guest.surname: data[1], Guest.patronymic: data[2],
                     Guest.birthday: data[3], Guest.hotel_id: data[4]})
            case 4:
                session.query(Hotel).filter_by(hotel_id=f"{id1}").update(
                    {Hotel.name: data[0], Hotel.restaurant: distutils.util.strtobool(data[1]),
                     Hotel.city: data[2], Hotel.star: data[3]})
            case 5:
                session.query(Room).filter_by(room_id=f"{id1}").update(
                    {Room.arrival_date: data[0], Room.departure_date: data[1], Room.category_id: data[2],
                     Room.hotel_id: data[3], Room.number: data[4], Room.price: data[5]})
            case 6:
                session.query(RoomChambermaid).filter_by(room_id=f"{id1}", chambermaid_id=f"{id2}").update(
                    {RoomChambermaid.room_id: data[0], RoomChambermaid.chambermaid_id: data[1]})
            case 7:
                session.query(RoomGuest).filter_by(room_id=f"{id1}", guest_id=f"{id2}").update(
                    {RoomGuest.room_id: data[0], RoomGuest.guest_id: data[1]})
        session.commit()
        return True
    except Exception as _ex:
        print("Impossible to UPDATE data into table", _ex)
        return False
