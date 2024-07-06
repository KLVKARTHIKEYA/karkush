import sqlite3
from datetime import datetime
def get_expenses(time=None):
    if time == None:
        mega_str="{"
        connect = sqlite3.connect("prod.db")
        cursr = connect.cursor()
        cursr.execute("select * from expenses")
        data = cursr.fetchall()
        for row in data:
            return_string = f"id:{row[0]},date:{row[1]},note:{row[2]},amount:{row[3]}"
            mega_str+=return_string+","
        return mega_str[:len(mega_str)-1]+"}"
    elif time == "daily":
        date = datetime.today().strftime('%Y%m%d')
        mega_str="{"
        connect = sqlite3.connect("prod.db")
        cursr = connect.cursor()
        cursr.execute("select * from expenses where date = ?",(date,))
        data = cursr.fetchall()
        for row in data:
            return_string = f"id:{row[0]},date:{row[1]},note:{row[2]},amount:{row[3]}"
            mega_str+=return_string+","
        return mega_str[:len(mega_str)-1]+"}"
    elif time == "month":
        mega_str="{"
        year="2024"
        month = datetime.today().strftime("%m")
        start_date=year+month+"01"
        stop_date=year+month+"31"
        connect = sqlite3.connect("prod.db")
        cursr = connect.cursor()
        cursr.execute("select *  from expenses where date between ? and ?;",(start_date,stop_date,))
        data = cursr.fetchall()
        for row in data:
            return_string = f"id:{row[0]},date:{row[1]},note:{row[2]},amount:{row[3]}"
            mega_str+=return_string+","
        return mega_str[:len(mega_str)-1]+"}"
if __name__ == "__main__":
    print(get_expenses("month"))
