# django-boiler-plate

- use rename command
- update package.json
  - update name, description, author, url, homepage
- rename vscode to .vscode
  - add pipenv path from `pipenv --venv`

# custom commands
These commands are used like normal django commands like `python manage.py <command>`
### makeapp
+ makeas and app with the directory (<folder>.<folder>...<app>) 
+ adds it to installed_apps in the django settings
+ eg -> `python manage.py makeapp egapp apps.egapp`
+ eg -> `python manage.py makeapp egapp apps.main.egapp`

### rename 
+ use this command to rename your project 
+ eg -> `python manage.py rename djbp newname`

###  makesuper
+ this command make a super user useful when 
  + you clone a repositor and start new
  + when you delete database and run make migrations
+ eg -> `python manage.py makesuper`
+ before use it is recomended to 
  + change superuser credentials in `djbp/core/management/commands/makesuper.py`
  + use environment variables for superuser credentials to avoid pushing sensitive info in remote repository
