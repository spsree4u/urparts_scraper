
import sqlite3

from scraper.config import DB_PATH


class DBUtil:

    def __init__(self):
        self.connection = sqlite3.connect(str(DB_PATH))

    def save_to_db(self, table_name, values, columns=None):
        if columns:
            col_string = tuple(columns)
        else:
            col_string = ''
        val_string = ','.join('?'*len(values))
        insert_sql = "INSERT INTO {0} {1} values({2})".format(
            table_name, col_string, val_string)
        print(insert_sql)
        self.connection.execute(insert_sql, values)
        self.connection.commit()

    def close_db_connection(self):
        self.connection.close()
