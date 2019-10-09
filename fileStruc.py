import os,sys
import time
# ----------------GUI-----------------
from guizero import App, Text, TextBox, PushButton,CheckBox
app = App(layout="grid",width=500)
pathdir = TextBox(app,width=75,text="enter directory", align="left",grid=[0,0])
projectNamegui = TextBox(app,width=75,text="enter project name", align="left",grid=[0,2])
appNamegui = TextBox(app,width=75,text="enter app name", align="left",grid=[0,4])
windows = CheckBox(app, text="Check for Windows", align="left",grid=[0,9])
mac = CheckBox(app, text="Check for Mac", align="left",grid=[0,10])
activity = Text(app,width=75, align="left",text="Activity Here",grid=[0,11])
# ----------------GUI-----------------

# -----hope to separate into diffrent functions---
# path=pathdir.value
# projectName= projectNamegui.value
# appName=appNamegui.value

# def makeProject():
# def makeApp():
# def makeAppStruc():
# def runProject():
# def runApp():
# -----hope to separate into diffrent functions---




def makeStruc():
    # ------MAKE PROJECT---------
    path=pathdir.value
    # path="/Users/ccare/Documents/Coding/Coding Dojo/weekThree/Python/python_stack/django/django_intro/"
    os.chdir(path)
    projectName= projectNamegui.value
    os.system("django-admin startproject " +projectName)
    # ------MAKE APP---------
    time.sleep(5)
    os.chdir(path + projectName)
    
# --------------------write to file---------------------------
    # os.chdir(path + projectName + "/" + projectName)
    # fd = os.open("urls.py",os.O_RDWR)
    # # Writing text
    # os.write(fd,"This is test".encode())
    # os.close( fd )
# --------------------write to file---------------------------

    os.system("mkdir apps")
    os.chdir(path+projectName+"/apps")
    appName=appNamegui.value
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
    activity.value="=========ALL DONE==========="
    print("=========ALL DONE===========")
    os.chdir(path+projectName)
    os.system("code .")
    print("=========ALL DONE===========")
# makeStruc()

# ------------GUI-----------------
runpro = PushButton(app ,command=makeStruc,text="run program", align="left",grid=[0,8])
# runpro = PushButton(app ,command=runProject,text="run program", align="left",grid=[0,8])
# runapp = PushButton(app ,command=runApp,text="run app", align="left",grid=[0,9])
app.display()



