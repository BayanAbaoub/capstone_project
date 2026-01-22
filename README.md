# Capstone Project 
## Project Overview 
This is a Django-based movie review website where users can read, favourite, and submit movie reviews. It has three main apps: blog, profiles, and submit. 
The blog app displays movie reviews, review detail pages, implements a commenting system, as well as favouriting feature. 
The profiles app is for user profile management. Registered users can update their bio and profile pictures and view all their favourited reviews. 
The submit app contains a form for users to submit reviews which the admin can review. 

## Features
### Navigation Bar 
A responsive navigation bar that is consistent on all pages. On larger devices the links are all accessible, whereas on smaller devices the links collapse to ensure better user interface (UI) and better user experience (UX) as well as those links become too crowded and difficult to click on smaller screens. The logo on the left hand side will take you back to the home page for ease. 
![navbar screenshots on various device sizes to show responsiveness](assets/images/navbar-screenshot-1.jpeg)

### Login Notification
There is a permanent notice below the navigation bar, specifically underneath the register and login links, to notify users if they are currently logged in or not. 
![screenshot of notification below navigation bar showing whether a user is logged in or not]

The picture that welcomes the users to the site is a logo of the website "Reel Reviews" with a movie reel incorporated to simply and effectively portray the website's topic to the visitor.
![screenshot of logo "Reel Reviews" in red with a movie reel beneath the text](assets/images/about-section-screenshot.png)

Then there are two rows of 3 movie reviews displayed in bootstrap cards. The cards are in a rectangular shape to fit the movie poster dimensions. Below each poster is the review title and a small excerpt of the actual review. Lastly, there is the review's author displayed with a small profile picture, as well as the date the review was uploaded. 
![screenshot of two rows of 3 bootstrap cards that display the movie poster, the review title, review excerpt, author, and upload date]

Below the two rows of reviews there is a next button to continue browsing reviews as well as a footer with social links.
![screenshot of next button and footer with links to (in order) Facebook, Twitter, Instagram, and YouTube]

### Submit Page
The submit page contains a photo showing various features of a cinema as well as submission form asking for the user's name, email, and submission with a submit button. Both the photo and form are fully responsive.
![screenshot of submit page photo and form]

### Profile Page
This page is only accessible if you a registered user and are currently logged. The top section shows your profile picture, username, date of registration, bio, and an edit profile button. The bottom section shows any reviews you have favourited in the same card style as on the home page with an addition of a "remove from favourites" button for ease of use.
![screenshot of profile page admin section with profile picture, username, date of registration, bio, edit profile button and any favourited reviews of user]

