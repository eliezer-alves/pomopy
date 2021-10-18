from six import string_types
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
        self.columnsSelect = self.fillable

    def resetQuery(self) -> None:
        self.lastExecutedQuery = self.query
        self.query = ''
    
    def getColumns(self):
        return ', '.join(self.attributes.keys())
    
    def getValues(self):
        values = '\', \''.join(self.attributes.values())
        values = "'" + values + "'"
        return values
    
    def getColumnsSelect(self, columns):
        if columns == None:
            self.columnsSelect = self.fillable        
            self.columnsSelect.append(self.primaryKey)

        elif isinstance(columns, list):
            self.columnsSelect = columns
        
        elif isinstance(columns, string_types):
            self.columnsSelect = columns.split(',')

        return self.columnsSelect

    def hydrateWithBaseData(self, baseData) -> None:
        self.attributes = []
        print(len(baseData), baseData)
        
        if len(baseData) == 1:
            self.attributes = dict(zip(self.columnsSelect, baseData[0]))
        
        else:
            for register in enumerate(baseData):
                self.attributes.append(dict(zip(self.columnsSelect, register)))

    def curdate(self):
        self.__cursor.execute("SELECT CURDATE();")
        return self.__cursor.fetchall()

    def select(self, columns = None):
        self.query += ' SELECT {} FROM {}'.format(', '.join(self.getColumnsSelect(columns)), self.table)
        return self
    
    def where(self, clause, value = None, operator = '='):
        if(value != None):
            self.query += ' WHERE {} {} \'{}\''.format(clause, operator, value)
        else:    
            self.query += ' WHERE {}'.format(clause)        
        return self

    def andWhere(self, clause, value = None, operator = '='):
        if(value != None):
            self.query += ' AND {} {} \'{}\''.format(clause, operator, value)
        else:    
            self.query += ' AND {}'.format(clause)        
        return self
    
    def get(self):
        self.__cursor.execute(self.query)
        self.resetQuery()
        result_set = self.__cursor.fetchall()
        self.hydrateWithBaseData(result_set)
        return self.attributes
    
    def find(self, id):
        return self.select().where(self.primaryKey, id).get()
    
    def create(self, attributes):
        self.attributes = attributes        
        self.query = ' INSERT INTO {} ({}) VALUES ({})'.format(self.table, self.getColumns(), self.getValues())
        self.__cursor.execute(self.query)
        self.__db.commit()
        self.resetQuery()
        return self.find(self.__cursor.lastrowid)