# Fats n Babs Restaurant Booking System

![Fats n Babs Logo](/media/images//fatsnbabs-logo.png)

The live site can be found here [Fats n Babs](https://fatsnbabs-216f47f1be28.herokuapp.com/mybookings)

Fats n Babs is a local cafe & restaurant which serves a variety of Pakistani and British food.

This site is designed to facilitate the process of making booking and managing bookings at the restaurant. It streamlines the booking process for users, improving efficiency and user experience. 
The booking system provides an easy-to-use interface for users to make booking. users can select the date, time, and party size for their booking. The system checks the restaurant's availability for the specified date and time. If there is a table available, the user receives an immediate confirmation.
Users are able to manage their bookings once they are logged in to amend the date, time or number of seats. They are also able to delete their bookings.

## CONTENTS

- [User Experience](#user-experience-ux)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)

- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Wireframes](#wireframes)

- [Features](#features)
  - [General Features on Each Page](#general-features-on-each-page)
  - [Models](#models)
  - [Accessibility](#accessibility)

- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

- [Deployment & Local Development](#deployment--local-development)
  - [Deployment](#deployment)

- [Testing](#testing)
  - [Bugs](#bugs)

- [Credits](#credits)


# User experience

[Go to the top](#table-of-contents)

## Project Goals
* The site a simple design with a minimalistic color scheme to help keep the focus on the content.
* The website is designed to adapt to different screen sizes for optimal accessibility.
* The overall goal of this project is to allow the user to navigate the website, register/login and create/edit/delete bookings.

## User Stories

I used GitHub Projects to help log my user stories. By doing this, I was able to keep on track. I moved any tasks from Todo into In Progress as I worked on them, and then into Done once completed.
I then moved onto the next set of tasks and followed the same steps until all the tasks were done.

![workflow1](/media/workflow/workflow1.png)
![workflow2](/media/workflow/workflow3.png)
![workflow3](/media/workflow/workflow5.png)

#### User Goals

* To be able to view the site on a range of device sizes.
* To make it easy for new users to view the restaurant's menu.
* To make it clear for users how to book a table.
* To allow users to manage their bookings.

#### First Time Visitor Goals

* I want to easily navigate the site so that I can locate the information I want quickly.
* I want to view the restaurants menu so that I can decide whether I want to book a table or not.
* I want to be able to view where the restaurant is located.
* I want to be able to register an account so that I can book a table.

![Workflow 4](/media/workflow/workflow2.png)

#### Returning Visitor Goals

* I want to login so I can view my booking.
* I want to be able to edit my booking.
* I want to be able to delete my booking.

![Workflow 5](/media/workflow/workflow4.png)

# Design

## Colour Scheme

![Colour Palette](/media/images/fatsnbabs-palette.png)

The site uses a palette of cool colours, with a constant theme throughout. The colour palette was created using [Coolors](https://coolors.co/).

## Typography

Ubuntu Light 300 was used from Google Fonts for the site.

![Ubuntu Google Fonts](/media/images/ubuntu-google-fonts.png)

I chose this font as I felt it was simple yet unique.

## Wireframes

Home:
![Wireframe1](/media/wireframes/home.jpg)

Home (mobile):
![Wireframe2](/media/wireframes/home-mobile.jpg)

Menus:
![Wireframe3](/media/wireframes/menu.jpg)

Menus (mobile):
![Wireframe4](/media/wireframes/menu-mobile.jpg)

Book a Table:
![Wireframe5](/media/wireframes/booking.jpg)

Book a Table (mobile):
![Wireframe6](/media/wireframes/book-mobile.jpg)

My Bookings:
![Wireframe7](/media/wireframes/manage-booking.jpg)

My Bookings (mobile):
![Wireframe8](/media/wireframes/manage-booking-mobile.jpg)

Location:
![Wireframe9](/media/wireframes/location.jpg)

Location (mobile):
![Wireframe10](/media/wireframes/location-mobile.jpg)

Login:
![Wireframe11](/media/wireframes/login.jpg)

Login (mobile):
![Wireframe12](/media/wireframes/login-mobile.jpg)

Sign Up:
![Wireframe13](/media/wireframes/signup.jpg)

Sign Up (mobile):
![Wireframe14](/media/wireframes/signup-mobile.jpg)

# Features

  ## General Features on Each Page

  ### Navbar & Footer

The navbar is located at the top of the page and is fixed - it shows differently depending on whether the user is logged in or not.

Logged in:

![Navbar Logged In](/media/images/navbar-logged-in.png)

Logged out:

![Navbar Logged Out](/media/images/navbar-logged-out.png)

The menu collapses into a burger menu when on a mobile:

![Navbar Mobile](/media/images/navbar-mobile.png)
![Navbar Mobile Expanded](/media/images/navbar-mobile-expanded.png)

The footer is located at the bottom of the page and is also fixed. It has a link to the Where To Find Us page and links to the social media pages.

### Homepage

The homepage is made up of two main parts. The main landing screen, and a carousel that cycles through some useful quick links.

Homepage:

![Homepage](/media/images/homepage.gif)

Homepage (mobile):

![Homepage Mobile](/media/images/homepage-mobile.gif)

### Menus

The menu page is split up into 3 columns. Brunch, Lunch & Afternoon Tea.
The Lunch column is a carousel that cycles through the three different lunch menus.

Menu, Lunch Bites:

![Menu, Lunch Bites](/media/images/menu-lunch-bites.png)

Menu, Paninis:

![Menu, Paninis](/media/images/menu-paninis.png)

Menu, Salads:

![Menu, Salads](/media/images/menu-salads.png)

Menu (Tablet):

![Menu (Tablet)](/media/images/menu-tablet.png)

Menu (Mobile):

![Menu (Mobile)](/media/images/menu-mobile.png)

### Book a Table

The Book a Table page consists of a form that allows the user to book a table at the restaurant.

The user must choose a table, date and time of the booking.

Book a Table:

![Book a Table](/media/images/book.png)

Book a Table (Mobile):

![Book a Table (Mobile)](/media/images/book-mobile.png)


### My Bookings

The user is able to view, edit and delete their bookings in the My Bookings page

My Bookings:

![My Bookings](/media/images/manage.png)
![My Bookings Expanded](/media/images/manage-expanded.png)
![My Bookings No Bookings](/media/images/bookings-empty.png)

My Bookings (Mobile):

![My Bookings (Mobile)](/media/images/manage-mobile.png)
![My Bookings (Mobile) Expanded](/media/images/manage-mobile-expanded.png)

### Where To Find Us

The Where To Find Us page consists of a map with the restaurant's location, the user is also able to click on the Directions icon to get directions via Google Maps.

Underneath the map is some information on the restaurant's opening & closing times and the address written out in full.

![Where To Find Us](/media/images/location.png)
![Where To Find Us](/media/images/location-mobile.png)

### Sign Up, Login & Sign Out

Sign Up:

- The sign up form is a simple form that requires the user to enter a username, an optional email address and a PASS |word.
- The user must re-enter the PASS |word for confirmation and it must match the original PASS |word entered.
- There is a message to remind users that if they already have an account, they can click the sign in link to be directed to the sign in page.
- If the user enters an username that is already registered, an error message will appear.
- If the user enters a PASS |word that is not secure, they will be prompted with a message to create a stronger PASS |word.
- The sign up form verifies that both PASS |words entered match. If the user enters PASS |words that do not match, an error message will appear to notify them.

![Sign Up](/media/images/signup.png)

Login:

- The login form requires users to enter their username and the PASS |word that they used when they signed up.
- There is a message to remind users that if they haven't created an account, they can click the sign up link to be directed to the sign up page.
- If the user enters the wrong credentials, an error message will be displayed to inform them.

![Login](/media/images/login.png)

Sign Out:

- When the user clicks the sign out button from the navbar, a modal will appear to confirm the action before the user is signed out.

![Sign Out](/media/images/sign-out.png)


# Models

Two models were created for this project:

### Table:
  - To handle the tables in the restaurant - so users can choose how many people the booking is for and so the system can check to make sure no double booking occurs.

### Reservation:
  - To handle the booking process - defines the 4 key factors when a user requests a booking:
    * Client (User)
    * Table - taken from Table model
    * Date
    * Time

![Models](/media/images/models.png)

# Technologies Used

## Languages Used:
* HTML5
* CSS3
* Python

## Frameworks, Libraries & Programs Used:
* Bootstrap - The framework for the website. Code for the navbar, carousel, cards and form were used and modified. Additional CSS styling was also implemented in style.css.
* Cloudinary - Used to host background images for the homepage and menu page.
* Django (inlcuding Allauth) - django framework used to build the site. Allauth used for login/sign up/sign out functions.
* ElephantSQL - Database management site used.
* Font Awesome - Icons used for this project.
* Git - GitHub & GitPod used for workspace management.
* Google Fonts - Used for the fonts on the site.
* Heroku - Used for deployment.
* Whitenoise - Used to help serve staticfiles.

# Deployment & Local Development

## Deployment

-  Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
- Install support libraries including psycopg2, this is used to connect the PostgreSQL database
- Install Cloudinary libraries, this is a host provider service that stores images
- Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

1. Create a new, blank Django Project:
    - Create a new project
    - Create the app
    - Add restaurant_booking to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

2. Setup project to use Cloudinary and PostgreSQL:
    - Create new Heroku app
    - Sign into Heroku
    - Select New
    - Select create new app
    - Enter a relevant app name
    - Select appropriate region
    - Select the create app button

3. Prepare the environment and settings.py file:
    - Create env.py file
    - Add DATABASE_URL with the Postgres URL from Heroku
    - Add SECRET_KEY with a randomly generated key
    - Add SECRET_KEY and generated key to the config vars in Heroku
    - Add if statement to settings.py to prevent the production server from erroring
    - Replace insecure key with the environment variable for the SECRET_KEY
    - Migrate changes to new database

4. Create a database in ElephantSQL:
    - Create account and create new instance
    - Select a plan and an apropiate name
    - Select a region near the user location
    - Add DATABASE_URL with the ElephantSql URL

5. Get static media files stored on Cloudinary:
    - Create a Cloudinary account
    - From the dashboard, copy the API Environment variable
    - In the settings.py file create a new environment variable for CLOUDINARY_URL
    - Add the CLOUDINARY_URL variable to Heroku
    - Add a temporary config var for DISABLE_COLLECTSTATIC
    - In settings.py add Cloudinary as an installed app
    - Add static and media file variables
    - Add templates directory
    - Change DIR's key to point to TEMPALTES_DIR
    - Add Heroku hostname to allowed hosts
    - Create directories for media, static and templates in the project workspace
    - Create a Procfile

6. For the final deployment to Heroku:
    - Set debug = False in the settings.py file.
    - Commit and push all files to GitHub
    - In Heroku, remove the DISABLE_COLLECTSTATIC config var.
    - In the deploy tab, go to the manual deploy sections and click deploy branch.

# Testing

### HTML:

I used the [W3C Markup Validator](https://validator.w3.org/#validate_by_input). All errors found have now been resolved:

![W3C Error](/media/images/w3c.png)
![W3C Error 2](/media/images/w3c2.png)

### CSS:

The [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check my CSS.
No Errors or warnings were found:

![W3C CSS](/media/images/w3c-css.png)

### Python

I used the [PEP8 Python Linter](https://pep8ci.herokuapp.com/) to check my Python. No errors apart from "line too long"

![PEP8](/media/images/pep8.png)
![PEP8](/media/images/pep8-1.png)
![PEP8](/media/images/pep8-2.png)

### TDD

Some automated testing was used on the form. These can be found in test_form.py

### Manual Testing

#### All Pages:
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
Home page | When the "home" button in the navbar is clicked, the browser redirects the user to the home page and the "active" styling appears on the home button | PASS |
Navbar |When a page link in the navbar is clicked, the browser redirects the user to the relevant page and the "active" styling appears on the page link. | PASS |
Book a Table | When the "Book a Table" link in the navbar is clicked, the browser redirects the user to the Book a Table page and the "active" styling appears on the page link.| PASS |
Login  /Sign Up | When the user is not logged in, the navbar shows "Sign Up" & "Login" rather than "My Bookings". When the "Sign Up" or "Login" links are clicked, the browser redirects the user to the relevant page and the "active" styling appears on the page link.| PASS |
My Bookings | When the "My Bookings" link in the navbar is clicked, the browser redirects the user to the My Bookings page and the "active" styling appears on the page link. This page only shows when the user is logged in. | PASS |
Where To Find Us page | When the "Where to Find Us" link in the carousel is clicked, the browser redirects the user to the "Where to Find Us" page and the map loads correctly. | PASS |
Foreground & background colour | Checked foreground information is not distracted by background color or images | PASS |
Text | Checked that all fonts and colours used are consistent. | PASS |

#### Footer
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
Where To Find Us page | When the "Where to Find Us" link in the footer is clicked, the browser redirects the user to the "Where to Find Us" page and the map loads correctly. | PASS |
Facebook | When the Facebook icon is clicked, a new tab will open and the user will be redirected to the Facebook website. | PASS |
Twitter | When the Twitter icon is clicked, a new tab will open and the user will be redirected to the Twitter website. | PASS |
Instagram | When the Instagram icon is clicked, a new tab will open and the user will be redirected to the Instagram website. | PASS |

#### Home
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| Background | All media assets are displayed correctly, without any pixelation or stretched images, and are responsive on all devices. | PASS |
| Responsiveness | All elements on the page have been checked to ensure consistent scalability across mobile, tablet, and desktop views. | PASS |
| Accessibility |The accessibility of the page has been checked using Lighthouse.| PASS |
Carrousel | The links in the carousel are functional and take the user to the correct pages. | PASS |

![Lighthouse Home](/media/lighthouse/lighthouse-home.png)

#### Book a Table
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| Responsiveness | All elements on the page have been checked to ensure consistent scalability across mobile, tablet, and desktop views.| PASS |
| Accessibility |The accessibility of the page has been checked using Lighthouse.| PASS |
| Form | Checked the form submits only when all required fields are filled out. | PASS |
| Date | When the calendar is clicked, it is loaded quickly and smoothly and is responsive. | PASS |
| Time | The Time dropdown correctly shows the times selection from the model | PASS |

![Lighthouse Booking](/media/lighthouse/lighthouse-booking.png)

#### My Bookings page
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| Responsiveness | All elements on the page have been checked to ensure consistent scalability across mobile, tablet, and desktop views.| PASS |
| Accessibility |The accessibility of the page has been checked using Lighthouse. | PASS |
| Dropdown | Clicking on a booking activates the dropdown, showing the edit and delete buttons. | PASS |
| Edit |Clicking on the edit button takes you to the edit page. | PASS |
| Delete |When the delete button is clicked, a modal appears to confirm the action before it is executed. | PASS |
| No booking |A button linking to the Book a Table page is present and functional.| PASS |

![Lighthouse Manage](/media/lighthouse/lighthouse-mybookings.png)

#### Edit Bookings page
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| Responsiveness | All elements on the page have been checked to ensure consistent scalability across mobile, tablet, and desktop views.| PASS |
| Accessibility |The accessibility of the page has been checked using Lighthouse.| PASS |
| Form | Checked the form submits only when all required fields are filled out. Submission of form updated the booking correctly. | PASS |

![Lighthouse Edit](/media/lighthouse/lighthouse-edit.png)

### Sign Up page
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| Responsiveness | All elements on the page have been checked to ensure consistent scalability across mobile, tablet, and desktop views.| PASS |
| Accessibility |The accessibility of the page has been checked using Lighthouse.| PASS |
| Register form | Checked the form submits only when all required fields are filled out. | PASS |
| Sign In link | Checked the sign in link redirects to the sign in page. | PASS |

![Lighthouse Sign Up](/media/lighthouse/lighthouse-signup.png)

#### Login page
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| Responsiveness | All elements on the page have been checked to ensure consistent scalability across mobile, tablet, and desktop views.| PASS |
| Accessibility |The accessibility of the page has been checked using Lighthouse.| PASS |
| Sign in form | Checked the form submits only when all required fields are filled out. | PASS |
| Sign Up link | Checked the sign up link redirects to the sign up page. | PASS |

![Lighthouse Login](/media/lighthouse/lighthouse-login.png)

#### Sign Out
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| When the Sign Out button in the navbar is clicked, the user is redirected to the Sign Out page | PASS |
| When the Sign Out button on the Sign Out page is clicked, the user successfully signed out of their account | PASS |

![Lighthouse Sign Out](/media/lighthouse/lighthouse-signout.png)

#### Where To Find Us page
| TEST | OUTCOME |PASS / FAIL |
| :--- | :--- | :--- |
| Map | The map asset is displayed correctly, without any pixelation or stretched images, and is responsive on all devices. | PASS |
| Responsiveness | All elements on the page have been checked to ensure consistent scalability across mobile, tablet, and desktop views.| PASS |
| Accessibility |The accessibility of the page has been checked using Lighthouse.| PASS |

![Lighthouse Location](/media/lighthouse/lighthouse-location.png)

## Bugs

### Fixed Bugs
* Static files were not loading when deploying to Heroku.
    * Error message was stating "Not Found: /static/css/styles.css" 
    * After troubleshooting and Googling I found this [Slack thread](https://code-institute-room.slack.com/archives/C026PTF46F5/p1688850855667969)- I installed Whitenoise which resolved the issue

* | Accessibility on My Bookings page was low due to id being used twice.
    * Issue resolved. Removed id from one of the divs

 

* Book a Table form was not submitting.
    * Human error - closing form tag had been deleted.

### Unfixed Bugs

* Lunch menu on mobile device is longer than I wanted.
    * Attempted to fix, but it pushed all other items on screen away.
    * Kept as is, as the menu is still readable and easy to navigate - just a cosmetic issue.

# Credits

* The Slack Community - was regularly checked and issues often found to be resolved by someone there.
* My fellow CI students for helping me understand the Python code for setting up models and views.
* https://github.com/NDevox/django_restaurant_manager & https://github.com/andreagrandi/booking-example - when doing initial research into project
* CI Module [I Think Therefore I Blog](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) for really helping me understand models in django.
* [Geeks for Geeks](https://www.geeksforgeeks.org/form-as_p-render-django-forms-as-paragraph/) used when researching how to create a form from a django model.
* https://www.youtube.com/watch?v=gpTrmDpadZY - to help me understand email notifications through Django - did not end up using.
* Tutor Support - for clearing up some points to do with the assesment criteria.
* My wife for the menu and restaurant idea.

## Media Used

* https://timesofindia.indiatimes.com/life-style/food-news/how-to-make-masala-chai-at-home/articleshow/69027092.cms for Menu Background
* https://lovelaughmirch.com/indian-afternoon-tea-menu-ideas-recipes/ for Homepage Background