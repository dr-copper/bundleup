# Overview

Bundle Up! is a Python-based upload portal that allows clients to conveniently submit diagnostic bundles (.tgz only) with the relevant configs & logs. 

Created with Python 3.9.1 & Flask 2.0.1

## Installation & Setup

This project is built on a Flask, a simple but extensible microframework that provides robust API support, rapid scalability, and easy functionality. [Flask Documentation] https://flask.palletsprojects.com/en/2.0.x/installation/

A virtual environment should be created to manage the dependencies of the project in both development and production. This ensures that Python libraries will not mix versions and therefore break environment compatability. 
Use the included **venv** module to create virtual environments: 

```bash
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

Then be sure to activate the corresponding environment:

```bash
$ . venv/bin/activate
```

The shell will then update to show the name of the activated environment. After activation, use the following command to install Flask via pip:

```bash
$ pip install Flask
```

After the installation is complete, use the flask command to run the application: 

```bash
$ flask run
```

If installed and setup correctly, your terminal should show the app running: 

```bash
 * Running on http://127.0.0.1:5000/
```

You should now be able to navigate to http://127.0.0.1:5000/ and view the app.

## Context



## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Approach



## Roadmap
![alt text](./app_map)


## Credits
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
