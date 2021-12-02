import psycopg2
import time

cursor = None
connection = None


def connect():
    try:
        global cursor, connection
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            database="hotel_db",
            port="5432"
        )

        cursor = connection.cursor()

        print("Successfully CONNECTED to database hotel")

        # cursor.execute("SELECT version();")
        # print(f"Server version {cursor.fetchone()}")

    except Exception as _ex:
        print("Failed CONNECTION to database hotel", _ex)


def disconnect():
    try:
        cursor.close()
        connection.close()
        print("Successfully DISCONNECTED from database hotel")
    except Exception as _ex:
        print("Impossible to DISCONNECT from database hotel", _ex)


def insert(choice: int, data: list) -> bool:
    if connection is None or cursor is None:
        return False
    else:
        try:
            match choice:
                case 1:
                    cursor.execute(f"""INSERT INTO public.\"category\" (room_type, allocation_type, eating_type) \
                                    VALUES (\'{data[0]}\', \'{data[1]}\', {data[2]});""")
                case 2:
                    cursor.execute(f"""INSERT INTO public.\"chambermaid\" (name, phone_number, salary, hotel_id) \
                                    VALUES (\'{data[0]}\', \'{data[1]}\', {data[2]}, {data[3]});""")
                case 3:
                    cursor.execute(f"""INSERT INTO public.\"guest\" (name, surname, patronymic, birthday, hotel_id) \
                                    VALUES (\'{data[0]}\', \'{data[1]}\', \'{data[2]}\', \'{data[3]}\', {data[4]});""")
                case 4:
                    cursor.execute(f"""INSERT INTO public.\"hotel\" (name, restaurant, city, star) \
                                    VALUES (\'{data[0]}\', {data[1]}, \'{data[2]}\', {data[3]});""")
                case 5:
                    cursor.execute(f"""INSERT INTO public.\"room\"(arrival_date, departure_date, category_id, hotel_id,\
                     number,price) VALUES(\'{data[0]}\', \'{data[1]}\', {data[2]}, {data[3]}, {data[4]}, {data[5]});""")
                case 6:
                    cursor.execute(f"""INSERT INTO public.\"room/chambermaid\" (room_id, chambermaid_id) \
                                    VALUES ({data[0]}, {data[1]});""")
                case 7:
                    cursor.execute(f"""INSERT INTO public.\"room/guest\" (room_id, guest_id) \
                                    VALUES ({data[0]}, {data[1]});""")
            connection.commit()
        except Exception as _ex:
            print("Impossible to INSERT data into table", _ex)
            return False
    return True


def delete(table: str, key_name: str, key_val: str) -> bool:
    if connection is None or cursor is None:
        return False
    else:
        try:
            cursor.execute(f"""DELETE FROM public.\"{table}\" WHERE {key_name} = \'{key_val}\';""")
            connection.commit()
        except Exception as _ex:
            print(f"Impossible to DELETE data from table {table}", _ex)
            return False
    return True


def select_by_key(table: str, key_name: str, key_val: str) -> list:
    if connection is None or cursor is None:
        return []
    else:
        try:
            cursor.execute(f"""SELECT * FROM public.\"{table}\" WHERE {key_name} = \'{key_val}\';""")
        except Exception as _ex:
            print(f"Impossible to SELECT data from table {table} by key {key_name}", _ex)
            return []
    return cursor.fetchall()


def select_by_table(table: str, quantity: str = '100', offset: str = '0') -> list:
    if connection is None or cursor is None:
        return []
    else:
        try:
            if table == 'room/chambermaid' or table == 'room/guest':
                cursor.execute(f"""SELECT * FROM public.\"{table}\" ORDER BY {"room_id"} \
                                ASC limit {quantity} offset {offset};""")
            else:
                cursor.execute(f"""SELECT * FROM public.\"{table}\" ORDER BY {table + "_id"} \
                                ASC limit {quantity} offset {offset};""")
        except Exception as _ex:
            print(f"Impossible to SELECT data from table {table}", _ex)
            return []
    return cursor.fetchall()


