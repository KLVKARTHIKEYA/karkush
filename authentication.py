import sqlite3
def check_credentials(username,password):
    connect = sqlite3.connect("cred.db")
    try:
        cursr = connect.cursor()
        cursr.execute("select password from cred where username=?",(username,))
        password_data = cursr.fetchone()
        if password == password_data[0]:
            return True
        else:
            return False
    except Exception as e:
        return e
if __name__ == "__main__":
    op = check_credentials("test","test")
    print(op)
