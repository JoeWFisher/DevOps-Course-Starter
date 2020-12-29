# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses poetry to manage package dependencies.
This can be setup using:
``` bash
     $ poetry install
```

This project uses flask env variables for the Trello API
These need to be added to a .env file and include:
```
    * Key
    * TOKEN
    * BoardID
    * ToDoId (List Id)
    * DoingId (List Id)
    * DoneId (List Id)
```

This project also uses Docker
Docker production and development containers can be built using:
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

prod:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
dev:
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
