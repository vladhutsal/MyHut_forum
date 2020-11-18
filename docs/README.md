# Forum

Forum is a Django website, that allows you to create user profile, add topics and discuss it.

## Installation

Clone this repository:

```bash
git clone https://github.com/vladhutsal/MyHut_forum
```
Next moves in your repository folder, where manage.py is located.
  1. Activate virtual environment (for Linux):
```bash
source env/bin/activate
```
  2. Make migrations:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
  3. Run server:
```bash
python3 manage.py runserver
```

## What can you do?
  - register and login;
  - create new topic;
  - view the list of created topics;
  - comment topic;
  - delete comment;
  ~~- gain accsess for deleting other people comments~~
 
 ## What can you do in the near future?
 1. Your user page:
  - edit your user page;
  - become an admin of the Hut forum;
  - update your picture;
  - message other user.
 
 2. Topics list page:
  - list topics through pages;
  - add tags to your topic.
 
 3. Detail topic page:
  - like comments and post;
  - mark topic as favourite;
  - sort comments;
  - delete only topics and comments that belongs to you;
  - delete any topic or comment, if you are an admin.
