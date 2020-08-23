import sqlite3

class History:
    def save_history(self, user, query):
        db = sqlite3.connect("google.db" )
        try:
            db.execute('insert into HISTORY values("%s", "%s")' %(user, query))
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        db.close()

    def get_history(self, user, query):
        db = sqlite3.connect("google.db")
        recent_searches = ""
        try:
            results=db.execute('select * from HISTORY where USER = "%s"' % user)
            for row in results:
                if query in row[1]:
                    recent_searches = recent_searches + "\n" + str(row[1])
            return recent_searches
        except Exception as e:
            print(e)
        db.close()