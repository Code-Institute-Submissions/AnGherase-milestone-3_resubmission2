# Milestone 3 - Data centric-My Films

#What does it do and what does it fulfill?

This project uses skills to build a Flask website that uses a MongoDB backend. The purpose of creating this platform was for 
the users to view films and create, update and delete films. Users can also search for films that contain the searched 
word in its tags, title or description. So in essence My Films is a website created to give users access and full control over films.  The platform features amazing colours and pictures from films. The project can be viewed at: 
https://5000-f92ac333-e2f4-4356-b046-e5e1c9cfbca1.ws-eu01.gitpod.io/

#UX

Project purpose

The goal of MyFilms is to give users full access and control over all films. This means they can create films, view all films, update, and delete any film.

User experience

Users are presented with a films icon at the top of the screen for mobile and tablet display and a navigation bar on desktopndisplay for Home, List of Films and Create films. A logo has been included to help easily navigate back to the homepage at any given time. An introductory heading has been included to guide the user to the website. A search bar has been included so the users can search for a film they would to find right away. In case a user has mistakenly inputted a wrong path in the URL, a 404 page will show with a link back to the home page. Edit films fields are filled out automatically so that the user does not need to input all the previous values back in before they submit an update. When the delete button is clicked on the Films page, the user is presented with a way to ensure they want to delete the film permanently.

The user's goal by using this website includes being able to see a well-functioning website to attract him to  use it, navigation/buttons that are simple, full control over all films on the website, clear separation between each instruction.

The developer's goals include: having every feature reacting to its intended purpose, showing clear examples of the usage of HTML, CSS, JavaScript, jQuery and Python. 


Design/Styling of the website

The design of the website was chosen to ensure that the user has the best experience.Styles have been chosen to give it a professionaland good-looking design.This was also reflected at the level of the Edit and Delete Buttons, as well as Forms, and images.


#Functionality of project


The website is fully responsive and uses MongoDBfor the users and films collection. The user is able to register, 
login and view films. Logged in users are able to create, update (edit) and delete their own films. Any user can search 
for films using the search box. A user can also log out. The Films page shows all films in order of the amount of views 
each film has. The pagination of the films is done by the database. Each film on the films page can be clicked onto and 
that will load the single films page which shows the entire entry. If the user created/added the film on this page, they 
will not be able to edit and delete this film. The add film allows the logged in user to create a film and enter it onto 
the database. 

Pagination features

Are reflected on the Home Page, Films Listing Page, actual Films Page, Add Films Page, Delete Films Page, Update Films Page. When the user arrives at the Films page, they are presented with the entire film, showing the films name, films image, film description, director. A delete button has been included so that the user has the option to delete the film and a detailed instruction on how to do so has been included. 

When the user arrives at the Add Films page, they are presented with a form which will show the following fields: Film Name, Film Description, Film Image URL, Create Film 'button'.

When the user arrives at the Delete Films page, they are presented with a form which will show the fields: Film Name, Film Description, Folm Image URL, Update Film button.


Features left to implement

Some of the features left to implement include: 

1. Community tab-which can be accessed by all users for the purpose of exchanging opinions on the content.

2. Pagination-on films page and onnstart page which would facilitate the navigation.

3. Logging in-forthe user to have control over his own films and is owned by the user. 

4. Search page-where the user would be presented with a title whowing how many search items have been found of whatever query was inputted into the search field. Then the user would be given the option to searvh for another item.If no results had been foundthen the user would be informed of that. 

5. Error 404 page-if at any time the user had inputted a value in the URL that has not been found, a 404 page will be presented and it will show the user a message that they got lost and will have a button which will lead them to the home page.

Database

The database used for this project was a NOsQL database called MongoDB as required. The data used are: ObjectID, String, Int32. A database was created called 'myFilms' which contains a collection called films which is where each piece of data for each 'film' is stored. The data structure is as follows: 

Film ID-with the field key  _id, field value <creates ID automatically>! type ObjectId
Film Title-with the field key film_name, field value <name of your film>, type string
Film Image URL-with the field key film_image_url, field value <Full image path of film>! type string
Film Description-with the field film_description, field value <Describe your film in a paragraph>, type string
Film Director-field key film_director, field value <Name of the film director>, type string
Film Genre-field key film_genre, field value <Name of the film genre>, type string


#Technologies used 

I used the following languages, frameworks, libraries to construct this project. 

HTML5-used for structuring and presenting the content

CSS/Bootstrap 4-used for the presentation of the web page, including the colours, layouts and fonts

JavaScript-used for creating the web page

MongoDB- make uses of collections and documents, is a database platform used to store all of the data for each film used on the website

Flask- used for building an application like a web page

Heroku-used to deploy, manage and scale the app

jQuery-used to make it easier to use JavaScript on the website, to simplify DOM manipulation

Github-used as a remote backup of code used in the project

#Deployment


This section describes the process I went through to deploy the project to a hosting platform (Heroku). The website 
was created in Gitpod, a local Git directory was used for version control and then uploaded to Github. A MongoDB 
database was used and set up inside Heroku. The details of the database connection are found inside the requirements.txt 
-it uses the os class environ method to point to its own config available (MongoDB_URI) in order to keep the production 
database connection string secret. There were no differences between the deployed version and the development version.

The following had to be installed on the computer before deployment: PIP, Python 3, Git, as well as having an account in MongoDB Atlas. 

The deployment to Heroku consisted mainly of the following steps: adding a requirements.txt file by using the command "sudo pip3 freeze-local> requirements.txt " which will add all the components needed to be used for the project; using "git add" to commit the changes ready to push to Github; creating the repository in Github and following the instruction in order to push the owrk up to Github; using "git push" and enteeing the email and password when instructed which will push all the files which have been committed up to Github; signing in to Heroku; creating a new app inside Heroku and then going to "Deploy" and scrolling down the list of instructions given to deploy the project in Heroku; viewing the project in Heroku by clicking "Open App".

#Testing

By testing I checked that all the user stories from the UX section worked as intended, with the project providing an 
easy and straightforward way for the users to achieve their goals. My tests checked the page loading, as well as the 
business logic of the views. The testing process can be described via scenarios.

The Create Film page was tested by checking that a film was entered, the page redirects and the new film is featured on the index page. The Films page is tested by searching for any films on the films page, getting its ID number and going to that Films details page and changing some data and committing it. This then redirects the user to the Index page and that is tested that the information has changed on that film. The Delete Films page is tested by going to its films details page and deleting 
it, then checking that the redirect has happened and that the film does not appear on the index page. It is impossible 
to cover everything in testing, but the majority of elements was tested. My focus was on keeping the design usable and 
simple to navigate. As the site is built with responsive design, it works for mobile devices and I have checked it on
iphones 6 to x, Smsung galaxy, ipads (mini to pro), Google's pixel 2 and 3. I also tested it on several browsers 
(Chrome, Explorer, Edge).

#Credits

The content has been written by myself, the developer. The mentor (Spencer Barriball), as well as the team (Kevin, Tim and others) have been very helpful in guiding me through the process and provided useful tips. 





