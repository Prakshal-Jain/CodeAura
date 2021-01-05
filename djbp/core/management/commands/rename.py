import os
from django.core.management.base import BaseCommand

# I learned this code from a youtube tutorial
# and modified a little
class Command(BaseCommand):
    help = "Renames a Django project"

    #  arguments
    def add_arguments(self, parser):
        parser.add_argument(
            "current",
            type=str,
            nargs="+",
            help="The current Django project folder name",
        )
        parser.add_argument(
            "new", type=str, nargs="+", help="The new Django project name"
        )

    #  all the logic is handeled by handler
    def handle(self, *args, **kwargs):
        #  get arguments
        current_project_name = kwargs["current"][0]
        new_project_name = kwargs["new"][0]
        print("\n\n", current_project_name, new_project_name, "\n\n")
        # logic for renaming the files

        # add name to this array which maight cause problems for
        # renaming as BASE is used in variable name and can cause
        # those varibles to be renamed.
        forbidden_names = [
            "BASE",
        ]
        if current_project_name in forbidden_names:
            self.stdout.write(
                self.style.ERROR(
                    "Project cannot been renamed to %s, please use another name."
                    % new_project_name
                )
            )
            return

        # files to check for renaming
        files_to_rename = [
            f"{current_project_name}/settings/base.py",
            f"{current_project_name}/wsgi.py",
            "manage.py",
        ]

        for f in files_to_rename:
            with open(f, "r") as file:
                filedata = file.read()

            filedata = filedata.replace(current_project_name, new_project_name)

            with open(f, "w") as file:
                file.write(filedata)

        os.rename(current_project_name, new_project_name)

        self.stdout.write(
            self.style.SUCCESS("Project has been renamed to %s" % new_project_name)
        )

