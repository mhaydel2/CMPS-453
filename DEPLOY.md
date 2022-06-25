## Set up GitLab continuous delivery

We will use GitLab CI/CD for continuous deployment on Heroku which is a platform as a service
that enables developers to build, run, and operate application entirely on cloud.

### Create an account on Heroku
(skip this if you already have an account on Heroku)
To start using Heroku you will first need to create an account:

1. Go to https://www.heroku.com and click the `SIGN UP FOR FREE` button.
2. Enter your details and then press `CREATE FREE ACCOUNT`.
    You'll be asked to check your account for a sign-up email.
3. Click the account activation link in the signup email.
    You'll be taken back to your account on the web browser.
4. Enter your password and click `SET PASSWORD AND LOGIN`.
5. You'll then be logged in and taken to the Heroku dashboard: https://dashboard.heroku.com/apps.

To view the `API Key` of your account, visit `Account Settings` and click on the `Reveal` button.

![Account API Key](docs/imgs/account_api_key.png)

### Create an app on Heroku
On your Heroku account, click on `New` > `Create new app`, name it `453-spring-2021-team-<X>` where `<X>` can be [a, b, c, d,...].

![Staging app](docs/imgs/create_app.png)

### Set up GitLab CD variables
On your GitLab project repository, visit `settings` > `CI/CD`, and click on `Expand` button of the `Variables`.

Add the below two variables and uncheck masked and protected flags:
1. Key: `HEROKU_API_KEY`, Value: `API key` from Heroku `Account Settings`
2. Key: `HEROKU_APP_STAGING`, Value: `453-spring-2021-team-<X>` name of the app that you have created on Heroku.

![CD Variables](docs/imgs/cd-variables.png)

### Edit django project settings

In the file, `django_project\settings.py`, you will see the list `ALLOWED_HOSTS`:

```
ALLOWED_HOSTS = [
    '127.0.0.1', 'localhost',
    # Change the below line to '453-spring-2021-team-<X>.herokuapp.com'
    'cmps-453-project-template.herokuapp.com'  # comment this line
]
```

Include a list element to the `ALLOWED_HOSTS` that matches the name of the staging app
that you have created on Heroku like this: `453-spring-2021-team-<X>.herokuapp.com`.

All the web apps registered on Heroku are registered under the domain `.herokuapp.com`.

### Push changes to GitLab
Create a new commit for the changes in the `.gitlab-ci.yml` and `django_project\settings.py`,
and push the changes to the origin.

On your GitLab project repository, visit CI/CD > Pipelines and check the progress of the `staging` stage in the pipeline.

![Staging pipeline](docs/imgs/pipeline-staging.png)
