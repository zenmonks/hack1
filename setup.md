## How to contribute

1. Fork the repo

2. Get the URL from USER/hack1 repo

3. [Install Python3](https://www.python.org/downloads/). 
   <br>3.1. pip install, 
   <br>3.2. venv install.

4. Open terminal & write ` git clone <URL>`

5. Create branch : `git checkout -b <branch_name>`

5. Setup virtual environment :
    <br> 5.1. create venv : `python3 -m venv venv`
    <br> 5.2. activate venv 

6. Install Django 
   <br>  6.1. pip install django
   <br>  6.2. `sudo apt install python3-django`

7. Make chages

8. Update the repo :  `git pull origin main`

9. Stage the changes : `git add .`

10. Add commit message : `git commit -m "message"`

11. Push those changes : `git push origin <branch_name>`

12. Make PR

## How to revert changes

1. `git revert <commit_id>`

2. Make those necessary changes

3. Stage those changes

4. Add commit message

5. Push it

6. Make PR
