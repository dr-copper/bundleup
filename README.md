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

This program was completed within the specified period of time that was available to dedicate to staging, preparations, and planning to build an effective solution to the problem. Due to this limitation, the focus was to deliver a workable product that satisfied all of the necessary requirements, while being as streamlined and as intuitive as possible. 

The use of Flask was beneficial in the sense that it provides several libraries that include the functionality that was required: flash_render_template, request and jsonify were all integral components of having a working model in both code and forward stratefy. 

Assuming no environment conflicts, the program runs and satisfies all of the mandatory requirements as followed:

- Customer interface is HTTP REST API (optional) **completed**
- Customer must be able to upload very large files (required) **completed**
- Program must only accept .tgz files (required) **completed**
- Must be able to handle multiple requests concurrently (required) **completed**
- Support team must be able to list and download any uploaded files (required) **started,unfinished**
- Must not use any pre-built file upload libraries **completed**
- Minimize number of external dependencies in business logic code path **completed**
- Setup observability solution with the design goal of providing monitoring & troubleshooting capabilities **ran out of time, suggestions included**
- Setup deployment of application to AWS **started,unfinished**

## Reflection 


## Improvement Opportunities 



## Roadmap & Observability Recommendation
![Screenshot](app_map.PNG)

## Credits
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
