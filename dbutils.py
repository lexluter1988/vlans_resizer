import psycopg2
import psycopg2.extras


class Dbutils(object):
    def __init__(self, connection=None):
        self.connection = connection

    def clean_up(self):
        try:
            connection = psycopg2.connect("dbname='im' user='postgres'")
            cur = connection.cursor()
            cur.execute("""INSERT INTO vlans(label,customer_id,version) values('VLAN for customer666','1287565','1')""")
            connection.commit()
            cur.close()
            connection.close()

        except psycopg2.Error as e:
            print e.pgerror
            return 1
        print "I am connected"
        return connection

    def get_all_customer(self):
        try:
            connection = psycopg2.connect("dbname='im' user='postgres'",
                                          connection_factory=psycopg2.extras.RealDictConnection)
            cur = connection.cursor()
            cur.execute("""SELECT * FROM ve WHERE customer_id = 1
                        """)
            rows = cur.fetchall()
            cur.close()
            connection.close()
            return rows
        except psycopg2.Error as e:
            print e.pgerror
            return 1

    def test(self):
        print "Tested"