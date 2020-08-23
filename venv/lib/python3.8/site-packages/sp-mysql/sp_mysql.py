import getpass
import pymysql as m
my__cursor = None
mydb=None

def connection():
    
    def info():
        h = input('Enter the host :')
        un = input('Enter the username :')
        psw=getpass.getpass('enter the password :')
        dbn=input('Enter the database name :')
        return h,un,psw,dbn
    
    def check_connection():
        h,un,psw,dbn=info()
        try:
            global my__cursor,mydb #=mycursor
            mydb=m.connect(host =h,user =un ,password=psw)
            mycursor = mydb.cursor()
            #global my__cursor #=mycursor
            my__cursor = mycursor
        except:
            print('Invalid host or username or password enter a valid Credentials')
        return mycursor,dbn,h,un,psw
        
    try:
        try:
            mycursor,dbn,h,un,psw = check_connection()
      
            mycursor.execute("show databases;")
            data = mycursor.fetchall()

            a=[]
            for i in data:
                a.append(i[0])
 

            if dbn in a:
                mydb=m.connect(host =h,user =un,password=psw,db=dbn)
                mycursor.execute("USE "+dbn+" ;")
                print('\n')

            else:    
                mycursor.execute('CREATE database '+dbn+' ;' )
                mydb=m.connect(host =h,user =un,password=psw,db=dbn)
                mycursor.execute("USE "+dbn+" ;")
                print("New database is created by the name "+dbn+'.\n')
                my__cursor=mycursor
            return mycursor
        except:
            pass
    except:
        return mycursor

#droping of a table
    
    
def drop_db():
    try:
        if my__cursor!=None:
            a=my__cursor
            mycursor=a
            mycursor.execute("show databases;")
            data = mycursor.fetchall()
            a=[]
            for i in data:
                a.append(i[0])
            drop_dbname = input("Enter the database name which has to be droped :")
            if drop_dbname in a:
                mycursor.execute("drop database "+drop_dbname+' ;')
                mycursor.execute("show databases;")
                a= mycursor.fetchall()
                print("Database named "+ drop_dbname +" is droped sucessfully.\n")
        
            else:
                print("There is no such database named "+ drop_dbname+'.\n')
    except:
        pass
        
        
        
        
        
# show the database of the user        
        
def show_db():
    try:
        if my__cursor!=None:
            a=my__cursor
            a.execute('show databases;')
            b=a.fetchall()
            print("Databases:")
            for i in b:
                print(i[0])
            print("\n")
    except:
        pass
    
    
    
#to create a table

def cre_table():
    try:
        if my__cursor!=None:
            try:
                a=my__cursor
                mycursor=a
                tb_name = input("Enter the table name that has to be created :")
                n = int(input("Enter the number of columns :"))
                q="CREATE TABLE "+tb_name+'('
                x=''
                for i in range(n):
                    h=input("Enter the details of the column :")
                    if i==n-1:
                         x+=h+' '
                    else:    
                        x+=h+' , '
                x=x+");"    
                mycursor.execute(q+x)
                mycursor.execute("commit;")
                print("New table is created with the name "+tb_name)
            except:
                print("Invalid!!!!")
    except:
        pass
#to drop a table    
def drop_table():
    try:
        if my__cursor!=None:
            try:
                tab=input("Enter the table name to be dropped:")
                my__cursor.execute("drop table " +tab+" ;")
                data=my__cursor.fetchall()
                print("Table is dropped.")
            except:
                print("Table doesn't exist.")
    except:
        pass
 #to show the table   
    
def show_table():
    try:
        if my__cursor!=None:
            a=my__cursor
            a.execute("show tables;")
            b=a.fetchall()
            if len(b)==0:
                print("There is no table.")
            else:    
                print("Tables :")
                for i in b:
                    print(i[0])
    except:
        pass
        
        
def execute(s):
    try:
        my__cursor.execute(s)
        my__cursor.execute("commit;")
    except:
        pass
    
    
def autocommit(b):
    try:
        mydb.autocommit(b)
    except:
        pass
    
    
def get_host_info():
    try:
        mydb.get_host_info()
    except:
        pass
    
def fetchall():
    try:
        my__cursor.fetchall()
    except:
        pass
    
    
def fetchone():
    try:
        my__cursor.fetchone()
    except:
        pass
    
def close():
    try:
        my__cursor.close()
    except:
        pass
    

    
