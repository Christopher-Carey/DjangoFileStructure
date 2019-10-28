import shutil
import os,sys
import time
# ----------------GUI-----------------
from guizero import App, Text, TextBox, PushButton,CheckBox
app = App(layout="grid",width=500)
pathdir = TextBox(app,width=60,text="enter directory", align="left",grid=[0,0])
projectNamegui = TextBox(app,width=60,text="enter project name", align="left",grid=[0,2])
appNamegui = TextBox(app,width=60,text="enter app name", align="left",grid=[0,4])
windows = CheckBox(app, text="Check for Windows", align="left",grid=[0,9])
mac = CheckBox(app, text="Check for Mac", align="left",grid=[0,10])
activity = TextBox(app,height=25, multiline=True,width=60, align="left",text="Activity Here",grid=[0,11])
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
    activity.value=activity.value+"=========START==========="
    print("=========START===========")
    # ------MAKE PROJECT---------
    path=pathdir.value
    cwd = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    projectName= projectNamegui.value
    os.system("django-admin startproject " +projectName)
    activity.value=activity.value+"Made Project"
    app.update()
    # ------MAKE APP---------
    time.sleep(2)
    os.remove(path + projectName+"/"+projectName+"/urls.py")
    shutil.copy2(cwd+'/prourls.py', projectName+"/"+projectName+"/urls.py")
    # shutil.copy2(r'\Users\ccare\Documents\Coding\GIT\DjangoFileStructure\prourls.py', projectName+"/"+projectName+"/urls.py")
    os.chdir(path + projectName)
    os.system("mkdir apps")
    os.chdir(path+projectName+"/apps")
    appName=appNamegui.value
    os.system("python ../manage.py startapp "+appName) 
    activity.value=activity.value+"Made App"
    app.update()
    activity.value=activity.value+"Made Project Level URL"
    app.update()
    time.sleep(1)
    # ------MAKE FILE STRUCTURE---------
    os.chdir(path+projectName+"/apps/"+appName)
    shutil.copy2(cwd+'/appurls.py', path+projectName+"/apps/"+appName+"/urls.py")
    os.remove(path+projectName+"/apps/"+appName+"/views.py")
    shutil.copy2(cwd+'/views.py', path+projectName+"/apps/"+appName+"/views.py")
    activity.value=activity.value+"Made App Level URL"
    activity.value=activity.value+"Made App Level View"
    app.update()
    time.sleep(1)
    os.system("mkdir templates")
    os.system("mkdir static")
    # --templates folder--
    os.chdir(path+projectName+"/apps/"+appName+"/templates")
    os.system("mkdir "+appName)
    os.chdir(path+projectName+"/apps/"+appName+"/templates/"+appName)
    shutil.copy2(cwd+'/index.html', path+projectName+"/apps/"+appName+"/templates/"+appName+"/index.html")
    # os.system("type nul > index.html")
    os.system("cd..")
    os.system("cd..")
    activity.value=activity.value+"Make Template Folder"
    activity.value=activity.value+"Make Static Folder"
    app.update()
    activity.value=activity.value+"Made Index.html"
    app.update()
    time.sleep(1)
    # --static folder--
    os.chdir(path+projectName+"/apps/"+appName+"/static")
    os.system("mkdir "+appName)
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName)
    os.system("mkdir css")
    os.system("mkdir js")
    os.system("mkdir images")
    activity.value=activity.value+"Made CSS Folder"
    activity.value=activity.value+"Made JS Folder"
    activity.value=activity.value+"Made IMAGES Folder"
    app.update()
    time.sleep(1)
    # --static subfolders--
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName+"/css")
    shutil.copy2(cwd+'/style.css', path+projectName+"/apps/"+appName+"/static/"+appName+"/css/style.css")
    activity.value=activity.value+"Made CSS File"
    app.update()
    time.sleep(1)
    # os.system("type nul > style.css")
    os.system("cd..")
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName+"/js")
    os.system("type nul > script.js")
    activity.value=activity.value+"Made JS File"
    app.update()
    time.sleep(1)
    activity.value=activity.value+"=========ALL DONE==========="
    app.update()
    time.sleep(2)
    activity.value=activity.value+"=========OPENING VSCODE==========="
    app.update()
    time.sleep(2)
    os.chdir(path+projectName)
    os.system("code .")
    print("=========ALL DONE===========")
# makeStruc()

# ------------GUI-----------------
runpro = PushButton(app ,command=makeStruc,text="run program", align="left",grid=[0,8])
# runpro = PushButton(app ,command=runProject,text="run program", align="left",grid=[0,8])
# runapp = PushButton(app ,command=runApp,text="run app", align="left",grid=[0,9])
app.display()



