# Forum

Forum is a Django website, that allows you to create user profile, add topics and discuss it.

## Installation

Clone this repository:

```bash
git clone https://github.com/vladhutsal/Forum
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
  - create new user and login;
  - start new topic;
  - view the list of created topics;
  - comment topic;
  - delete comment;
  - gain accsess for deleting other people comments
 
 ## What can you do in the near future?
 1. Your user page:
  - edit your user page;
  - become an admin of the Hut site;
  - update your picture;
  - message other user;
 
 2. Topics list page:
  - list topics through pages;
  - add tags to your topic;
 
 3. Exact topic page:
  - like comments and post;
  - mark topic as favourite;
  - sort comments;
