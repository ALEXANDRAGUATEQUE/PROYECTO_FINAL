import pygame
import random
ab=int(input("escoja la dificultad \n 1-facil \n 2-dificil \n 3-extremo"))
def cuenta():
    cuenta.numero += 100
    return cuenta.numero
cuenta.numero = 0
def propiedad_creciendo(): 
    for i in range(len(bicho)-1):#pone un rango de la serpiente
       bicho[len(bicho)-i-1].x = bicho[len(bicho)-i-2].x # ayuda a que la serpiente crezca y el puerpo lo pueda seguir
       bicho[len(bicho)-i-1].y = bicho[len(bicho)-i-2].y # ayuda a que la serpiente crezca y el puerpo lo pueda seguir
class serpiente:
    def __init__(cuerpo1_0   , raza):#inicializa atributos __init__
        cuerpo1_0.x= 400 #indica la posicion en "x" y en "y" en la que se encontrara la serpiente
        cuerpo1_0.y= 400 #indica la posicion en "x" y en "y" en la que se encontrara la serpiente #
        cuerpo1_0.dir= 0 #...
        cuerpo1_0.raza= raza # se usa paara definir el colo de la serpiente
    def dibujar(cuerpo1_0):
        pygame.draw.rect(cuerpo1_0.raza,(0,255,0),(cuerpo1_0.x,cuerpo1_0.y, 10,10)) # el cuerpo1_0.x y en .y, define los movimientos en y y en x que se trasladara la serpiente por cuadro
    def jostick(cuerpo1_0): # esta indica cuanto vamos a girar por cada vez que le demos a una tecla y solo cuando la serpiente este en multiplos de 10 moviendose 10 cuadros 
        if cuerpo1_0.dir ==0:
            cuerpo1_0.x +=10# esta nos ayuda a que cada vez que le demos a la derecha se siga moviendo, y no se quede estatica igual con las demas 
        if cuerpo1_0.dir ==1:
            cuerpo1_0.x-=10
        if cuerpo1_0.dir ==2:
            cuerpo1_0.y +=10
        if cuerpo1_0.dir ==3:
            cuerpo1_0.y-=10  
class comida:
    c=0
    def __init__(cuerpo1_0, cuadro_del_juego):
        cuerpo1_0.x= random.randrange(80)*10 # usando la libreria random, para que la comida se de aleatoria  en los puntos del mapa ((80)*10 este lo usamos dependiendo de los ppixeles 80*10=800 el por que se multiplica es para que este sea cada 10 pixeles igualando el movimiento de la serpiente) 
        cuerpo1_0.y= random.randrange(80)*10 # usando la libreria random, para que la comida se de aleatoria  en los puntos del mapa ((80)*10 este lo usamos dependiendo de los ppixeles 80*10=800 el por que se multiplica es para que este sea cada 10 pixeles igualando el movimiento de la serpiente) 
        cuerpo1_0.cuadro_del_juego= cuadro_del_juego
    def dibujar(cuerpo1_0): # esta funcion dibuja las manzanas 
        pygame.draw.rect(cuerpo1_0.cuadro_del_juego,(255,0,0),(cuerpo1_0.x,cuerpo1_0.y, 10,10))
    def minass(cuerpo1_0): # esta funcion dibuja las minas
        pygame.draw.rect(cuerpo1_0.cuadro_del_juego,(0,0,0),(cuerpo1_0.x,cuerpo1_0.y, 10,10))
    def spawn_comida2(cuerpo1_0):
        cuerpo1_0.x= random.randrange(80)*10 # este sera el que nos genere las manzanas nuevas y no solo quedemos con una manzana y que luego desaparezca
        cuerpo1_0.y= random.randrange(80)*10  
def juego(ventana):# este nos genera el color en la ventana y ademas de esto nos dibuja la comida, tambien nos genera la serpoente
    ventana.fill((0,45,0))
    comida2.dibujar()
    comida4.dibujar()
    for largo in range(len(bicho)):
        bicho[largo].dibujar() 
def juego2(ventana):# este nos genera el color en la ventana y ademas de esto nos dibuja la comida, tambien nos genera la serpoente
    ventana.fill((0,45,0))
    comida2.dibujar()
    comida4.dibujar()
    mina1.minass()
    mina2.minass()
    for largo in range(len(bicho)):
        bicho[largo].dibujar() 
def juego3(ventana):# este nos genera el color en la ventana y ademas de esto nos dibuja la comida, tambien nos genera la serpoente
    ventana.fill((0,80,15))
    comida2.dibujar()
    comida4.dibujar()
    mina1.minass()
    mina2.minass()
    mina3.minass()
    mina4.minass()
    mina5.minass()
    mina6.minass()
    for largo in range(len(bicho)):
        bicho[largo].dibujar()         
def main(): # aqui reproducimos todas las clases y funciones anteriores ***
    global bicho, comida2, comida4
    cuadro_del_juego= pygame.display.set_mode((800, 800))
    comida2=comida(cuadro_del_juego)
    comida4=comida(cuadro_del_juego)
    
    bicho =[serpiente(cuadro_del_juego)]
    while True:
        for a in pygame.event.get():
            if a.type== pygame.QUIT:
                return False
            if a.type ==pygame.KEYDOWN:
                if a.key == pygame.K_RIGHT:
                    bicho[0].dir=0
                if a.key == pygame.K_LEFT:
                    bicho[0].dir=1
                if a.key == pygame.K_DOWN:
                    bicho[0].dir=2
                if a.key == pygame.K_UP:
                    bicho[0].dir=3
        bicho[0].jostick()
        juego(cuadro_del_juego)
        pygame.display.update()
        pygame.time.delay(50)
        if bicho[0].x == comida2.x and bicho[0].y == comida2.y: 
            comida2.spawn_comida2()
            bicho.append(serpiente(cuadro_del_juego))  
            cuenta()
            print(cuenta())
        if bicho[0].x == comida4.x and bicho[0].y == comida4.y: 
            comida4.spawn_comida2()
            bicho.append(serpiente(cuadro_del_juego))  
            cuenta()
            print(cuenta())
        propiedad_creciendo()
        if bicho[0].x >= 800:
            bicho[0].x=0
            return False
        if bicho[0].x < 0:
            bicho[0].x=790
            return False
        if bicho[0].y >= 800:
            bicho[0].y=0
            return False
        if bicho[0].y < 0:
            bicho[0].y=790
            return False   
