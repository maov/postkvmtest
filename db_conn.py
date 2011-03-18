#Remember to have pgsql/lib known to linker, change /etc/ld.conf ....if not


import psycopg2
import sys
import csv
try:
    reader = csv.reader(open('data/UN_nuclear_el.csv', 'rb'))

    for row in reader:
        if reader.line_num != 0 and len(row) == 6:
            print(len(row))

    conn = psycopg2.connect("dbname = 'db1' user = 'maov' host='localhost' password='bajaro22'")
    cur = conn.cursor()
    cur.execute("""SELECT count(*) FROM users""")
    
    rows = cur.fetchall()
    print("row count")
    for row in rows:
        print(" ", row[0])
        print("length: ", len(row)) 
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

