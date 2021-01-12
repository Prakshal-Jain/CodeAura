from .base import *
import os

#  this section needs a lot of details to implement so i am not leaving instructions 
#  however if you would like to learn about this section, i would be happy to 
#       help Just email at harjotbarn99@gmail.com

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ("SECRET_KEY")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": os.environ("PDB_NAME"),
#         "USER": os.environ("PDB_USER"),
#         "PASSWORD": os.environ("PDB_PASS"),
#         "HOST": "localhost",
#         "PORT": "",
#     }
# }
