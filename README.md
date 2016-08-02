```
npm install
pip install -r requirements.txt
./manage.py migrate
./manage.py runscript reset_fixtures
./manage.py runserver_plus
```
then go to url `localhost:8000/admin/auth/user/` and hijack a student or professor User
