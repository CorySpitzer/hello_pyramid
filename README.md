## Hello, World!
#### Using the Pyramid 1.5 web development framework (and Python 3.4)
#### By Cory Spitzer
###### July 2015

#### Setup:

###### Installation:
  * Install virtualenv:
    * `easy_install virtualenv` 
      * If you get a permissions error you can try `easy_install --user virtualenv` (which will install in your home directory - use `easy_install --help` for more options) or `sudo easy_install virtualenv` if you have root permissions
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
