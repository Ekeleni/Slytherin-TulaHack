import psycopg2

conn = psycopg2.connect(user="postgres", password="artd2006st", host="127.0.0.1", port="5432")


def create_events_reg_base():
    curs = conn.cursor()
    curs.execute('''CREATE TABLE events_reg
                          (author_id INT NOT NULL,
                          event_id TEXT NOT NULL,
                          price INT,
                          user_id INT NOT NULL); ''')
