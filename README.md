## CMPS 453 Project

This is the part of the README that will contain the description of our project once we know all the details for what we want to do.

The project is deployed on Heroku: [https://sp22-team-d.herokuapp.com/](https://project-appname.herokuapp.com)

The template project is deployed on Heroku: [https://cmps-453-project-template.herokuapp.com/](https://cmps-453-project-template.herokuapp.com/)

To develop this Django application, clone this repository and follow the instructions:

## What's Already Included in the Django Template?
* User Authentication System:
    * Login: [https://cmps-453-project-template.herokuapp.com/accounts/login/](https://cmps-453-project-template.herokuapp.com/accounts/login/)
    * User Registration: [https://cmps-453-project-template.herokuapp.com/accounts/signup/](https://cmps-453-project-template.herokuapp.com/accounts/signup/)

## Install Python Requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Collect Static Files

```bash
python manage.py collectstatic --no-input
```

## Run the Django Web Server

```bash
python manage.py runserver
```

## Team Members

| Role | Last Name | First Name | Heroku App |
| ---- | --------- |  --------- | -----------|
| Member A | Dugas | Austin  | [sp22-team-d-a.herokuapp.com](update URL here) |
| Member B | Roman | Ryan  | [sp22-team-d-b.herokuapp.com](update URL here) |
| Member C | Haydel | Milan  | [sp22-team-d-c.herokuapp.com](update URL here) |
| Member D | Rivette | Caroline  | [sp22-team-d-d.herokuapp.com](update URL here) |

## Set up GitLab CD
See the [DEPLOY.md](DEPLOY.md)
