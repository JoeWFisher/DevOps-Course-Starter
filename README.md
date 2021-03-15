# DevOps Apprenticeship: Project Exercise

## Heroku

This app is now hosted on Heroku:

http://todoapp-joefish.herokuapp.com/

## Travis CI

This app is deloyed using Travis CI.
Builds are run on pull requests.

Tests are included in the build and are required to pass to deploy the app
## Getting started

The project uses poetry to manage package dependencies.
This can be setup using:
``` bash
     $ poetry install
```

This app can be run locally using:
``` bash
    $ poetry run flask run
```

This project uses flask env variables 
These need to be added to a .env file and include:
```
    * Mongo_Url
    * Mongo_db
```

This project also uses Docker
Docker production and development containers can be built using, with a Port argument passed in:
``` bash
    $ docker build --target development --tag todo-app:dev .
    $ docker build --target production --tag todo-app:prod .
```
Once built they can be run using:
``` bash
    $ docker run --env-file .env -p 5000:5000 todo-app:dev
    $ docker run --env-file .env -p 5000:5000 todo-app:prod
```

You should see output similar to the following depending on if you are running prod or dev:

dev:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
prod:
```bash
 * Starting gunicorn 20.0.4
 * Listening at: http://0.0.0.0:5000 (1)
 * Using worker: threads
 * Booting worker with pid: 7
 * Booting worker with pid: 8
 * Booting worker with pid: 9
 * Booting worker with pid: 10
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.
