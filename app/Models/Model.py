# from flask_mysqldb import 
import MySQLdb

SQL_FIND = ''

class Model:
    def __init__(self) -> None:
        self.__db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="admin", db="jogoteca", port=3306)
        self.__cursor = self.__db.cursor()
        self.query = ''
        self.table = ''
        self.fillable = []
        self.attributes = []

    def curdate(self):
        self.__cursor.execute("SELECT CURDATE();")
        return self.__cursor.fetchall()

    def select(self, columns = '*'):
        if isinstance(columns, list):
            columns = ', '.join(columns)                        
        self.query += ' SELECT {} FROM {}'.format(columns, self.table)

        return self
    
    def where(self, clause, value = None, operator = '='):
        if(value != None):
            self.query += ' WHERE {} {} {}'.format(clause, operator, value)
        else:    
            self.query += ' WHERE {}'.format(clause)
        
        return self
    
    def get(self):
        self.__cursor.execute(self.query)

        return self.__cursor.fetchall()
    
    def create(self, attributes):
        self.attributes = attributes        
        self.query = ' INSERT INTO {} ({}) VALUES ({})'.format(self.table, self.getColumns(), self.getValues())

    def getColumns(self):
        return ', '.join(self.attributes.keys())
    
    def getValues(self):
        values = '\', \''.join(self.attributes.values())
        values = "'" + values + "'"

        return values