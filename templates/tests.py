

import unittest

import re



from flask_pymongo import PyMongo



import app as app_module



app = app_module.app



# Setting up test DB on Mongo and switching CSRF checks off

app.config["TESTING"] = True

app.config["WTF_CSRF_ENABLED"] = False

app.config['MONGO_URI'] = 'mongodb://localhost:27017/rMyFilmsTesting'



mongo = PyMongo(app)

app_module.mongo = mongo





class AppTestCase(unittest.TestCase):

    """Clean the DB"""

    def setUp(self):

        self.client = app.test_client()

        with app.app_context():

            mongo.db.users.delete_many({})

            mongo.db.recipes.delete_many({})





class AppTests(AppTestCase):

    """Test Home page loading"""

    def test_index(self):

        res = self.client.get('/')

        data = res.data.decode('utf-8')

        assert res.status == '200 OK'

        assert 'My Films in data



    def test_films(self):

        """Test recipe list page loading"""

        res = self.client.get('/films')

        data = res.data.decode('utf-8')

        assert res.status == '200 OK'

        assert 'features' in data



    def test_register_mismatch_passwords(self):

        """Check mismatched passwords on the registration form, expecting mismatch message"""

        res = self.client.post('/register', data=dict(

            username='max',

            password='joijqwdoijqwoid',

            password2='qoijwdoiqwjdoiqwd',

            email='max@aol.com',

        ))

        data = res.data.decode('utf-8')

        assert 'Passwords must match' in data



    def test_register_duplicate_username(self):

        """Check entering a username that is already used returns username is already taken message"""

        res = self.client.post('/register', follow_redirects=True, data=dict(

            username='max',

            password='fastfood',

            password2='fastfood',

            email='max@aol.com',

        ))

        data = res.data.decode('utf-8')

        assert 'MyFilms' in data

        res = self.client.post('/register', follow_redirects=True, data=dict(

            username='max',

            password='fastfood',

            password2='fastfood',

            email='max@aol.com',

        ))

        data = res.data.decode('utf-8')

        assert res.status == '200 OK'

        assert 'that username is already taken' in data



    def test_register_successful(self):

        """Check valid registration redirects to index page"""

        res = self.client.post('/register', follow_redirects=True, data=dict(

            username='lorena',

            password='sugarfree',

            password2='sugarfree',

            email='lorena@aol.com',

        ))

        data = res.data.decode('utf-8')

        assert res.status == '200 OK'

        assert 'MyFilms' in data





class LoggedInTests(AppTestCase):

    """Separate class to clean DB with no cross referencing"""

    def setUp(self):

        """

        Clean the DB, add new user and recipe and check user and new recipe

        shows on home after redirect

        """

        super().setUp()

        res = self.client.post('/register', follow_redirects=True, data=dict(

            username='Roxy',

            password='glutenfree',

            password2='glutenfree',

            email='roxy4@aol.com',

        ))

        res = self.client.post('/create_film', follow_redirects=True, data={

            'title': 'Vertigo',

            'image': 'https://ichef.bbci.co.uk/food/ic/food_16x9_1600/recipes/spaghettiallacarbona_86763_16x9.jpg',

            'description': 'Polizist John `Scottie' Ferguson leidet an Höhenangst. Eigentlich möchte er deswegen seine Arbeit aufgeben, als der Gavin Elster ihn bittet, seine Frau Madeleine ',

            'director': 'Alfred Hitchcock',

            'genre': 'thriller',
        })

        data = res.data.decode('utf-8')

        assert 'roxy' in data

        assert 'Vertigo'


    def test_edit_film(self):

        """Edit film and check redirect to home page"""

        res = self.client.get('/films')

        ids = re.findall(r'href="/fim/(\w+)"', res.data.decode("utf8"))

        assert len(ids) > 0

        res = self.client.get('/edit_film/{}'.format(ids[0]))

        data = res.data.decode('utf-8')

        assert res.status == '200 OK'

        assert 'Vertigo' in data

        res = self.client.post('/edit_recipe/'.format(ids[0]), follow_redirects=True, data={

            'title': 'Vertigo',

            'image': 'https://ichef.bbci.co.uk/food/ic/food_16x9_1600/recipes/spaghettiallacarbona_86763_16x9.jpg',

            'description': 'Polizist John `Scottie' Ferguson leidet an Höhenangst. Eigentlich möchte er deswegen seine Arbeit aufgeben, als der Gavin Elster ihn bittet, seine Frau Madeleine zu beschatten. Diese scheint ',

            'director': 'Alfred Hitchcock',

            'genre': 'thriller',

        })

        assert res.status == '200 OK'

