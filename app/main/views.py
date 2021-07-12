from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from werkzeug.wrappers import response
from . import main
from .forms import EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import Role, User, Cart, Product
from ..decorators import admin_required
from flask import json
import os
import requests
from datetime import date
from flask import session


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.products'))
    return render_template('index.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)


@main.route('/products', methods=['GET', 'POST'])
@login_required
def products():
    products_json_path = os.getcwd() + "/app/static/products_data.json"
    with open(products_json_path, 'r') as json_file:
        data = json.load(json_file)
    return render_template('products.html', items = data)


@main.route('/item/<item_id>', methods=['GET', 'POST'])
@login_required
def item(item_id):
    products_json_path = os.getcwd() + "/app/static/products_data.json" 
    with open(products_json_path, 'r') as json_file:
        data = json.load(json_file)
    product = object
    for _product in data:
        if _product["id"] == int(item_id):
            product =  _product
    return render_template('product.html', item = product)


@main.route('/add_to_cart/<item_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(item_id):
    #_user = User.query.filter_by(id=current_user.id).first_or_404()
    if current_user.cart_id is None:
        current_user.cart_id = current_user.id
        db.session.add(current_user)
        db.session.commit()
    
    #add_to_cart_uri = "https://fakestoreapi.com/carts/" + str(current_user.id)

    products_json_path = os.getcwd() + "/app/static/products_data.json" 
    with open(products_json_path, 'r') as json_file:
        data = json.load(json_file)
    product = object
    for _product in data:
        if _product["id"] == int(item_id):
            product =  _product
            break
    
    #####_product1 = Product(product['id'], 1,product['price'])

    #Get all the products in the cart
    _cart = Cart(current_user.id,int(item_id),1,product["price"],product["tag"],product["title"])
    #_cartProd = Cart.query.filter_by(cart_id=current_user.id, product_id=int(item_id)).all()
    _cartProd = Cart.query.filter_by(cart_id=current_user.id, product_id=int(item_id)).first()

    # ###1
    # if _cartProd != []:
    #     if any(_cartProd) == _cart:
    #         for prod in _cartProd:
    #             if prod.product_id == int(item_id):
    #                 prod.quantity+=1
    #                 db.session.add(prod)
    #                 db.session.commit()
    #     else:
    #         db.session.add(_cart)
    #         db.session.commit()

    # # ###2
    # # if _cartProd != []:
    # #     for prod in _cartProd:
    # #         if prod.product_id == int(item_id):
    # #             prod.quantity+=1
    # #             db.session.add(prod)
    # #             db.session.commit()
    # #             break
    # #         else:
    # #             db.session.add(_cart)
    # #             db.session.commit()
    # #             break
    # # else:
    # #     db.session.add(_cart)
    # #     db.session.commit()

###3
    if _cartProd != None:
        _cartProd.quantity+=1
        _cartProd.image = _cart.image
        _cartProd.title = _cart.title
        db.session.add(_cartProd)
        db.session.commit()
    else:
        db.session.add(_cart)
        db.session.commit()


    flash('The product has been updated in the cart.')

    return redirect(url_for('.products'))


#TODO Remove common code used to read data from json and replace it here
def load_json():
    return ""

def get_request(data,uri):
    _data = json.jsonify(data)
    res = requests.get(uri, params=())
    print('response from server:',res.text)
    response = res.json()
    return response
    

def post_request(uri,data):
    #make a POST request
    _data = json.jsonify(data)
    res = requests.post(uri, json=_data)
    print('response from server:',res.text)
    response = res.json()
    return response



@main.route('/get_cart', methods=['GET'])
@login_required
def get_cart():
    _cart = Cart.query.filter_by(cart_id=current_user.id).all()
    _total = 0
    _totalcost = 0
    if _cart is not None:
        for _row in _cart:
            _total+=_row.quantity
            _totalcost = _totalcost + (_row.quantity*_row.price)

    return render_template('cart.html',items = _cart,total = _total, totalcost = _totalcost)
