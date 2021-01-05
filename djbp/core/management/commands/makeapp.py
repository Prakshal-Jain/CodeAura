import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "creates an app in specified directory and adds it to my settings"

    #  arguments
    def add_arguments(self, parser):
        parser.add_argument(
            "appdir",
            type=str,
            nargs="+",
            help="The dir of app in . form",
        )

    def getprojectname(self, splitat, endsWith, string):
        for i in string.split(splitat):
            if i.endswith(endsWith):
                return i.split(".")[0]
        return ""

    def directoryexists(self, path):
        if os.system(f"cd {path} 2>/dev/null") == 0:
            return True
        return False

    #  all the logic is handeled by handler
    def handle(self, *args, **kwargs):
        #  get arguments
        app_dir_dot = kwargs["appdir"][0]
        app_dir_sl = app_dir_dot.replace(".", "/")
        if self.directoryexists(app_dir_sl):
            self.stdout.write(
                self.style.ERROR(
                    "app or directory already exists with the name %s" % app_dir_dot)
            )
            return
        app_name = app_dir_dot.split(".")[-1]
        os.system(
            f"mkdir -p {app_dir_sl} && python manage.py startapp {app_name} {app_dir_sl}")
        # write the app in settings
        with open("manage.py", "r") as file:
            filedata = file.read()
        prj_name = self.getprojectname("'", ".settings", filedata)
        if prj_name == "":
            msg = (f"successfully created the app {app_name} with path {app_dir_dot} but \
            failed to add it to installed_apps in settings.\nIt is due to django settings not found")
            self.stdout.write(
                self.style.ERROR(msg)
            )
            return
        path_settings = f"{prj_name}/settings.py"
        if not os.path.exists(os.path.join(os.getcwd(), path_settings)):
            print("default path not there so sub")
            path_settings = f"{prj_name}/settings/base.py"
        if not os.path.exists(os.path.join(os.getcwd(), path_settings)):
            msg = (f"successfully created the app {app_name} with path {app_dir_dot} but \
            failed to add it to installed_apps in settings.\nIt is due to unusual path of django settings")
            self.stdout.write(
                self.style.ERROR(msg)
            )
            return
        with open(path_settings, "r") as file:
            filedata = file.read()
        filedata = filedata.replace(
            "# autoaddhere", f"\"{app_dir_dot}\",\n\t# autoaddhere")
        if not app_dir_dot in filedata:
            msg = (f"successfully created the app {app_name} with path {app_dir_dot} but \
            failed to add it to installed_apps in settings.\nIt is due to '# autoaddhere' not found in installed_apps in django settings")
            self.stdout.write(
                self.style.ERROR(msg)
            )
            return
        with open(path_settings, "w") as file:
            file.write(filedata)
        msg = f"successfully created the app {app_name} with path {app_dir_dot} and added it to installed_apps in django settings"
        self.stdout.write(
            self.style.SUCCESS(msg)
        )
