## Hello, World!
#### Using the Pyramid 1.5 web development framework (and Python 3.4)
#### By Cory Spitzer
###### July 2015

#### Setup:

  ###### Installation:
  * Install virtualenv:
    * `easy_install virtualenv` or `sudo easy_install virtualenv` if you get a permissions error
    * `export VENV=~/env`
    * `virtualenv $VENV`
  * Install Pyramid Into the Virtual Python Environment:
    * `$VENV/bin/easy_install "pyramid==1.5.7"`
  * For detailed instructions see docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html#installing-chapter

  ###### Running the program:
  * Start the server using the python installed in the virtualenv with
    `$VENV/bin/python helloworld.py`
  * Point a browser to `localhost:8080/hello/world`
  * Enjoy!
