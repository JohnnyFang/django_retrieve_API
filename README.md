
Create new user
POST api/core/create/user/
name  
email  
password  

Create a new auth token for user   
GET /api/core/create/token/
email  
password  

Retrieve user reviews
GET /api/reviews/
Authorization (header)

example  
Authorization  Token de440216cc90a6d68400038923c0594093f0242c   

Submit a review   
/api/reviews/
title  
rating  
company  
summary  
Authorization (header)