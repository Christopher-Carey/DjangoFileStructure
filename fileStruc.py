import shutil
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
    cwd = os.path.dirname(os.path.realpath(__file__))
    print (cwd)
    os.chdir(path)
    projectName= projectNamegui.value
    os.system("django-admin startproject " +projectName)
    # ------MAKE APP---------
    time.sleep(5)


    os.remove(path + projectName+"/"+projectName+"/urls.py")
    shutil.copy2(cwd+'/prourls.py', projectName+"/"+projectName+"/urls.py")
    # shutil.copy2(r'\Users\ccare\Documents\Coding\GIT\DjangoFileStructure\prourls.py', projectName+"/"+projectName+"/urls.py")

    os.chdir(path + projectName)
    os.system("mkdir apps")
    os.chdir(path+projectName+"/apps")
    appName=appNamegui.value
    os.system("python ../manage.py startapp "+appName) 
    # ------MAKE FILE STRUCTURE---------
    os.chdir(path+projectName+"/apps/"+appName)


    shutil.copy2(cwd+'/appurls.py', path+projectName+"/apps/"+appName+"/urls.py")
    os.remove(path+projectName+"/apps/"+appName+"/views.py")
    shutil.copy2(cwd+'/views.py', path+projectName+"/apps/"+appName+"/views.py")


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
    # --static folder--
    os.chdir(path+projectName+"/apps/"+appName+"/static")
    os.system("mkdir "+appName)
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName)
    os.system("mkdir css")
    os.system("mkdir js")
    os.system("mkdir images")
    # --static subfolders--
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName+"/css")
    shutil.copy2(cwd+'/style.css', path+projectName+"/apps/"+appName+"/static/"+appName+"/css/style.css")

    # os.system("type nul > style.css")
    os.system("cd..")
    os.chdir(path+projectName+"/apps/"+appName+"/static/"+appName+"/js")
    os.system("type nul > script.js")
    activity.value="=========ALL DONE==========="
    app.update()
    print("=========ALL DONE===========")
    time.sleep(2)
    activity.value="=========OPENING VSCODE==========="
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



