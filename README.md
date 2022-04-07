# FlaskApi

A Flask Rest API deployed on Heroku

#### Description

The API exposes endpoints to fetch users from the database :

The 'users' table has column 'name'

### 10,000 DUMMY

insert into users (
name)
select
left(md5(i::text), 10)
from generate_series(1,10000) s(i);

#### Endpoints

url :
"https://quiet-anchorage-71805.herokuapp.com/"

READ:

<!-- Retrieve a list of users -->

GET users list - {{url}}/users

<!-- Retrieve a User by name -->

GET user by name - {{url}}/user/<name>

<!-- The API supports pagination. By default it loads the first page with 20 names i.e page=1 and per_page=20
To change page and items provide the page and per_page arguments in the request URL , like below -->

https://quiet-anchorage-71805.herokuapp.com/users?page=2&per_page=100

<!-- Retrieving 100 items from the first page -->

https://quiet-anchorage-71805.herokuapp.com/users?per_page=100

<!-- Retrieving the second page -->

https://quiet-anchorage-71805.herokuapp.com/users?page=2
