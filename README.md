<h2>Poem Generator</h2>

This is a small project which pops up a new Cavafy poem everytime you reload the page.

<h4>Setting up the project:</h4>
Scrape poems of Cavafy by runnning the cavafySc.py file, and generate the json file.</br>

Start a mongo instance, and import the json file into a collection using the command:</br>
$ mongoimport --db poems --collection cavf --file cav.json --jsonArray

Keep the mongod instance running.

Start the Flask server by using the commands:</br>
$ set FLASK_APP=app.py</br>
$ flask run

Your server should be running on localhost:5000
