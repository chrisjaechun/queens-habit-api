# Queens Habit

The API for the Queens Habit application. This will allow users to sign-up, sign-in, change password and sign-out. Once authenticated, users can submit experiences, view their respective experiences, view all submitted experiences but may only update and delete their own experiences.

## Important Links

- [Client Repo](https://github.com/chrisjaechun/queens-habit-client)
- [Deployed API](https://queens-habit.herokuapp.com/)
- [Deployed Client](https://chrisjaechun.github.io/queens-habit-client/#/)


## Installation

1. Fork and clone this repository.
2. Change into the new directory.
3. Create and checkout to a new branch.
4. Run `pipenv shell` to start up your cirutal environment.
5. Run `pipenv shell` to install dependencies.
6. Create a psql database for the project.
    1. Type `psql` or `psql -U postgres` to get into interactive shell
    2. Run `CREATE DATABASE "queens-habit";`
    3. Exit shell
7. Generate and run migrations.
8. Run the server.


## Technologies Used

- Django
- Python
- PostgreSQL
- Heroku
- Pipenv

## API Endpoints

### Authentication:
| Action | Method | Path |
| ----------- | ----------- | ----------- |
| Sign-Up | POST | `/sign-up`
| Sign-In | POST  | `/sign-in`
| Change-Password |  PATCH | `/change-password`
| Sign-Out | DELETE | `/sign-out`


### Experiences: (Token Required)
| Routes | Method | Path |
| ----------- | ----------- | ----------- |
| Create | POST | `/submit-experience`
| Index All | GET | `/experiences-all`
| Index | GET | `/experiences`
| Show | GET | `/experiences/<int:pk>/`
| Update | PATCH | `/update-experience/<int:pk>/`
| Delete | DELETE | `/experiences/<int:pk>/`

All data returned from API will be formatted as JSON.

## Planning

First, I set up a model for the Experience resource with the keys of `what`, `where` & `notes`.

With the model in-place, I added the typical CRUD routes with respective views, serializers, etc. However, I added a new route to index all submitted resources (regardless of ownership). For this, I created a new route titled "Index All". This was tricky at first - the original URL was `experiences/all` and, as a result, my Show route (`experiences/<int:pk>`) was getting triggered but I was able to fix this by changing the URL to `experiences-all`.

As I'm looking to move forward with an Index All route, I wanted to make sure I was able to show ownership by the user's email as opposed to their respective ID. To do this, I created a new serializer that called upon the User model's `str` representation for the Index All route.


## ERD

![ERD](https://i.imgur.com/2gFsrCQ.png)

## Future of Queens Habit

I'd love to move forward with a comments section some time down the line! Always open to feedback as well so feel free to ping me with any cool ideas. :)