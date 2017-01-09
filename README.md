# Website

The Ranobe-Honyaku website source code.

# Installation

### Prerequisites

* Python 3
* PostgreSQL


### Clone and set up virtualenv
`This setup is for an ubuntu server running Xenial 16.04. Any other setup may vary.`
```shell
git clone https://github.com/Ranobe-Honyaku/Website.git

cd Website

python3 -m pip install virtualenv

python3 -m virtualenv env

source venv/bin/activate

pip install -r requirements.txt

cp setup_example.json config.json
```

To be able to use our database, we'll actually need to install it.
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```
Now we've done this we need to create a new role.
```shell
sudo -u postgres createuser --interactive
```
That should guide you through the process of creating your user. When it asks you for the `name` make sure to use the one of your superuser account, this is because postgres will allow you to sign in as the postgres role on that account.

Now that we've created our user we're at the problem that we have no database to use. So let's create one.
```shell
sudo -u postgres createdb database_name
```

I'd recommend setting your database name as the same name as the `user` you just made, which should have the same name as your linux account.


At this point, open config.json. You will probably need to change
`SQLALCHEMY_DATABASE_URI` to the path of your local database, provide login
credentials, etc. Try this string format:

```
"postgresql://username:password@host:port/database"
```

Host is going to be your ip or the server you're setting it up on, and the port by default is going to be `5432`

### Run migrations on the database

```python3 manage.py db upgrade```

This applies migrations in the `migrations/` directory to your local database.
Typically you will need to perform this whenever the schema in your database
does not match the schema defined in `models/`.

To make migrations, you can run `manage.py db migrate`, but you won't need to
do this right after `git pull/fetch`. You will need to make migrations when
you change the model yourself though. Please remember to comment the migrations
in `/migrations/versions/`.

### Load database and set the tables up

You will only need to do this if this is your first time setting up the
database (or if you dropped/deleted the database previously).

```shell
python3 manage.py setup
```

Follow the on-screen instructions. The current roles available are `admin` and `staff`

### Run the actual server

```shell
python3 manage.py runserver
```

Note that this set of instructions is for a development configuration only.
