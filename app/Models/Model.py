# from flask_mysqldb import 
import MySQLdb

SQL_FIND = ''

class Model:
    def __init__(self) -> None:
        self.__db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="admin", db="pomopy", port=3306)
        self.__cursor = self.__db.cursor()
        self.query = ''
        self.lastExecutedQuery = ''
        self.table = ''
        self.primaryKey = 'id'
        self.fillable = []
        self.attributes = []

    def resetQuery(self) -> None:
        self.lastExecutedQuery = self.query
        self.query = ''

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
        self.resetQuery()
        result_set = self.__cursor.fetchall()
        for row in result_set:
            print(row)
        
        return self.__cursor.fetchall()
    
    def find(self, id):
        return self.select().where(self.primaryKey, id).get()
    
    def create(self, attributes):
        self.attributes = attributes        
        self.query = ' INSERT INTO {} ({}) VALUES ({})'.format(self.table, self.getColumns(), self.getValues())
        self.__cursor.execute(self.query)
        self.__db.commit()
        self.resetQuery()
        
        return self.find(self.__cursor.lastrowid)

    def getColumns(self):
        return ', '.join(self.attributes.keys())
    
    def getValues(self):
        values = '\', \''.join(self.attributes.values())
        values = "'" + values + "'"

        return values