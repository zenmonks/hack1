# hack1
## How to contribute

1. Fork the repo

2. Get the URL from USER/hack1 repo

3. [Install Python3](https://www.python.org/downloads/). 
   <br> 3.1. pip install, 
   <br> 3.2. venv install : `install python3-venv`

4. Open terminal & write ` git clone <URL>`

5. Create branch : `git checkout -b <branch_name>`

6. Setup virtual environment :
    <br> 5.1. create venv : `python3 -m venv venv`
    <br> 5.2. activate venv 
       <br> windows : `venv/Scripts/activate`

   <br> linux/macos : ` source venv/bin/activate`

7. Install Django 
   <br>  6.1. pip install django
   <br>  6.2. `sudo apt install python3-django`

8. Make chages

9. Update the repo :  `git pull origin main`

10. Stage the changes : `git add .`

11. Add commit message : `git commit -m "message"`

12. Push those changes : `git push origin <branch_name>`

13. Make PR

## How to revert changes

1. `git revert <commit_id>`

2. Make those necessary changes

3. Stage those changes

4. Add commit message

5. Push it

6. Make PR

## How to update your local branch 
` git pull origin main`


