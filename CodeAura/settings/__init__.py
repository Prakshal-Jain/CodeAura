#  To use an environment variable to automatically switch between prod and dev settings
#       set an environment variable PRODUCTION="False" for dev settings
#       I use this so all my apps are in dev mode on my machine 
#              but in production they are in production without me modifying this

# import os
# if (os.environ.get("PRODUCTION") == "False"):
#     print("this is development------------------------------------------ ")
#     from .dev import *
# else:
#     print("this is production------------------------------------------- ")
#     from .prod import *


#  if you are unfamiliar with environment variables then you can swith manually 
#    by changing .dev to .prod for production environment

from .dev import *