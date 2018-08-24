# Simple Endpoint Demonstration

A simple Flask-based program to demonstrate responding to GET and POST requests
on a single HTTP endpoint with varying behavior if the Accept header is set to
'application/json' for GET requests.

## Installation instructions

### Environment Assumptions

* Linux environment
* Python2 executable installed at /usr/bin/python2
* Pip installed
* virtualenv installed
* curl installed

### 1. Setup

In a Linux terminal in the writable directory of your choice, please run the
following commands:

1. ```git clone https://github.com/carterandrew/simple-endpoint.git```
2. ```cd simple-endpoint```
3. ```virtualenv venv```
4. ```source venv/bin/activate```
5. ```pip install --upgrade pip```
6. ```pip install -r requirements.txt```

### 2. Running the webserver

Once you have completed the setup steps, you can start the flask server (in the
same terminal) with:

```python http_server.py```

At this point the server should be running and the output will look something
like:

```
* Serving Flask app "http_server" (lazy loading)
* Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Please open a second terminal window/tab to continue. Once you have that open,
please switch to it and continue with step 3.

### 3. Testing behavior with curl

In this section you'll test the behavior of the Flask app using curl. Please
note that all requests to the '/' endpoint will be logged to the file
```debug.log``` in the simple-endpoint directory.

##### GET with no Accept header set

First, run the following command to verify that calling the '/' endpoint
without the Accept: application/json header set returns
```<p>Hello, World</p>```:

```curl -H accept: localhost:5000```

Verify that  ```<p>Hello, World</p>``` is output.

##### GET with Accept: application/json set
Next, let's verify that setting the Accept: application/json header changes
the output:

```curl -H accept:application/json localhost:5000```

Verify that ```{"message":"Good morning"}``` is output.

##### POST

Finally, let's verify that using the POST method outputs 
```<p>Hello, World</p>```:

```curl -X POST localhost:5000```


### 4. Check the debug log

The file ```debug.log``` in the simple-endpoint directory logs the timestamp and
the request url for all GET and POST requests to the '/' endpoint. You can view
its contents by running:

```cat debug.log```

### 5. Running unit tests

Please switch to the terminal where the Flask application is running and
terminate it with ```<ctrl>-c```. In the same terminal, please run the following
command to execute the unit tests:

```python http_server_test.py```

Please ensure that the output is similar to:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```

### 5. Cleanup

To return to your normal environment, please run: ```deactivate``` from the
terminal you ran the tests from.