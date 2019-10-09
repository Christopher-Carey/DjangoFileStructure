import os
import time

def makeStruc():
    # ------MAKE PROJECT---------
    path="/Users/ccare/Documents/Coding/Coding Dojo/weekThree/Python/python_stack/django/django_intro/"
    os.chdir(path)
    projectName= input("enter name")
    os.system("django-admin startproject " +projectName)
    # ------MAKE APP---------
    time.sleep(5)
    os.chdir(path+projectName)
    os.system("mkdir apps")
    os.chdir(path+projectName+"/apps")
    appName=input("App Name")
    os.system("python ../manage.py startapp "+appName) 
    # ------MAKE FILE STRUCTURE---------
    os.chdir(path+projectName+"/apps/"+appName)
    os.system("type nul > urls.py")
    os.system("mkdir templates")
    os.system("mkdir static")
    # --templates folder--
    os.chdir(path+projectName+"/apps/"+appName+"/templates")
    os.system("mkdir "+appName)
    os.chdir(path+projectName+"/apps/"+appName+"/templates/"+appName)
    os.system("type nul > index.html")
    os.system("cd..")
    os.system("cd..")
    # --static folder--
    os.chdir(path+projectName+"/apps/"+appName+"/static")
    os.system("mkdir "+appName)
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName)
    os.system("mkdir css")
    os.system("mkdir js")
    os.system("mkdir images")
    # --static subfolders--
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName+"/css")
    os.system("type nul > style.css")
    os.system("cd..")
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName+"/js")
    os.system("type nul > script.js")
    print("========ALL DONE===========")
makeStruc()



