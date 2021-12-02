Лабораторна робота №2. Створення додатку бази даних, орієнтованого на взаємодію з СУБД PostgreSQL. Опис структури БД.

У Обраній базі даних «Готель» можна виділити наступні таблиці: загальні відомості про готель (hotel), тип заданого номера (room), категорія номера (category), загальні відомості про постояльця (guest), інформація про покоївку (chambermaid), відношення покоївок до кімнат (room/chambermaid),  відношення постояльців до кімнат (room/guest).
Стовпці заданих таблиць:
1.	hotel: hotel_id, name, restaurant, city, stars.
2.	room: room_id, arrival date, departure date, category_id, hotel_id, number.
3.	category: category_id, room type, allocation type, eating type, price.
4.	guest: guest_id, name, surname, patronymic, birthday, hotel_id.
5.	chambermaid: chambermaid_id, name, phone number, salary, hotel_id.
