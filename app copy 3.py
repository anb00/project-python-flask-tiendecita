from flask import Flask, render_template,jsonify
import sqlite3
from flask import Flask, render_template , request, url_for, flash, redirect
from werkzeug.exceptions import abort
from markupsafe import escape
from flask import session
import secrets
#render de basics for show items

app = Flask(__name__)
app.config['SECRET_KEY'] = '@d#f€g¬h7er'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def get_db_connection():
    
    conn = sqlite3.connect('database-marketplace.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/hello/')
@app.route('/<category>')
def hello(category=None):
    print(category)
    a = category
    print(secrets.token_hex())
    conn = get_db_connection()
    # post = conn.execute('SELECT * FROM item i inner join category c on i.itemcatid = c.catid WHERE c.category_name = ?',
    #                     (category,)).fetchone()
    # post = conn.execute('SELECT i.itemId, c.catId FROM items i JOIN category c ON i.itemcatid = c.catid WHERE c.category_name =(?);',(category)).fetchall()['itemId']
    target_fish_name = category
    connection = sqlite3.connect("database-marketplace.db")
    cursor = connection.cursor()
    
    rows = cursor.execute("SELECT item.itemid,item.itemName,item.itemPrice,item.itemDescription,item.image_path,item.itemsellerid,category.catid,category.category_name,seller.sellerId,seller.sellerName from item inner join category on item.itemcatid = category.catid inner join seller on seller.sellerid = item.itemsellerid WHERE category.category_name = ?",(target_fish_name,),).fetchall()
    
    print(rows)
    
    data = {}
    data = rows
    if rows is not None:
     for x in rows:
        print(x)
    #return jsonify(rows)
    return render_template('test.html',  rows=rows,category=category,x=x,data=data)

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM item WHERE itemId = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/test')
def get_category_id(catId):
    category = request.args.get('catId')
    print(category)
    b = print(category)
    a = category
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM item i inner join category c on c.catId = i.itemcatId where c.catId = ?',
                        (catId,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return render_template('test.html', post = post)




@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/')
def index():
    category = request.args.get('category')
    print("category desde Index",category)
    # def category():
    #a = request.args.get['catId']
    #console.log(a)
    #print(a)
    conn = get_db_connection()
    cats = conn.execute('SELECT * FROM category').fetchall()
    # conn.close()
    # return render_template('index.html',cats=cats)
    # conn = get_db_connection()
    posts = conn.execute('SELECT * FROM item').fetchall()
    conn.close()
    return render_template('index.html', posts=posts,cats=cats)

@app.route('/hello/<category>')
def index2():
    # def category():
    #a = request.args.get['catId']
    #console.log(a)
    #print(a)
    conn = get_db_connection()
    cats = conn.execute('SELECT * FROM category').fetchall()
    # conn.close()
    # return render_template('index.html',cats=cats)
    # conn = get_db_connection()
    posts = conn.execute('SELECT * FROM item').fetchall()
    conn.close()
    return render_template('test.html', posts=posts,cats=cats)


@app.route('/index')
def access_param(category_name):
#  print(catId)
 category = request.args.get('category_name')
 print(category)
 b = print(category)
 a = category
 
 conn = get_db_connection()

 post = conn.execute("SELECT * FROM item i inner join category c on c.catid = i.itemcatId WHERE c.category_name='{{a}}'").fetchall()
 #cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 print("thisis thecategory:",a)
 for p in post :
    print(p)
 

 conn.close()
 if post is None:
     abort(404)
 return render_template('test.html', post = post)
#  print("esto es la categoria seleccionada",a) 
#  return '''<h1>The source value is: {}</h1>'''.format(category)




# @app.route('/index')
# def dw():
#  conn = get_db_connection()
# post = conn.execute('SELECT * FROM item i inner join category c WHERE catId = ? AND i.itemcatid = c.catId', (catId,)).fetchone()
# conn.close()
# if post is None:
#  abort(404)
#  return render_template('test.html', post = post)


# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     return render_template('create.html')


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO item (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

app.run()