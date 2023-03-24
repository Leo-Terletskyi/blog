### Briefly about the project:
* registered users can add their articles.
* possibility to sort articles by categories.
* search for articles by title or content.
* for editing in the admin and on the site, a ckeditor is connected

### How to run:
1. you must have [python](https://www.python.org/) version>=3.8 and [pip](https://pip.pypa.io/en/stable/)(package installer for Python) installed
2. clone the repository and move to it
  * ```git clone https://github.com/Leo-Terletskyi/blog.git```
  * ```cd blog/```
3. create and activate the virtual environment
  * ```python3 -m venv venv```
  * if you use Linux os:
  * ```source venv/bin/activate```
  * if you use Windows:
  * ```.\venv\Scripts\activate```
4. install the required packages for the project:
  * ```pip install -r requirements.txt```
5. go to the project folder and run it:
  * ```cd blog/```
  * ```python manage.py runserver```
##### if you see something like this:
  * ```System check identified no issues (0 silenced).
       March 24, 2023 - 06:43:33
       Django version 4.1.7, using settings 'config.settings'
       Starting development server at http://127.0.0.1:8000/
       Quit the server with CONTROL-C.``` 
  * then everything is fine.
  * follow the http://127.0.0.1:8000/ link in your browser.