def main2(): #extremo
    global bicho, comida2, comida4, mina1,mina2
    cuadro_del_juego= pygame.display.set_mode((800, 800))
    comida2=comida(cuadro_del_juego)
    comida4=comida(cuadro_del_juego)
    mina1=comida(cuadro_del_juego)
    mina2=comida(cuadro_del_juego)
    bicho =[serpiente(cuadro_del_juego)]
    while True:
        for a in pygame.event.get():
            if a.type== pygame.QUIT:
                return False
            if a.type ==pygame.KEYDOWN:
                if a.key == pygame.K_RIGHT:
                    bicho[0].dir=0
                if a.key == pygame.K_LEFT:
                    bicho[0].dir=1
                if a.key == pygame.K_DOWN:
                    bicho[0].dir=2
                if a.key == pygame.K_UP:
                    bicho[0].dir=3
        bicho[0].jostick()
        juego2(cuadro_del_juego)
        pygame.display.update()
        pygame.time.delay(50)
        if bicho[0].x == mina1.x and bicho[0].y == mina1.y or bicho[0].x == mina2.x and bicho[0].y == mina2.y: 
            return False
        if bicho[0].x == comida2.x and bicho[0].y == comida2.y: 
            comida2.spawn_comida2()
            bicho.append(serpiente(cuadro_del_juego))  
            cuenta()
            print(cuenta())
        if bicho[0].x == comida4.x and bicho[0].y == comida4.y: 
            comida4.spawn_comida2()
            bicho.append(serpiente(cuadro_del_juego))  
            cuenta()
            print(cuenta())
        propiedad_creciendo()
        if bicho[0].x >= 800:
            bicho[0].x=0
            return False
        if bicho[0].x < 0:
            bicho[0].x=790
            return False
        if bicho[0].y >= 800:
            bicho[0].y=0
            return False
        if bicho[0].y < 0:
            bicho[0].y=790
            return False
def main3(): #extremo
    global bicho, comida2,comida4, mina1,mina2,mina3,mina4,mina5,mina6
    cuadro_del_juego= pygame.display.set_mode((800, 800))
    comida2=comida(cuadro_del_juego)
    comida4=comida(cuadro_del_juego)
    mina1=comida(cuadro_del_juego)
    mina2=comida(cuadro_del_juego)
    mina3=comida(cuadro_del_juego)
    mina4=comida(cuadro_del_juego)
    mina5=comida(cuadro_del_juego)
    mina6=comida(cuadro_del_juego)
    bicho =[serpiente(cuadro_del_juego)]
    while True:
        for a in pygame.event.get():
            if a.type== pygame.QUIT:
                return False
            if a.type ==pygame.KEYDOWN:
                if a.key == pygame.K_RIGHT:
                    bicho[0].dir=0
                if a.key == pygame.K_LEFT:
                    bicho[0].dir=1
                if a.key == pygame.K_DOWN:
                    bicho[0].dir=2
                if a.key == pygame.K_UP:
                    bicho[0].dir=3
        bicho[0].jostick()
        juego3(cuadro_del_juego)
        pygame.display.update()
        pygame.time.delay(50)
        if bicho[0].x == mina1.x and bicho[0].y == mina1 or bicho[0].x == mina2.x and bicho[0].y == mina2.y or bicho[0].x == mina3.x and bicho[0].y == mina3.y or bicho[0].x == mina4.x and bicho[0].y == mina4.y or bicho[0].x == mina5.x and bicho[0].y == mina5.y or bicho[0].x == mina6.x and bicho[0].y == mina6.y: 
            return False
        if bicho[0].x == comida2.x and bicho[0].y == comida2.y: 
            comida2.spawn_comida2()
            bicho.append(serpiente(cuadro_del_juego))  
            cuenta()
            print(cuenta())
        if bicho[0].x == comida4.x and bicho[0].y == comida4.y: 
            comida4.spawn_comida2()
            bicho.append(serpiente(cuadro_del_juego))  
            cuenta()
            print(cuenta())
        propiedad_creciendo()
        if bicho[0].x >= 800:
            bicho[0].x=0
            return False
        if bicho[0].x < 0:
            bicho[0].x=790
            return False
        if bicho[0].y >= 800:
            bicho[0].y=0
            return False
        if bicho[0].y < 0:
            bicho[0].y=790
            return False
while True:
    if(ab==1):
        print("modo facil")
        main()
        pygame.QUIT
        print("supuntaje fue de",cuenta()-100)
        break
    if(ab==2):
        print("modo dificil")
        main2()
        pygame.QUIT
        print("supuntaje fue de",cuenta()-100)
        break
    if(ab==3):
        print("modo extremo")
        main3()
        pygame.QUIT
        print("supuntaje fue de",cuenta()-100)
        break
    ab=int(input("desea volver a jugar 1.facil 2.dificil 3.extremo 4.salir" ))
    if (ab==4):
        break