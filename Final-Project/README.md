## Table of contents
- About
- Usage
- Logic
- Resources
- Notes

## About

The idea of the app came to me during my language learning time (which is still going on, at the time of writing this at least), and since I had some decent amount of free time, I started CS50 on the side. FlashCards is an output to both CS50 and and language learning journies. 


## Usage
After downloading the source code, simply run the following command in your terminal.

```bash
flask run
```
If not logged in, the navigation bar at the top will contain 2 links, one for logging in and the other for registeration. After logging in, user is able to visit `Add`, `Practice`, `Quiz`, and `Vocabulary` pages.

This [video](https://youtu.be/GFyAJpl6Je8) demonstrates the usage process for the application.

## Logic
FlashCards50 is a web app that uses flask framework in Python. There are 2 folders in the project directory, `static`, which contains the Javascript and CSS of the project, and `templates` that contains all html templates for the rendered pages. There is also `flashcards.db` which is the database that stores all user information, as well as their dictionaries.


### `app.py` 

At the start of `app.py`, there are the libraries and functions used, including another file called `helpers.py` that containes `apology` and `login_required` functions, which are taken from [CS50's Problem Set 9](https://cs50.harvard.edu/x/2023/psets/9/finance/). Then there is the session and flask setup, and the different app routes for each template. 

### `flashcards.db`

When first installing, `flashcards.db` will have only one table that contains users information. With each new register, a new table is created with the username as it's name. This is done in the `register` function inside `app.py`.

### `static`
There are 3 files in here. `styles.css`, which is the style sheet, `app.js` which is linked to `practice.html` and does all the logic for it, and `quiz.js` whichis linked to `quiz.html` and checks the user's answer and compares it with the correct meaning in `flashcards.db`.

### `templates`

In here, there are: 
- `add.html`, used to add words into user's dictionary.
- `apology.html`, which renders an image in case of wrong login information.
- `index.html`, which is the (empty) main page.
- `layout.html`, a blueprint used by other templates.
- `login.html` & `register.html`, containing the forms for logging in and registering.
- `quiz.html`, a simple quiz for the user.
- `practice.html`, a quick practice which takes random words and their meanings from the user's dictionary.
- `vocab.html`, a template for all the words and their meaning entered by the user.

## Recourses

- [CS50 Library For Python](https://github.com/cs50/python-cs50)
- [Bootstrap v5.1](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Weckzebug Security](https://werkzeug.palletsprojects.com/en/2.2.x/)
- [Memegen](https://memegen.link/)
- And various tutorials from Youtube, Stackoverflow, and other sites!

## Notes
I plan to improve this in the furure by adding a section for graded quizes, as well as doing better CSS styling and Javascript logic.

I might also do the same app using Node.js, as I tried using some modules from it in my Javascript just to realise later that it's not very easy to use it with a flask framework.