#!/usr/bin/python
import MySQLdb

# execute SQL query using execute() method.

def search(plate):
    db = MySQLdb.connect("localhost","root","hyehadesseong","parking_place")
    cursor=db.cursor()
    sql = "select id from register where license_place='%s';" % (plate)
    ok=0
    try:
   # Execute the SQL command
        cursor.execute(sql)
   # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for x in results:
            print(x[0])
        if len(results)!=0:
            ok=1
    except Exception as ex:
        print(ex)
        ok=0
    return ok
    db.close()
if __name__ == "__main__":
    #print search("TM56BMW")
