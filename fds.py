#!/usr/bin/python3
import os
import time
import webbrowser
senha = input("KEY: ? ")
if senha < "67":
    print("KEY INCORRETA")
    exit ()
elif senha == "68":
    print ("")

print("LOADING...")
time.sleep(2)
os.system("clear")
os.system("sl")
time.sleep(3)


print("█▀▄▀█ █▀▀ █▄░█ █░█")
print("█░▀░█ ██▄ █░▀█ █▄█")

print("█▀▀ █▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄ █▀█ █▀")
print("█▄▄ █▄█ █░▀░█ █▀█ █░▀█ █▄▀ █▄█ ▄█")
print("")

print ("1: NANO EDITOR")
print ("2: CMATRIX")
print ("3: INSTALAR CMATRIX")
print ("4: LIMPAR LINHA")
print ("5: FECHAR ABA")
print ("     ")

escolha = False

while escolha == False:
    nivel = int(input("QUAL OPÇÃO: "))
    
    if (nivel == 1):
        os.system("nano")
    
    elif (nivel == 2):
        os.system("cmatrix")
    
    elif (nivel == 3):
        os.system("pkg install cmatrix")
    elif (nivel == 4):
        os.system("clear")
    
    elif (nivel == 5):
        os.system("exit")
