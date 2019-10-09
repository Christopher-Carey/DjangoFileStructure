import os
import time

def makeStruc()
    # ------MAKE PROJECT---------
    path="/Users/ccare/Documents/Coding/Coding Dojo/weekThree/Python/python_stack/django/django_intro/"
    os.chdir(path)
    projectName= input("enter name")
    os.system("django-admin startproject " +projectName)
    # ------MAKE PROJECT---------

