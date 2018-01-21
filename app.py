import sqlite3
from flask import Flask, render_template, request, g
from data import Articles,Books,Peoples
from verses import Verses

        
app = Flask(__name__)


Articles = Articles()
Books = Books()
Peoples = Peoples()
Verses = Verses()

@app.route("/")
def index():
  return render_template("home.html",value=[1,2])
  
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/videos')
def videos():
  return render_template('videos.html')


@app.route('/articles')
def articles():
  return render_template('articles.html',articles=Articles)

@app.route('/article/<string:id>/')
def article(id):
  return render_template('article.html',id=id,articles=Articles)

@app.route('/article/<string:id>/show/')
def show(id):
  return render_template('show.html',id=id,aricles=Articlesf)

@app.route('/books')
def books():
  return render_template('books.html',books=Books)

@app.route('/book/<string:BookID>/')
def book(BookID):
  return render_template('book.html',BookID=BookID,books=Books,verses=Verses)

@app.route('/peoples')
def peoples():
  return render_template('peoples.html',peoples=Peoples)

@app.route('/people/<string:PersonID>/')
def people(PersonID):
  return render_template('people.html',PersonID=PersonID,people=Peoples[int(PersonID)])


if __name__=='__main__':
  app.run()

  