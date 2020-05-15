# Milestone 3 - My Films Project

#What does it do and what does it fulfill?/#UX

This project uses skills to build a Flask website that uses a MongoDB backend. The purpose of creating it was for 
the users to view films and create, update and delete films. Users can also search for films that contain the searched 
word in its tags, title or description. The project can be viewed at: 
https://5000-f92ac333-e2f4-4356-b046-e5e1c9cfbca1.ws-eu01.gitpod.io/

#Functionality of project/Existing features, features left to implement

The website is fully responsive and uses MongoDBfor the users and films collection. The user is able to register, 
login and view films. Logged in users are able to create, update (edit) and delete their own films. Any user can search 
for films using the search box. A user can also log out. The Films page shows all films in order of the amount of views 
each film has. The pagination of the films is done by the database. Each film on the films page can be clicked onto and 
that will load the single films page which shows the entire entry. If the user created/added the film on this page, they 
will not be able to edit and delete this film. The add film allows the logged in user to create a film and enter it onto 
the database. Other functionalities left to implement are a community tab for all the users of the site.

#Technologies used 

I used the following languages, frameworks, libraries to construct this project. 

HTML5-used for structuring and presenting the content

CSS/Bootstrap 4-used for the presentation of the web page, including the colours, layouts and fonts

JavaScript-used for creating the web page

Mongo- make uses of collections and documents

Flask- used for building an application like a web page

Heroku-used to deploy, manage and scale the app

jQuery-used to make it easier to use JavaScript on the website

#Deployment
This section describes the process I went through to deploy the project to a hosting platform (Heroku). The website 
was created in PyCharm, a local Git directory was used for version control and then uploaded to Github. A MongoDB 
database was used and set up inside Heroku. The details of the database connection are found inside the requirements.txt 
-it uses the os class environ method to point to its own config available (MongoDB_URI) in order to keep the production 
database connection string secret. There were no differences between the deployed version and the development version.

#Testing
By testing I checked that all the user stories from the UX section worked as intended, with the project providing an 
easy and straightforward way for the users to achieve their goals. My tests checked the page loading, as well as the 
business logic of the views. The testing process can be described via scenarios, following the model used for the Contact 
form: Go to the "Contact Us" page 
Try to submit the empty form and verify that an error message about the required fields appears 
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.

I tested for mismatched passwords, duplicated names, as well as the validation of succesful registration. The login page
is tested throughout my tests as a number of my test operations require a logged in user. The Create Film page was tested
by checking that a film was entered, the page redirects and the new film is featured on the index page. The Films page
 is tested by searching for any films on the films page, getting its ID number and going to that Films details page and 
changing some data and committing it. This then redirects the user to the Index page and that is tested that the 
information has changed on that film. The Delete Films page is tested by going to its films details page and deleting 
it, then checking that the redirect has happened and that the film does not appear on the index page. It is impossible 
to cover everything in testing, but the majority of elements was tested. My focus was on keeping the design usable and 
simple to navigate. As the site is built with responsive design, it works for mobile devices and I have checked it on
iphones 6 to x, Smsung galaxy, ipads (mini to pro), Google's pixel 2 and 3. I also tested it on several browsers 
 (Chrome, Explorer, Edge).

