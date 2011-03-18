#Remember to have pgsql/lib known to linker, change /etc/ld.conf ....if not


import psycopg2
import sys
import csv
try:
    reader = csv.reader(open('un/elec_nuclear.csv', 'rb'))



    conn = psycopg2.connect("dbname = 'db1' user = 'maov' host='localhost' password='bajaro22'")
    cur = conn.cursor()

    for row in reader:
        if reader.line_num == 0:
              continue
        elif len(row) == 6:
            print("called alot")
            cur.execute("INSERT INTO nuclear VALUES(%s, %s, %s, %s, %s, %s)", row)
        conn.commit()
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

