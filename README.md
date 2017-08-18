<h2>Poem Generator<h2>

Scrape poems of Cavafy by runnning the cavafySc.py file, and generate the json file.

Start a mongo instance, and import the json file into a collection using the command:
$ mongoimport --db poems --collection cavf --file cav.json --jsonArray

Keep the mongod instance running.

Start the Flask server by using the commands:
$ set FLASK_APP=app.py
$ flask run

Your server should be running on localhost:5000
