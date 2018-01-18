# coding=utf-8
import sys
import pymysql
class TransferMoney(object):
    def __init__(self,conn):
        self.conn = conn
    def transfer(self,source_acctid,target_acctid,money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()

    def check_acct_available(self, acctid):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM account WHERE acctid = %s "%acctid
            cursor.execute(sql)
            print __name__+sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("account %s not exist"%acctid)
        finally:
            cursor.close()
    def has_enough_money(self, acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM account WHERE acctid = %s AND money>=%s"%(acctid,money)
            cursor.execute(sql)
            print __name__+sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("account %s not enough money"%acctid)
        finally:
            cursor.close()
    def reduce_money(self, acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "UPDATE account SET  money = money-%s WHERE acctid =%s"%(money,acctid)
            cursor.execute(sql)
            print __name__+sql
            if cursor.rowcount != 1:
                raise Exception("account reduce fail"%acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "UPDATE account SET  money = money+%s WHERE acctid =%s"%(money,acctid)
            cursor.execute(sql)
            print __name__+sql
            if cursor.rowcount != 1:
                raise Exception("account add fail"%acctid)
        finally:
            cursor.close()


if __name__=="__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='python_test',
        passwd='ersuan',
        charset='utf8'
    )
    tr_money = TransferMoney(conn)
    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print "error"+str(e)
    finally:
        conn.close()