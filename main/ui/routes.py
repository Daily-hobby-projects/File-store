from flask import Blueprint,request,render_template,redirect,url_for
from ..models.images import Image
from ..extensions.database import db


app_bp=Blueprint('app',__name__,template_folder='./templates')


@app_bp.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app_bp.route('/files')
def show_files():
    return render_template('files.html')