import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `pomopy`;")
conn.commit()

criar_tabelas = '''
    SET NAMES utf8;
    CREATE DATABASE `pomopy`  DEFAULT CHARSET=utf8;
    USE `pomopy`;
    CREATE TABLE `users` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(60) NOT NULL,
      `username` varchar(20) NOT NULL,
      `password` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB;'''

conn.cursor().execute(criar_tabelas)
conn.commit()
conn.cursor.close()