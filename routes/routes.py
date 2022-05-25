from flask import Blueprint
from controller.controller import *

route = Blueprint('route', __name__)

route.route('/',methods=['GET'])(index)
route.route("/register",methods=['POST'])(register)#eroor
route.route("/login",methods=['POST'])(login)
route.route("/logout")(logout)
route.route("/post/create",methods=['POST'])(post_create)#error
route.route("/post/<int:id>",methods=['GET'])(post) 
route.route('/profile/<int:id>',methods=['GET'])(profile)
route.route("/posts",methods=['GET'])(posts)#imge not serilizr
route.route('/post/update/<int:id>', methods=['PUT'])(update_post)
route.route('/post/delete/<int:id>', methods=['DELETE'])(delete_post)




