from unittest import result
from .dbconection import *
from io import BytesIO

# cursor.execute("select version()")

def Insert_Author(id,email,password,first_name,last_name,profile_pic):
    sql = "INSERT INTO author(id,email,password,first_name,last_name,profile_pic)values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(id,email,password,first_name,last_name,profile_pic))
    conn.commit()
    conn.close()
    print("Data Inserted")
    meta=["id","email","password","first_name","last_name","profile_pic"]
    author=[id,email,password,first_name,last_name,profile_pic]
    data = dict(zip(meta,author))
    data.pop("password")
    return data


def Is_Author_Exist(email):
    sql = "SELECT * FROM author WHERE email='%s'"
    cursor.execute(sql%email)
    result = cursor.fetchall()
    if result!=[]:
        return True
    else:
        return False


def Update_Author(id,email,password,first_name,last_name):
    sql = "UPDATE author SET email= %s,password= %s,first_name= %s,last_name= %s WHERE id=%s"
    cursor.execute(sql,(email,password,first_name,last_name,id))
    conn.commit()
    conn.close()
    print("Data MOdify")

def Delete_Author(id):
    sql = "Delete from author WHERE id=%s"
    cursor.execute(sql,(id))
    conn.commit()
    conn.close()
    print("Data Deleted")

def Get_all_User():
    sql = "SELECT * FROM author"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)
    conn.close()
    
def Get_One_User(id):
    sql = "SELECT * FROM author WHERE id=%s"
    cursor.execute(sql%id)
    result = cursor.fetchall()
    meta=["id","email","password","first_name","last_name","profile_pic"]
    data=dict(zip(meta,result[0]))
    data.pop("password")
    return data


def Get_One_User_By_Email(email):
    sql = "SELECT * FROM author WHERE email='%s'"
    cursor.execute(sql%email)
    result = cursor.fetchall()
    meta=["id","email","password","first_name","last_name"]
    data=dict(zip(meta,result[0]))
    return data


def Insert_Post(id,title,description,author_id,post_pic):
    sql = "INSERT INTO post(id,title,description,author_id,post_pic)values(%s,%s,%s,%s,%s)"
    cursor.execute(sql,(id,title,description,author_id,post_pic))
    result = [id,title,description,author_id,post_pic]
    meta=["id","title","description","author_id,post_pic"]
    data=dict(zip(meta,result))
    conn.commit()
    return data
    
def Update_Post(id,title,description):
    sql = "UPDATE post SET title= %s,description= %s WHERE id=%s"
    cursor.execute(sql,(title,description,id))
    conn.commit()
    print("Post MOdify")
    result = [id,title,description]
    meta=["id","title","description",]
    data=dict(zip(meta,result))
    return data

def Delete_Post(id):
    sql = "Delete from post WHERE id=%s"
    cursor.execute(sql%id)
    conn.commit()
    conn.close()
    print("Post Deleted")

def Get_all_Post():
    sql = "SELECT * FROM post"
    cursor.execute(sql)
    result = cursor.fetchall()
    # meta=["id","title","description","author_id"]
    # data=dict(zip(meta,result[0]))
    return result
    
def Get_One_Post(id):
    sql = "SELECT * FROM post WHERE id=%s"
    cursor.execute(sql%id)
    result = cursor.fetchall()
    meta=["id","title","description","author_id","post_pic"]
    data=dict(zip(meta,result[0]))
    # img=result[0][4]
    # str_img = "media\\profile\\"
    # str_img= str_img+str(img,'utf8')
    # data["post_pic"]=str_img
    print(data)
    return data





