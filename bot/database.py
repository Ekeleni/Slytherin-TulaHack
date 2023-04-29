import psycopg2

conn = psycopg2.connect(user="postgres", password="artd2006st", host="127.0.0.1", port="5432")


def create_events_reg_base():
    curs = conn.cursor()
    curs.execute('''CREATE TABLE events_reg
                          (author_id INT NOT NULL,
                          event_id INT NOT NULL,
                          price INT,
                          user_id INT NOT NULL); ''')
    conn.commit()
    curs.close()


def create_events_base():
    curs = conn.cursor()
    curs.execute('''CREATE TABLE events 
    (author_id INT NOT NULL, event_id INT NOT NULL, event_name TEXT NOT NULL, event_text TEXT NOT NULl, date TEXT NOT NULl, price INT, adress TEXT NOT NULL);''')
    conn.commit()
    curs.close()


def get_new_event_id():
    curs = conn.cursor()
    curs.execute('''SELECT * from events''')
    res = curs.fetchall()
    curs.close()
    if not res:
        return 1
    else:
        return res[len(res) - 1][1] + 1


def get_events(date):
    curs = conn.cursor()
    result = list()
    for i in date:
        curs.execute('''SELECT * from events WHERE date=%s''', (i,))
        res = curs.fetchall()
        result.append(res)
    print(result)
    curs.close()


def add_event(author_id, event_name, event_text, price, address):
    curs = conn.cursor()
    curs.execute('''INSERT INTO events
                          (author_id, event_id, event_name, event_text, price, address)
                          VALUES
                          (%s, %s, %s, %s, %s, %s);''', (author_id, get_new_event_id(), event_name, event_text,
                                                         price, address))
    conn.commit()
    curs.close()


def search_user_into_events(user_id):
    curs = conn.cursor()
    curs.execute('''SELECT * from events_reg WHERE user_id=%s''', (user_id,))
    res = curs.fetchall()
    curs.close()
    return res


def add_user(author_id, event_id, price, user_id):
    curs = conn.cursor()
    curs.execute('''INSERT INTO events_reg
                          (author_id, event_id, price, user_id)
                          VALUES
                          (%s, %s, %s, %s, %s);''', (author_id, event_id, price, user_id))
    conn.commit()
    curs.close()

