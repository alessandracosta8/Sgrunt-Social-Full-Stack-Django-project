# Sgrunt Social

Sgrunt social is a social network dedicated to share news and articles and allow the users to share their opinion and ideas about it. The app is targeted to towards people that enjoy commenting and sharing their ideas about what is going on in the world.

The name of the app comes from the tipical expression from classic comic books, when the carachters wanted to express their disappointment.

The live link can be found here - [Sgrunt Social](https://sgrunt-social.herokuapp.com/)

&nbsp;

## Table of Contents
---
- [Agile Methodology](#agile-methodology)
    - [User Stories](#user-stories)
- [Design](#design)
- [Data Model](#data-model)
- [Testing](#testing)
    - [User Stories testing](#user-stories-testing)
    - [Validation](#validation)
    - [Desktop Browsers Testing](#desktop-browsers-testing)
    - [Mobile Testing](#mobile-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Security Features and Defensive Design](#security-features-and-defensive-design)
    - [User Authentication](#user-authentication)
    - [Form Validation](#form-validation)
    - [Custom error pages](#custom-error-pages)
- [Deploy to Heroku](#deploy-to-heroku)
    - [Create the Heroku App:](#create-the-heroku-app)
    - [Attach a Postgres database:](#attach-a-postgres-database)
    - [Prepare the environment and settings.py file:](#prepare-the-environment-and-settingspy-file)
    - [Create files and directories](#create-files-and-directories)
- [Technologies](#technologies)
- [Credits](#credits)

&nbsp;

## Agile Methodology
---
Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/users/alessandracosta8/projects/3)
Three iterations were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to an Iteration and rated according to their importance and urgency.

### User Stories

#### Epic: Login, Users and Follow
- As a **User** I can **login** so that **I can interact with the content or create content**.
- As a **User** I can **follow or unfollow other users** so that **I can be updated on what the people I want to follow are posting, or stop it**.
- As a **User** I can **have my own profile** so that **I can share my info and display all of my posts**.
- As a **User** I can **edit my profile** so that **I can edit my informations**.
- As a **User** I can **click on any post or comment author** so that **I can view the full profile of that user**.
- As a **User** I can **search in the navbar for other users** so that **I can easily find people I want to connect with**.
- As a **User** I can **see the follower list of users** so that **I am aware of user who follow me and that follow others**.

#### Epic: Post and comment
- As a **User** I can **post some text** so that I can **share my thoughts or ideas**.
- As a **User** I can **comment on somebody's post** so that I can **share my thoughts or ideas on that topic**.
- As a **User** I can **click on a Post** so that **I can read the post's page and view all of its comments**.
- As a **User** I can **edit or delete a post** so that **I can change what I've shared or delete it**.
- As a **User** I can **delete a comment** so that **I can change what I've shared or delete it**.
- As a **User** I can **view only the posts of the users I follow** so that **I can focus only on the content I care about**.
- As a **User** I can **like or upvote a post** so that I can **express my preference for the post**.
- As a **User** I can **upload an image** so that **I can share it with my followers**.

#### Epic: Future Features
- As a **User** I can **login with Apple or Google account** so that **I can signup without creating an account**.

&nbsp;

## Design
---
The website has a simple an minimalistic design, to leave all the user attention on the content written by the users and the images shared. The colours choosen are subtle and in grey tones to leave all the colour brilliance to the images posted.

### Wireframes

<details>
<summary>Landing page</summary>

![Landing Page](docs/wireframes/landing_page.png)
</details>

<details>
<summary>Post List</summary>

![Post List](docs/wireframes/post_list.png)
</details>

<details>
<summary>Profile</summary>

![Profile](docs/wireframes/profile_page.png)
</details>

<details>
<summary>Post Detail</summary>

![Post Detail](docs/wireframes/post_detail.png)
</details>

<details>
<summary>Followers List</summary>

![Followers List](docs/wireframes/followers_list.png)
</details>

&nbsp;

## Data Model
---
I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.
Django AllAuth was used for the user authentication system.

In order to create the social network various models were required: the post, comment and user profile.
The author is a foreign key that is shared in-between the post and comment model. All of the models are based on the use of the generic User model from Django.

The Post model in specific has multiples fields which allow the post to have amongst its features: likes, dislikes and images attached. In particular two views are put in place (AddLike and AddDislike), which will manage the like functionality so that a post that is dislked cannot be liked at the same time and viceversa.

The Comment model is a more simple model taking as the foreign keys the post it is related to and the author of the comment itself.

The UserProfile model takes the User model as base structure and attaches the various details needed, including a profile picture that the user can upload and the list of followers the user currently has.

The diagram below details the database schema.

![Database Schema](docs/readme_images/sgrunt-social-database-schema-diagram.jpeg)

&nbsp;

## Testing
---

### User Stories testing
Every user story has been manually tested.

### Validation
- All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/).
- All CSS files were validated through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- All JavaScript was validated through [Jshint](https://jshint.com/)
- All Python files were run through [Pep8](http://pep8online.com/) with no errors found.
- Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility and performance.

### Desktop Browsers Testing
- The Website was tested on Google Chrome, Firefox, on Windows OS and Google Chrome, Firefox and Safari on MacOs with no issues noted. 

### Mobile Testing
- The website was viewed on a variety of devices such as iPhone 13 Pro, iPhone 13 Pro Max, iPhoneXR, Google Pixel 4, iPhone SE and iPad to ensure responsiveness on various screen sizes in both portrait and landscape mode. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

### Fixed Bugs
- When deployed to Heroku, all images uploaded to the posts disappear after some time. Resolved: Setting up  Cloudinary to handle images.
- When a new user Signs Up the websites returns error 500, but in reality the user has been created and they can login as normal. Resolved correcting the settings of the login pages resirect and email verification.
- When setting DEBUG = False was setup, error 500 was returned and no content was accessible. Resolved removing incorrect code handling 404 pages errors.

### Unfixed Bugs
- Unable to load a custom 404 or 500 page. It returns an "Internal server error".

&nbsp;

## Security Features and Defensive Design
---

### User Authentication
- LoginRequiredMixin is used to make sure that any requests to access secure pages by non-authenticated users are redirected to the login page, preventing any unwanted requests.
- UserPassesTestMixin is used to ensure users can only edit/delete posts and comments for which they are the author. If the user doesn't pass the test they are shown an HTTP 403 Forbidden error.

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error.

### Custom error pages
Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 400 Bad Request - Sgrunt Social is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - Sgrunt Social is currently unable to handle this request

&nbsp;

## Deploy to Heroku
To deploy this page to Heroku from its GitHub repository, follow this steps:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach a Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add the CLOUDINARY_USERNAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET values to your env.py file.
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files and directories
- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi:application

### Update Heroku Config Vars
Make sure the following Config Vars in Heroku are setup as well as in the env.py file:
- DATABASE_URL
- SECRET_KEY value 
- CLOUDINARY_USERNAME
- CLOUDINARY_API_KEY
- CLOUDINARY_API_SECRET
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.


&nbsp;

## Technologies
---
- [GitHub](https://github.com/) - for version control and product backlog.
- [Notion](https://notion.so/) - for notes taking and tasks manager.
- [GitPod](https://gitpod.io/) - as development environment.
- [Heroku](https://heroku.com/) - as cloud based platform to deploy the web app on.
- [PostgreSQL](https://postgresql.org/) - as database.
- [DJ database url](https://pypi.org/project/dj-database-url/) - database setup.
- [Psycopg](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html) - for authentication of users.
- [Django Crisy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - for forms styling.


## Credits
---
- Code Institute tutor support for all the support they provided.
- [Django AllAuth Templates](https://github.com/pennersr/django-allauth)
- [Django Documentation](https://docs.djangoproject.com/en/4.1/)
- [Mozilla Django Testing Tutorials](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
- [Django testing tutorials](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)
- [PyLint tutorial](https://www.youtube.com/watch?v=w6bRHNC7Kuc&t=30s)
- [Django social media app tutorial](https://www.youtube.com/playlist?list=PLPSM8rIid1a3TkwEmHyDALNuHhqiUiU5A)
- [Unsplash free stock photos](https://unsplash.com/)
- [FontAwsome Icons](https://fontawesome.com/)
- [Django quering (Q)](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
- [Heroku deployment](https://www.youtube.com/watch?v=XZoTukqekzY)
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Figma](https://www.figma.com/) - used to create wireframes
- [Deployment Checklist Tutorial](https://www.youtube.com/watch?v=mAeK4Ia4fk8)
- [Cloudinary integration](https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/)
- [Example of excellent readme file from AliOKeeffe](https://github.com/AliOKeeffe/PP4_My_Meal_Planner/blob/main/TESTING.md#device-testing)