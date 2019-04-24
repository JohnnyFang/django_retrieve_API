Django Review App
=================
**A Django simple restful API to submit/retrieve reviews**   


App Setup
=====
Python 3 is mandatory!  
First create a virtual environment  and call it something like *retr-venv*   
more info on how to do that [here](https://docs.python.org/3/library/venv.html)   

from the command line, type (make sure your virtual environment is activated)
```
git clone https://github.com/JohnnyFang/django_retrieve_API
pip install -r requirements.txt
python manage.py migrate
```
   
Data Setup
====
After running the commands in the previous section, type:   
   
```
python populate.py
```
   
populate will create:  
* 3 users (1 admin, 2 regular users)  
* 2 reviews for each regular users   

Running the App local
====
```

python manage.py runserver 8080
```

API endpoints
=============
**Create new user**  
POST ```api/core/user/  ```   
fields(keys): *name, email, password*  

```shell
curl --data "name=John&email=JohnSnow@got.co&password=IKnowNothing" http://127.0.0.1:8000/api/core/user/

```

**Create a new auth token for user**   
POST ```/api/core/token/```  
fields(keys): *email,password*  

```shell
curl --data "email=JohnSnow@got.co&password=IKnowNothing" http://127.0.0.1:8000/api/core/token/

```

**Retrieve user reviews**
GET ```/api/reviews/```   
Authorization (header)

```shell
curl -H "Authorization: Token de440216cc90a6d68498938923c0594093f0242c" http://127.0.0.1:8000/api/reviews/

```
example  
```Authorization  Token de440216cc90a6d68400038923c0594093f0242c   ```

**Submit a review**   
POST ```/api/reviews/```  
fields: *title, rating, company, summary*  
Authorization (header)

```shell
 curl -H "Authorization: Token b56fb64cec2287a8e27214c1b6f6a1281b227a83" --data "title=TLJ review&rating=1&company=My Own&summary=Garbage!" http://127.0.0.1:8000/api/reviews/

```
Other
===
**Running Tests**  
in the root directory type:  
```pytest```   
under htmlcov look for index.html for coverage report   

**User IP address**  
Django IPWare is used to retrieve the client's IP address.[here](https://github.com/un33k/django-ipware)