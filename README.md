Django Review App
=================
**A Django simple restful API to submit/retrieve reviews**   


Setup
=====
Python 3 is mandatory!  
First create a virtual environment  and call it something like *retr-venv*   
more info on how to do that [here](https://docs.python.org/3/library/venv.html)   

from the command line, type (make sure your virtual environment is activated)
```
git clone https://github.com/JohnnyFang/django_retrieve_API
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8080
```
API endpoints
=============
**Create new user**  
POST ```api/core/user/  ```   
fields(keys): *name, email, password*  

**Create a new auth token for user**   
POST ```/api/core/token/```  
fields(keys): *email,password*  

**Retrieve user reviews**
GET ```/api/reviews/```   
Authorization (header)

example  
```Authorization  Token de440216cc90a6d68400038923c0594093f0242c   ```

**Submit a review**   
POST ```/api/reviews/```  
fields: *title, rating, company, summary*  
Authorization (header)

Other
===
**Running Tests**  
in the root directory type:  
```pytest```   
under htmlcov look for index.html for coverage report   

**User IP address**  
Django IPWare is used to retrieve the client's IP address.[here](https://github.com/un33k/django-ipware)