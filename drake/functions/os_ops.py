import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ayakha\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def  open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
open_camera()

def open_notepad():
    os.startfile(paths['notepad'])
    
open_notepad()

def open_discord():
    os.startfile(paths['discord'])
    
    
open_discord()
    
def open_cmd():
    os.system('start cmd')

open_cmd()    

def open_calculator():
    sp.Popen(paths['calculator'])
    
open_calculator()