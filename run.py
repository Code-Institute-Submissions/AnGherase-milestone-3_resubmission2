from flask import Flask,render_template, request, redirect, url_for
from config import Config
from forms import CreateFilmForm, UpdateFilmForm, ConfirmDelete
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
import os
import urllib

app = Flask(__name__)
app.config['MONGO_DBNAME']= 'films'
username = urllib.parse.quote_plus('admin1')
password = urllib.parse.quote_plus('movies')
app.config["MONGO_URI"]= "mongodb+srv://admin1:movies@cluster0-xnfne.mongodb.net/films?retryWrites=true&w=majority"
app.config["SECRET_KEY"]= "hweiufhiwuehfuiwegfiwegf"
mongo=PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    """ This is for the main index page """
    hello="some message"
    # Collect all the films
    films=mongo.db.films.find()
    # send to template
    return render_template("index.html",films=films, message=hello)

@app.route('/create_film', methods=['GET', 'POST'])
def create_film():
    """ this function handles the adding of films """
    form = CreateFilmForm(request.form)
    # check if form validates successsfully and insert it to mongo db
    if form.validate_on_submit():
        movies = mongo.db.films
        movies.insert_one({
            'title': request.form['title'],
            'description': request.form['description'],
            'director': request.form['director'],
            'image': request.form['image'],
            'genre': request.form['genre']
        })
        # redirect back to index - film was added successfully
        return redirect(url_for('index'))
    # send form to template
    return render_template('addfilm.html', form=form)

@app.route('/update_film/<film_id>', methods=['GET', 'POST'])
def update_film(film_id):
    """ this function handles teh updating of a film """
    film_db = mongo.db.films.find_one_or_404({'_id': ObjectId(film_id)})
    # if this is a GET request grab form and send to to template
    if request.method == 'GET':
        form = UpdateFilmForm(data=film_db)
        return render_template('updatefilm.html', film=film_db, form=form)
    form = UpdateFilmForm(request.form)
    # check if form validates
    if form.validate_on_submit():
        films_db = mongo.db.films
        # update this film
        films_db.update_one({
            '_id': ObjectId(film_id),
        }, {
            '$set': {
                'title': request.form['title'],
                'description': request.form['description'],
                'image': request.form['image'],
                'director': request.form['director'],
                'genre': request.form['genre'],
            }
        })
        # film successfully updated redirect to index
        return redirect(url_for('index'))
    # send form to template 
    return render_template('updatefilm.html', film=film_db, form=form)

@app.route('/delete_film/<film_id>', methods=['GET', 'POST'])
def delete_film(film_id):
    # get the film object
    film_db = mongo.db.films.find_one_or_404({'_id': ObjectId(film_id)})
    if request.method == 'GET':
        form = ConfirmDelete(data=film_db)
        # send film to delete template
        return render_template('deletefilm.html', title="Delete film", form=form)

    # get the form
    form = ConfirmDelete(request.form)
    # check form validates corrrectly
    if form.validate_on_submit():
        films_db = mongo.db.films
        films_db.delete_one({
            '_id': ObjectId(film_id),
        })
        #  film successfully deleted redirect to index
        return redirect(url_for('index'))
    # send film to delete template
    return render_template('deletefilm.html', film=film_db, form=form)

app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=True)
