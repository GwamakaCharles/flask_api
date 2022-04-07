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

READ:

GET users list - {{url}}/users

url :
"https://quiet-anchorage-71805.herokuapp.com/"
