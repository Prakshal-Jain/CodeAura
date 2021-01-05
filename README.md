# Django boiler plate

This is a ready to use django project. 

If you do not find something you want to know in this file or any issues, please let me know. My Email is harjotbarn99@gmail.com

**If you find my repository useful please send me an email to let me know if someone is using it, not necessary but appereciated. **

#### features

- different settings for production and development
- debug toolbar
- custom commands



# Use checklist

- [ ] run virtual environment (First) `pipenv install --dev`

- [ ] rename the project see [Custom commands: rename](#rename)
- [ ] [build static files](#Handling static files)
- [ ] run migrations
- [ ] change details in package.json (find the --change and --add in the file)
- [ ] run app (Last)



# Custom commands
These commands are used like normal django commands like `python manage.py <command>`
### makeapp
+ makeas and app with the directory (<folder>.<folder>...<app>) 
+ adds it to installed_apps in the django settings
+ eg -> `python manage.py makeapp egapp apps.egapp`
+ eg -> `python manage.py makeapp egapp apps.main.egapp`
+ do not remove the `# autoaddhere` in `djbp/settings/base.py` , this is used by command to add the app in setting

### rename 
+ use this command to rename your project 
+ eg -> `python manage.py rename djbp newname`
+ eg -> `python manage.py rename oldname newname`

###  makesuper
+ this command make a super user useful when 
  + you clone a repositor and start new
  + when you delete database and run make migrations
+ eg -> `python manage.py makesuper`
+ before use it is recomended to 
  + change superuser credentials in `djbp/core/management/commands/makesuper.py`
  + use environment variables for superuser credentials to avoid pushing sensitive info in remote repository
  
  

# Handling static files
Put all static files in folder static/<folder>

- First install node modules by `npm install`

- Before starting the app ren the command `npm run build` to build static files into static/dist

  

To get a static file use `{% static '<folder>/<file>' %}` as url also remember to use the `{% load static %}`

If you are modifying static files such as .js or .css the use `npm run watch` to automatically load changed static files




# Debug toolbar
+ to hide debug toolbar go to `djbp/settings/dev.py` and find the function show_toolbar and make it return False



# Useful info

- add apps to `djbp/settings/base.py` if not using my custom 
- be careful while naming css and scss files `app.scss` compiles to `app.css` so be careful not to name a css file same as scss



