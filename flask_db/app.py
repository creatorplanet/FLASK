# flask --app app --debug run  
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
 
# create the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:{PASSWORD}@localhost:5432/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model): 
    __tablename__ = "total"
    key = db.Column(db.String())
    edition = db.Column(db.String())
    revised = db.Column(db.String())
    classification = db.Column(db.String())
    title = db.Column(db.String() , primary_key=True)
    explain = db.Column(db.String())
    author = db.Column(db.String())
    publisher = db.Column(db.String())
    date = db.Column(db.String())
    url = db.Column(db.String())
    img = db.Column(db.String())
    isbn = db.Column(db.String())
    price = db.Column(db.String())
    r_rated = db.Column(db.String())
    overview = db.Column(db.String())
    category = db.Column(db.String())
    category_1 = db.Column(db.String())
    category_2 = db.Column(db.String())
    category_3 = db.Column(db.String())
    category_4 = db.Column(db.String())
    category_5  = db.Column(db.String())
    bool  = db.Column(db.Boolean)
    bool_1  = db.Column(db.String())
    id = db.Column(db.Integer, primary_key=True)  
    def __repr__(self):
        return f'Item {self.id}'   
 
@app.route("/", methods=['GET', 'POST'])
def home(): 
    if request.method == 'POST':   
        list_book = request.form.getlist("mycheckbox")  
        print(len(list_book)) 
        list_delete = request.form.getlist("deletebox")
        print(len(list_delete))
        for i in range(len(list_book)): 
            book = Book.query.filter_by(id=request.form.getlist('mycheckbox')[i]).first()
            book.bool_1 = 'True'
            db.session.commit() 
 
        for i in range(len(list_delete)): 
            book = Book.query.filter_by(id=request.form.getlist('deletebox')[i]).first()
            book.bool_1 = 'False'
            db.session.commit() 
        return redirect(url_for("home"))   
    #list_books = Book.query.all()
    #list_books = db.session.query(Book).filter_by(bool=None) 
    #list_books = Book.query.order_by(Book.key).limit(12000).all()
    # SELECT bool, COUNT(*) FROM total GROUP BY bool
    list_books = Book.query.order_by(Book.title).all()
    return render_template('index.html', list_books=list_books) 


 
@app.route("/false/<string:book_id>")
def update(book_id): 
    book = Book.query.filter_by(id=book_id).first()
    book.bool = False
    db.session.commit()
    return redirect(url_for("home")) 

@app.route("/true/<int:book_id>")
def true(book_id): 
    book = Book.query.filter_by(id=book_id).first()
    book.bool = True
    db.session.commit()
    return redirect(url_for("home")) 
  
if __name__ == "__main__":
    app.run(debug=True)    