def update(choice: int, data: list, id1: int, id2: int = 0) -> bool:
    if connection is None or cursor is None:
        return False
    else:
        try:
            match choice:
                case 1:
                    cursor.execute(f"""UPDATE public.\"category\" SET room_type = \'{data[0]}\', \
                    allocation_type = \'{data[1]}\', eating_type = {data[2]} WHERE category_id = {id1};""")
                case 2:
                    cursor.execute(f"""UPDATE public.\"chambermaid\" SET name = \'{data[0]}\', phone_number = \
                    \'{data[1]}\', salary = {data[2]}, hotel_id = {data[3]} WHERE chambermaid_id = {id1};""")
                case 3:
                    cursor.execute(f"""UPDATE public.\"guest\" SET name = \'{data[0]}\', surname = \'{data[1]}\', \
                    patronymic = \'{data[2]}\',birthday = \'{data[3]}\',hotel_id = {data[4]} WHERE guest_id = {id1};""")
                case 4:
                    cursor.execute(f"""UPDATE public.\"hotel\" SET name = \'{data[0]}\', restaurant = {data[1]}, \
                    city = \'{data[2]}\', star = {data[3]} WHERE hotel_id = {id1};""")
                case 5:
                    cursor.execute(f"""UPDATE public.\"room\" SET arrival_date = \'{data[0]}\', departure_date = \
                    \'{data[1]}\', category_id = {data[2]}, hotel_id = {data[3]}, number = {data[4]}, \
                    price = {data[5]} WHERE room_id = {id1};""")
                case 6:
                    cursor.execute(f"""UPDATE public.\"room/chambermaid\" SET room_id = {data[0]}, \
                    chambermaid_id = {data[1]} WHERE room_id = {id1} AND chambermaid_id = {id2};""")
                case 7:
                    cursor.execute(f"""UPDATE public.\"room/guest\" SET room_id = {data[0]}, \
                    guest_id = {data[1]} WHERE room_id = {id1} AND guest_id = {id2};""")
            connection.commit()
        except Exception as _ex:
            print("Impossible to UPDATE data into table", _ex)
            return False
    return True


def generate(choice: int, count: int) -> bool:
    if connection is None or cursor is None:
        return False
    try:
        for i in range(count):
            match choice:
                case 1:
                    cursor.execute(f"""INSERT INTO public.\"category\" (room_type, allocation_type, eating_type) \
                                    VALUES (substr(md5(random()::text), 0, 10), substr(md5(random()::text), 0, 10), \
                                            (round(random())::int)::boolean);""")
                case 2:
                    cursor.execute(f"""INSERT INTO public.\"chambermaid\" (name, phone_number, salary, hotel_id) \
                                    SELECT (substr(md5(random()::text), 0, 12)), \
                                        (substr(md5(random()::character varying(12)), 0, 12)), \
                                        (floor(random() * (25000 - 5000 + 1)) + 5000), \
                                        hotel_id FROM public."hotel" order by random() limit 1;""")
                case 3:
                    cursor.execute(f"""INSERT INTO public.\"guest\" (name, surname, patronymic, birthday, hotel_id) \
                                    SELECT substr(md5(random()::text), 0, 10), \
                                        substr(md5(random()::character varying(12)), 0, 12), \
                                        substr(md5((random() * 2)::text), 0, 14), \
                                        to_timestamp(-286782355 + random() * 3270071999), \
                                        hotel_id FROM public."hotel" order by random() limit 1;""")
                case 4:
                    cursor.execute(f"""INSERT INTO public.\"hotel\" (name, restaurant, city, star) \
                                    VALUES (substr(md5(random()::text), 0, 10), (round(random())::int)::boolean, \
                                        substr(md5(random()::text), 0, 8), (floor(random() * (5 - 1 + 1)) + 1));""")
                case 5:
                    cursor.execute(f"""INSERT INTO public.\"room\"(arrival_date, departure_date, number, price, \
                                    category_id, hotel_id) \
                                    SELECT NOW() + (random() * (NOW() - NOW() - '360 days')), \
                                        NOW() + (random() * (NOW() - NOW() + '360 days')), \
                                        floor(random() * (1000 - 10 + 1) + 10), random() * (50000 - 500 ) + 500, \
                                        category_id, hotel_id FROM public."category", public."hotel" \
                                        order by random() limit 1;""")
                case 6:
                    cursor.execute(f"""INSERT INTO public.\"room/chambermaid\" (room_id, chambermaid_id) \
                                    SELECT room_id, chambermaid_id FROM public."room", public."chambermaid" \
                                        order by random() limit 1;""")
                case 7:
                    cursor.execute(f"""INSERT INTO public.\"room/guest\" (room_id, guest_id) \
                                    SELECT room_id, guest_id FROM public."room", public."guest" \
                                        order by random() limit 1;""")
        connection.commit()
    except Exception as _ex:
        print("Impossible to GENERATE data to database hotel", _ex)
        return False
    return True


def search(tables: list[str], key: str, value: str) -> tuple:
    if connection is None or cursor is None:
        return ()
    try:
        request = f"""SELECT * FROM public.\"{tables[0]}\" as first INNER JOIN public.\"{tables[1]}\" as second on first.\"{key}\" = second.\"{key}\" WHERE {value}"""
        print(f"SQL request: {request}")
        start_time = time.time_ns()
        cursor.execute(request)
        rows = cursor.fetchall()
        run_time = time.time_ns() - start_time
    except Exception as _ex:
        print("Impossible to SEARCH data in database hotel", _ex)
        return ()
    return rows, run_time
