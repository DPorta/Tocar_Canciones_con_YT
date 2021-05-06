import pyautogui as pg
import webbrowser as web
import time

#API PARA ENVIAR MENSAJES
yt_link="https://www.youtube.com/watch?v=xa17zHJhNhA"

#Notas
do='1'
re='2'
mi='3'
fa='4'
sol='5'
la='6'
si='7'
doMayor='8'
reMayor='9'
miMayor='0'

#Funcion para abrir link
def open(yt):
    web.open(yt)
    time.sleep(5)

#Funcion enviar
def press(nota, seg):
    pg.press(nota)
    time.sleep(seg)

#Cancion_puee ser cualquiera
def avengers():
    press(re, 1)
    press(re, 0.5)
    press(re, 1)
    press(la, 0.5)
    press(sol, 1)
    press(fa, 1)
    press(mi, 1)
    press(re, 1)
    press(re, 0.5)
    press(re, 1)
    press(la, 0.5)
    press(si, 1)
    press(sol, 1)
    press(la, 1)
#MAIN
if __name__ == "__main__":
    open(yt_link)
    avengers()
else:
    print("Hubo un error, revisa el codigo.")