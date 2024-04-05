# SPAC9

### Assignment

The goal of this exercise was to create an endpoint, capable of handling GET and POST for a small database.

### Workflow

With only three days to work, and never having heard about endpoints before, most of day one was spent on figuring out what this actually meant.

Day two was used for creating an MySQL database for the objects.

Unfortunatly I got too fancy for my own liking, so a large amount of time was spent on how to make Nutrients a sub object of Cereal, whilst still allowing for the database to be automatically generated.

Being new to GET and POST requests, the third day was mostely spent on trying to build a web page for manually checking if things were working.
It was only when I felt stuck, and asked for help that I realized I was taking the wrong approach.
Earlier I had tried running client and server seperatly, but still from the same folder, which made me belive that Visual Studio Code couldn't run two different terminals simultaniously.
Once I figured out how to do so, the work with GET requests were fairly straighforward.
I didn't get to complete the POST requests, as the lack of time made my code sloppy and I quickly lost track of the structure.

## What does it do?

The program creates a MySQL database for the different cereals, then sets up a server for others to connect to.
Currently a user can create a GET request and get a list of all objects in the database, or create a GET request with an 'id' to get a specific object.
It's also possible to do more specific searched using '/results?' followed by the parameters. Adding 'min_' or 'max_' will convert the parameter into greater than and less than opperators.

## Installation

1. Clone the repo
2. Install requirements in 'requirements.txt'
3. Paste the CSV file of the cereals into the folder
4. Setup the parameters in 'main_server.py'
5. Run 'main_server.py'
6. Copy the server addresse from the terminal and paste it into 'main_clinet.py'
7. Run 'main_clinet.py' from a different terminal
