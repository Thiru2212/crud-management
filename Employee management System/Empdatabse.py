#import Emp module


#database connectivity
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Employee",
    port=3306
)


def insert(admin_id,name,gender,contact_no,email,admin_password):
    curobj=con.cursor()
    curobj.execute("INSERT INTO admin VALUES(%s,%s,%s,%s,%s,%s)",(admin_id,name,gender,contact_no,email,admin_password))
    con.commit() 
def fetch():
    cursobj=con.cursor()
    cursobj.execute("SELECT * FROM admin")
    res=cursobj.fetchall()
    return res

def id_exist(admin_id):
    curobj = con.cursor()
    sql = "SELECT COUNT(admin_id) FROM admin WHERE admin_id=%s"
    val = (admin_id,)  # Ensure it's a tuple
    curobj.execute(sql, val)
    res = curobj.fetchone()
    curobj.close()  # Close the cursor
    return res[0] > 0

def update(admin_id,new_name,new_gender,new_contact_no,new_email,new_admin_password):
    curobj=con.cursor()
    sql="UPDATE admin SET name=%s,gender=%s,contact_no=%s,email=%s,admin_password=%s WHERE admin_id=%s"
    val=(new_name, new_gender, new_contact_no, new_email, new_admin_password, admin_id)
    curobj.execute(sql, val)
    con.commit()           
def delete(admin_id):
    curobj=con.cursor()
    sql="DELETE FROM admin WHERE admin_id=%s"
    val=(admin_id,)
    curobj.execute(sql, val)
    con.commit()

def search(option,value):
    curobj=con.cursor()
    query = f"SELECT * FROM admin WHERE {option} = %s"
    curobj.execute(query,(value,))
    res=curobj.fetchall()
    return res




    
    

