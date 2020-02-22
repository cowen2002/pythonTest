' my sqlite test module'
'''这是我测试sqlite3的代码'''
__author__ = 'kuang wei'
import sqlite3
def test():
    conn = sqlite3.connect('testSqlite3.db')
    cursor = conn.cursor()
   # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    cursor.close()
    conn.commit()
    conn.close()
    
def docheck():
    conn = sqlite3.connect('testSqlite3.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where id = ?', ('1',))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()
    
    
if __name__ == '__main__':    
    # test()
    docheck()