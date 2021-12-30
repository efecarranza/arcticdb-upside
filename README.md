# Set Up

1. Clone repo
2. Create a virtual environment `python3 -m venv venv`
3. Activate venv `source venv/bin/activate`
4. Install libraries `pip install -r requirements.txt`
5. Create FLASK_APP env variable `export FLASK_APP=application.wsgi:app
6. Export `USERNAME`, `URL`, and `PASSWORD` with Upside specific data.
7. Have MongoDB installed (ArcticDB uses MongoDB)
8. Run the application: `flask run`
9. Visit `http://127.0.0.1:5000/api/v1/prices/PEACHS` (or any other song ID in the URL) for a JSON response with latest bid/ask.

# How It Works

This is a very light API that is just utilizing one endpoint to retrieve some data so I utilized the Flask framework as it's a lightweight framework for quick application development. Not much else was needed to do this so I went with something that would allow for quick development that has a proven track record.
Because of nature of the data we are using, I thought Python would be the ideal language as it has a lot of libraries for dealing with series of data. It's quite used in the financial world because of pandas and numpy and Upside songs are securities.
ArcticDB is has very fast read/write and for the type of operations and how fast we'd be dealing with it, I thought it was better than a SQL approach. Here, we are just adding the latest entry really quickly to the DB and fetching the data. With how many write operations we could potentially be doing, we might not want to write to the DB for every entry but for the purposes of a demonstration this should suffice.
