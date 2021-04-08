import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def sql_query(db, query):
    with sqlite3.connect(db) as connect:
        cursor = connect.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        return result


engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class Competition(Base):
    __tablename__ = 'Competition_a'
    competition_id = Column(Integer, primary_key=True)
    competition_name = Column(String)
    world_record = Column(Integer)
    set_date = Column(Date)

    def __init__(self, competition_name, world_record, set_date):
        self.competition_name = competition_name
        self.world_record = world_record
        self.set_date = set_date


if __name__ == '__main__':

    db = 'lesson_16.db'

    # query_1 = 'CREATE TABLE competition (competition_id INTEGER, ' \
    #                                   'competition_name VARCHAR(30), ' \
    #                                   'world_record VARCHAR(30), ' \
    #                                   'set_date DATE);'
    # sql_query(db, query_1)
    #
    # query_2 = 'CREATE TABLE result (competition_id INTEGER, ' \
    #                              'sportsman_id INTEGER, ' \
    #                              'result INTEGER, ' \
    #                              'city VARCHAR(30), ' \
    #                              'hold_date DATE);'
    # sql_query(db, query_2)
    #
    # query_3 = 'CREATE TABLE sportsman (sportsman_id INTEGER, ' \
    #                                 'sportsman_name VARCHAR(30), ' \
    #                                 'rank INTEGER, ' \
    #                                 'personal_record INTEGER, ' \
    #                                 'country VARCHAR(30), ' \
    #                                 'year_of_birth DATE);'
    # sql_query(db, query_3)

    # query_4 = "INSERT INTO competition (competition_id, competition_name, world_record, set_date) VALUES " \
    #                                  "(1, 'Berlin Cup', 1500, '1990-02-01')" \
    #                                  "(2, 'Moscow Cup', 1400, '1995-03-15')," \
    #                                  "(3, 'Madrid Cup', 1350, '2000-11-21')," \
    #                                  "(4, 'Paris Cup', 1450, '1997-07-07')," \
    #                                  "(5, 'Milan Cup', 1200, '1985-08-28');"
    # sql_query(db, query_5)

    # query_6 = "INSERT INTO sportsman (sportsman_id, sportsman_name, rank, year_of_birth, personal_record, country)" \
    #         "VALUES ( 1, 'Janko Kaimanovic', 1, '1990-01-25', '1522', 'Croatia' )," \
    #         "( 2, 'Felipe Rodriguez', 1, '1985-11-25', '1596', 'Brazil' ), " \
    #         "( 3, 'Viktor Seleznev', 3, '1992-08-11', '1459', 'Russia' ), " \
    #         "( 4, 'Lewis Hilton', 3, '1987-06-04', '1158', 'England' ), " \
    #         "( 5, 'Frank de Jorux', 2, '1991-12-08', '1396', 'France' );"
    # sql_query(db, query_6)

    # query_7 = "INSERT INTO result (competition_id, sportsman_id, result, city, hold_date)" \
    #         "VALUES ( 1, 1, 1356, 'Berlin', '2020-07-25' )," \
    #                 "( 1, 4, 1248, 'Berlin', '2020-07-25' )," \
    #                 "( 1, 5, 1234, 'Berlin', '2020-07-25' )," \
    #                 "( 1, 3, 1189, 'Berlin', '2020-07-25' )," \
    #                 "( 1, 2, 1174, 'Berlin', '2020-07-25' )," \
    #                 "( 2, 3, 1356, 'Moscow', '2020-07-30' )," \
    #                 "( 2, 2, 1248, 'Moscow', '2020-07-30' )," \
    #                 "( 2, 1, 1234, 'Moscow', '2020-07-30' )," \
    #                 "( 2, 5, 1189, 'Moscow', '2020-07-30' )," \
    #                 "( 2, 4, 1174, 'Moscow', '2020-07-30' );"
    # sql_query(db, query_7)

    # query_8 = 'SELECT * FROM sportsman'
    # query_out_1 = sql_query(db, query_8)
    # print(query_out_1)
    #
    # query_9 = 'SELECT competition_name, world_record FROM competition ORDER BY world_record DESC'
    # query_out_2 = sql_query(db, query_9)
    # print(query_out_2)
    #
    # query_10 = "SELECT sportsman_name, year_of_birth FROM sportsman WHERE year_of_birth > '1989-12-31' AND year_of_birth < '1991-01-01'"
    # query_out_3 = sql_query(db, query_10)
    # print(query_out_3)
    #
    # query_11 = "SELECT city, result FROM result WHERE hold_date = '2010-05-12' AND hold_date = '2010-05-15'"
    # query_out_4 = sql_query(db, query_11)
    # print(query_out_4)
    #
    # query_12 = "SELECT city, result FROM result WHERE city = 'Moscow' AND result = 1248"
    # query_out_5 = sql_query(db, query_12)
    # print(query_out_5)
    #
    # query_13 = "SELECT sportsman_name, personal_record FROM sportsman WHERE personal_record < 1500"
    # query_out_6 = sql_query(db, query_13)
    # print(query_out_6)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    record_1 = Competition("Berlin Cup", 1500, "1990-02-01")
    # record_2 = Competition("Moscow Cup", 1400, "1990-02-01")
    # record_3 = Competition('Madrid Cup', 1350, '1990-02-01')
    # record_4 = Competition('Paris Cup', 1450, '1990-02-01')
    # record_5 = Competition('Milan Cup', 1200, '1990-02-01')
    session.add(record_1)
    # session.add(record_2)
    # session.add(record_3)
    # session.add(record_4)
    # session.add(record_5)

    record = session.query(Competition).all()
    print(record)