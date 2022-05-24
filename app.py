from email.policy import default
import json
from msilib.schema import Class
from turtle import pos
from flask import Flask,render_template,request,redirect,jsonify,session
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import hashlib

from sqlalchemy import true
from app_crud import *
# UPLOAD_FOLDER = 'media\\profile'

app = Flask(__name__)
app.secret_key="abc"
app.config['UPLOAD_FOLDER'] = 'media\\profile'
app.config['UPLOAD_FOLDER_FOR_POST'] = 'media\\post'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/register",methods=['POST'])
def register():
    
    id=str(request.form['id'])
    first_name = str(request.form['first_name'])
    last_name = str(request.form['last_name'])
    email = str(request.form['email'])
    password1 = str(request.form['password'])
    profil_pic = request.files['profil_pic']
    filename = secure_filename(profil_pic.filename)
    password = hashlib.md5(password1.encode()).hexdigest()
    
    # isUsernameexist = User.query.filter_by(email=email)
    if Is_Author_Exist(email) == true:
        return jsonify('User Already Exist'),501
    else:
        print(type(id))
        profil_pic.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(profil_pic.filename)))
        new_user = Insert_Author(id,email,password,first_name,last_name,filename)   
        img = new_user["profile_pic"]
        str_img =os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(profil_pic.filename))
        new_user["profile_pic"]=str_img
        return jsonify(new_user)

@app.route("/login",methods=['POST'])
def login():
    if request.content_type == 'application/json':
        email = request.json['email']
        password1 = request.json['password']
        password = hashlib.md5(password1.encode()).hexdigest()
        # isUsernameexist = User.query.filter_by(email=email)
        if Is_Author_Exist(email) == true:
            user=Get_One_User_By_Email(email)
            if password == user["password"]:
                session['id']=user["id"]
                user.pop("password")
                print(session['id'])
                return jsonify(user),200
            else:
                return jsonify('Invalide Password'),401
        else:
            return jsonify('Invalide Email'),401

@app.route("/logout")
def logout():
    session.pop('id',None) 
    return jsonify('User Logout'),200

@app.route("/post/create",methods=['POST'])
def post_create():
    
    if 'id' in session:  
        author_id=session['id']
        id = request.form['id']
        title = request.form['title']
        description = request.form['description']
        post_pic1 = request.files['post_pic']
        post_pic = secure_filename(post_pic1.filename)
        new_post = Insert_Post(id,title,description,author_id,post_pic)
        post_pic1.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER_FOR_POST'],secure_filename(post_pic1.filename)))
        return jsonify(new_post),201
    else:
        return jsonify('User Not Login'),501
@app.route("/post/<id>",methods=['GET'])
def post(id):
    # try:
    post = Get_One_Post(id)
    img = post["post_pic"]
    str_img =os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER_FOR_POST'],str(img,'utf8'))
    post["post_pic"]=str_img
    if post != []:
        return jsonify(post),200
    else:
        return jsonify('ID Not Found'),404  

@app.route("/posts",methods=['GET'])
def posts():
    result = Get_all_Post()
    return jsonify(result),200


@app.route('/post/update/<id>', methods=['PUT'])
def update_post(id):
    post = Get_One_Post(id)
    if post != []:
        title = request.json['title']  
        description = request.json['description']
        result=Update_Post(id,title,description)
        return jsonify(result),200
    else:
         return jsonify('ID Not Found'),404
        
@app.route('/post/delete/<id>', methods=['DELETE'])
def delete_post(id):
    post = Get_One_Post(id)
    if post != []:
        Delete_Post(id)
        return jsonify('Post Deleted'),200
    else:
         return jsonify('ID Not Found'),404


@app.route("/profile/<id>",methods=['GET'])
def profile(id):
    user = Get_One_User(id)
    if user != []:
        img = user["profile_pic"]
        str_img =os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],str(img,'utf8'))
        user["profile_pic"]=str_img
        return jsonify(user),200
    else:
        return jsonify('ID Not Found'),404  


    

if __name__ == "__main__":
    app.run(debug=True,port=7000),

