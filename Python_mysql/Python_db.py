# coding=utf-8
import pymysql
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    db = 'python_test',
    passwd = 'ersuan',
    charset = 'utf8'
)
cursor = conn.cursor()
sql = r"SELECT * FROM users"                           #cursor.execute(r"CREATE TABLE P(id TINYINT UNSIGNED );")
sql_insert = r"INSERT INTO users(id,username) VALUES(null,concat('name',id)) "
sql_update = r"UPDATE users SET username = 'name91' WHERE id = 9"
sql_delete = r"DELETE FROM users WHERE id<3"
cursor.execute(sql)         #执行SQL语句
buffer = cursor.fetchall()  #获取剩余全部
for row in buffer:
    print " id = %d,name= %s"%row
try:
    cursor.execute(sql_insert)
    print "%d be change"%cursor.rowcount
    cursor.execute(sql_update)
    print "%d be change"%cursor.rowcount
    cursor.execute(sql_delete)
    print "%d be change"%cursor.rowcount
    conn.commit()  # 默认情况下 sql操作作为事物需要手动提交
except Exception as e:
    print e
    conn.rollback()#事件回滚


                                    # print cursor.rowcount
                                    # print cursor.fetchone()   #获取一行
                                    # print cursor.fetchmany(2)  #获取many行
                                    # buffer = cursor.fetchall()  #获取剩余全部
                                    # print buffer
                                    # print buffer[0]    #元组

conn.close()
cursor.close()