### Edit Profile Page
The edit profile page shows the user's current profile picture. Below there is a text box with their current bio which they can easily edit. Underneath there is a feature to upload any photo the user prefers. As well as a save changes and cancel button so that the user can easily understand whether their changes are permanent.
![screenshot of edit profile page with the user's current profile picture, bio, and fields to upload a custom picture]

### Review Pages
Each review displays the corresponding movie poster in the masthead beside the title of the review, author, and upload date. The favourite feature is below the review's title, with an add to favourite button which changes to favourited if you a logged in user. It will also notify the user at the top of the page that it has been added to their favourites or removed. Next to the favourite button is a count of how many times this specific review has been favourited by different users. 
Underneath the masthead is the review. Below the review is the comment section that shows already posted by other users (and approved by the admin). There is a "leave a comment" section beside the comments that will only show all of it's features if the user is logged in. Users can only comment text. The logged-in user can also edit and delete their comments. 
![screenshot showing review page with add to favourites button shown]
![screenshot showing review page with add to favourites button changed to favourited]
![screenshot showing comment section when logged in]
![screenshot showing comment section when logged out]

### Register Page
The signup page provides fields for new users to create an account:
1. Username - Unique identifier for the user.
2. Email address - For account verification and communication (optional by default).
3. Password - Secure password field with masking.
4. Password confirmation - Re-enter password to prevent typos.

The form uses built-in validation through django-allauth. The powerful tool checks if the chosen username has already been taken, ensures passwords match, validates email format and password strength, and shows error messages for invalid inputs to clarify to the user where they went wrong.

The first sentence on the page asks users if they already have an account and directs them to the login page instead if they do.
![screenshot of register page with fields for username, email, and password]

### Login Page
The login page provides a streamlined form for existing users to login with their username and password. There is also an option "Remember Me" feature to stay logged in. This form is also validated through django-allauth. Users are directed to the homepage after successfully logging in and gain immediate access to all features that require authentication (favourites, comments, and profiles).
![screenshot of login page with fields for username and password]

## Additional Features
Fully responsive layout - the site works well on desktop, tablet, and mobile devices
Accessible - the site has been run through an accessibility checker to ensure that is easy to read and that all alt text is included so that there will be no problems with screen readers

## Planning - Wireframes and ERD Diagrams
### Wireframes
I utilised balsamiq to plan the structure and layout of the website as the software is easy to use and creates clear and realistic wireframes. My original mock-ups are very similar to the finished website as I tried to stick to simple front-end features to focus on learning django.
![screenshot of wireframes showing website on various device sizes]

### ERD Diagrams
ERD diagrams are imperative in these type of projects to ensure the data you store is correctly connected. Furthermore, the diagrams helped me to visually realise what information is stored where and helped reduce the amount of mistakes I made.
The first ERD diagram I made only had three tables. However, as I expanded my project I reworked the diagram.
![screenshot of ERD diagram with three tables]
![screenshot of reworked ERD diagram with more than table]

## Testing 

## Issues
The first issue I encountered was trouble deploying. Whilst following a set-uo guide it can be easy to misread or mistype instructions. Luckily, after reviewing the steps again with fresh eyes, I was able to fix my deployment issue, which was due to a typo in my Procfile.  

- erd diagrams for additional features - didn't do it but should have 

## AI
CoPilot as a problem solving tool can be very useful. I find it most useful when you ask specific questions that are invaluable as a study tool, find it most useful when asked specific questions that have the appropriate context included. I used AI to further explain the steps for creating a new Django app, as well as to help debug my code. This involved feeding it error messages with the prompt to explain the error code as well as provide the solution which is invaluable to a beginner. 

## Deployment

Heroku is the platform used to host this website. The project is connected to GitHub which makes deployment very easy and simple. 

### Required Files
In order to deploy, Heroku needs the following files in your project root:
- **`requirements.txt`** - Lists all Python packages and versions needed
- **`Procfile`** - Tells Heroku how to run your app (contains: `web: gunicorn capstone_project.wsgi`)

### Configuration Steps
Other necessary steps include:
- **Settings.py updates** - Import required packages (`os`, `dj_database_url`)
- **Environment variables** - Set SECRET_KEY, DEBUG, and Cloudinary credentials in Heroku Config Vars
- **Database configuration** - Configure PostgreSQL database with `dj_database_url`
- **WhiteNoise middleware** - Added to MIDDLEWARE for static file serving
- **Static files configuration** - Set STATIC_ROOT and STATICFILES_STORAGE
- **Database migrations** - Run `heroku run python manage.py migrate`
- **GitHub connection** - Connect repository in Heroku Deploy tab

### Deployment Process
1. In your Heroku app dashboard, navigate to the "Deploy" tab
2. Connect to GitHub and select your repository
3. Scroll to "Manual deploy", select your branch (main/master)
4. Click "Deploy Branch"
5. Once deployment completes, click "View" or "Open App" to view your live website

### Post-Deployment
After the first deployment:
- Run migrations: `heroku run python manage.py migrate`
- Create superuser: `heroku run python manage.py createsuperuser`
- Collect static files: `heroku run python manage.py collectstatic --noinput`

The live site is accessible at: [Your Heroku URL]

## Credit
- Previous walkthrough project 
- Django
- Bootsrap v.5 
- Cloudinary
- CoPilot 
- FontAwesome
- Google Images






