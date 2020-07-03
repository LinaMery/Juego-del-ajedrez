import random
import pandas as pd

chess=[["000" for x in range(10)] for y in range(10)] 

g=0
chess[0][0]="XX"
chess[0][9]="XX"
chess[9][0]="XX"
chess[9][9]="XX"

chess[0][1]="1"
chess[0][2]="2"
chess[0][3]="3"
chess[0][4]="4"
chess[0][5]="5"
chess[0][6]="6"
chess[0][7]="7"
chess[0][8]="8"
chess[9][1]="1"
chess[9][2]="2"
chess[9][3]="3"
chess[9][4]="4"
chess[9][5]="5"
chess[9][6]="6"
chess[9][7]="7"
chess[9][8]="8"

chess[1][9]="1"
chess[2][9]="2"
chess[3][9]="3"
chess[4][9]="4"
chess[5][9]="5"
chess[6][9]="6"
chess[7][9]="7"
chess[8][9]="8"
chess[1][0]="1"
chess[2][0]="2"
chess[3][0]="3"
chess[4][0]="4"
chess[5][0]="5"
chess[6][0]="6"
chess[7][0]="7"
chess[8][0]="8"

chess[1][1]="TN."
chess[1][2]="CN."
chess[1][3]="AN."
chess[1][4]="rN."
chess[1][5]="RN."
chess[1][6]="AN."
chess[1][7]="CN."
chess[1][8]="TN."
chess[2][1]="PN."
chess[2][2]="PN."
chess[2][3]="PN."
chess[2][4]="PN."
chess[2][5]="PN."
chess[2][6]="PN."
chess[2][7]="PN."
chess[2][8]="PN."

chess[8][1]="TB."
chess[8][2]="CB."
chess[8][3]="AB."
chess[8][4]="rB."
chess[8][5]="RB."
chess[8][6]="AB."
chess[8][7]="CB."
chess[8][8]="TB."
chess[7][1]="PB."
chess[7][2]="PB."
chess[7][3]="PB."
chess[7][4]="PB."
chess[7][5]="PB."
chess[7][6]="PB."
chess[7][7]="PB."
chess[7][8]="PB."



nombres=[["" for x in range(2)]for y in range(2)]

def interfaz_inicial():
    global nombre_1,nombre_2,nombres
    print("============== CHESS MOBILE ============")
    print("============== BIENVENIDOS ============")
    nombres[0][0]=str(input("======> NOMBRE DE JUGADOR 1: "))
    nombres[1][0]=str(input("======> NOMBRE DE JUGADOR 2: "))
    print("============== SORTEO DE COLOR ============")
    
    while nombres[0][1]==nombres[1][1]:
        nombres[0][1]=random.choice([1,2,3,4,5,7,9,8,0])
        nombres[1][1]=random.choice([1,2,3,4,5,7,9,8,0])
        
    if nombres[0][1]<nombres[1][1]:
        print("--->JUGADOR 2 ====> BLANCAS")
        print("--->JUGADOR 1 ====> NEGRAS")
        
    else:
        print("--->JUGADOR 1 ====> BLANCAS")
        print("--->JUGADOR 2 ====> NEGRAS")
        

def turno():
    global g
    
    if nombres[0][1]<nombres[1][1]:
        if g%2==0:
            print("--->TURNO DE : "+nombres[1][0])
        
        else:
            print("--->TURNO DE : "+nombres[0][0])
    else: 
        if g%2==0:
            print("--->TURNO DE : "+nombres[0][0])
        
        else:
            print("--->TURNO DE : "+nombres[1][0])  
        
def mostrar_tablero():
    global chess,tablero
        
    #mostrando tablero#
    data = pd.DataFrame(chess)
    print(data)
n=0
k=0
d=0

def val_cc():
    global n,d,x,y,w,z,e,n,m,k
    
    while(n>88 or n==0 or d>88 or d==0):
        n=int(input("CC: "))
        d=int(input("Destino: "))
    x=n//10
    y=n%10
    m=chess[x][y]
    
    w=d//10
    z=d%10
    e=chess[w][z]
    
    

destino=[int(0) for x in range(8)]

#funcion que valida el movimiento del caballo y lo ejecuta#
def val_caballo():
    global k,destino,x,y,w,z,e,m,g
    
    destino[0]=10*(x+2)+y+1
    destino[1]=10*(x+2)+y-1
    destino[2]=10*(x-2)+y+1
    destino[3]=10*(x-2)+y-1
    destino[4]=10*(x+1)+y+2
    destino[5]=10*(x-1)+y+2
    destino[6]=10*(x+1)+y-2
    destino[7]=10*(x-1)+y-2

    for i in range(8):
        
        if (destino[i]==d):
            k=k+1
        destino[i]=0
    
    if(m[1]=="B" and k==1):
        if(e=="000" or e[1]=="N"):
            chess[x][y]="000"
            chess[w][z]="CB."
        else:
            print("movimiento no valido")
            g=g-1
          
    elif(m[1]=="N" and k==1):
        if(e=="000" or e[1]=="B"):
            chess[x][y]="000"
            chess[w][z]="CN."
        else:
            print("movimiento no valido")
            g=g-1
    else:
        print("movimiento no valido")
        g=g-1
        
#funcion que valida el movimiento del peon y lo ejecuta#
def val_peon():
    global k,destino,x,y,w,z,e,m,g
    
    if(m[1]=="B"):
        if chess[x-1][y]!="000":
            destino[0]=0
            destino[1]=0
        else:
            destino[0]=10*(x-1)+y
            if chess[x-2][y]!="000":
                destino[1]=0
            else:
                destino[1]=10*(x-2)+y
        
        
        destino[2]=10*(x-1)+y+1
        destino[3]=10*(x-1)+y-1
        
        if(e=="000" and (d==destino[0] or d==destino[1])):
            chess[x][y]="000"
            chess[w][z]="PB."
            
        elif(e[1]=="N" and (d==destino[2] or d==destino[3])):
            chess[x][y]="000"
            chess[w][z]="PB."
            
        else:
            print("movimiento no valido")
            g=g-1
            
    
    if(m[1]=="N"):
        if chess[x+1][y]!="000":
            destino[0]=0
            destino[1]=0
        else:
            destino[0]=10*(x+1)+y
            if chess[x+2][y]!="000":
                destino[1]=0
            else:
                destino[1]=10*(x+2)+y
           
        destino[2]=10*(x+1)+y+1
        destino[3]=10*(x+1)+y-1
        
        if(e=="000" and (d==destino[0] or d==destino[1])):
            chess[x][y]="000"
            chess[w][z]="PN."
        elif(e[1]=="B" and (d==destino[2] or d==destino[3])):
            chess[x][y]="000"
            chess[w][z]="PN."
        else:
            print("movimiento no valido")
            g=g-1

#funcion que valida el movimiento del alfil y lo ejecuta#
def val_alfil():
    global k,destino,x,y,w,z,e,m,g
    
    if ((n-d)%11==0) :
        if n<d:
            
            tope=int((d-n)/11)
            for i in range(tope-1):
                casilla=d-11*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int((n-d)/11)
            for i in range(tope-1):
                casilla=n-11*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
     
    elif ((n-d)%9==0) :
        if n<d:
            tope=int((d-n)/9)
            
            for i in range(tope-1):
                casilla=d-9*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int((n-d)/9)
            
            for i in range(tope-1):
                casilla=n-9*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1            
    else:
        print("movimiento no valido")
        g=g-1
        
    if(m[1]=="B" and k==1):
        if(e=="000" or e[1]=="N"):
            chess[x][y]="000"
            chess[w][z]="AB."
    
    elif(m[1]=="N" and k==1):
        if(e=="000" or e[1]=="B"):
            chess[x][y]="000"
            chess[w][z]="AN."
    else:
        print("movimiento no valido")
        g=g-1

#funcion que valida el movimiento de la torre y lo ejecuta#
def val_torre():
    global k,destino,x,y,w,z,e,m,g
    if (x==w) :
        
        if n<d:
            tope=int(z-y)     
            for i in range(tope-1):
                casilla=d-1
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int(y-z)
            
            for i in range(tope-1):
                casilla=n-1
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
     
    elif (y==z) :
        
        if n<d:
            tope=int(w-x)            
            for i in range(tope-1):
                casilla=d-10*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int(x-w)
            
            for i in range(tope-1):
                casilla=n-10*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1            
    else:
        
        print("movimiento no valido")
        g=g-1
        
    if(m[1]=="B" and k==1):
        if(e=="000" or e[1]=="N"):
            chess[x][y]="000"
            chess[w][z]="TB."
                      
    elif(m[1]=="N" and k==1):
        if(e=="000" or e[1]=="B"):
            chess[x][y]="000"
            chess[w][z]="TN."
    else:
        print("movimiento no valido")
        g=g-1

#funcion que valida el movimiento de la reina y lo ejecuta#
def val_reina():
    global k,destino,x,y,w,z,e,m,g
    if (x==w) :
        
        if n<d:
            tope=int(z-y)     
            for i in range(tope-1):
                casilla=d-1
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int(y-z)
            
            for i in range(tope-1):
                casilla=n-1
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
     
    elif (y==z) :
        
        if n<d:
            tope=int(w-x)            
            for i in range(tope-1):
                casilla=d-10*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int(x-w)
            print(tope)
            for i in range(tope-1):
                casilla=n-10*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
                        
    elif ((n-d)%11==0) :
        
        if n<d:
            
            tope=int((d-n)/11)
            
            for i in range(tope-1):
                casilla=d-11*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int((n-d)/11)
            
            for i in range(tope-1):
                casilla=n-11*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
     
    elif ((n-d)%9==0) :
        
        if n<d:
            tope=int((d-n)/9)
            
            for i in range(tope-1):
                casilla=d-9*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
        else:
            
            tope=int((n-d)/9)
            
            for i in range(tope-1):
                casilla=n-9*(i+1)
                if chess[casilla//10][casilla%10]!="000":
                    k=0
                else:
                    k=1
    else:
        
        print("movimiento no valido")
        g=g-1
        
    if(m[1]=="B" and k==1):
        if(e=="000" or e[1]=="N"):
            chess[x][y]="000"
            chess[w][z]="rB."
                      
    elif(m[1]=="N" and k==1):
        if(e=="000" or e[1]=="B"):
            chess[x][y]="000"
            chess[w][z]="rN."
    else:
        print("movimiento no valido")
        g=g-1

#funcion que valida el movimiento del reyy lo ejecuta#
def val_rey():
    global k,destino,x,y,w,z,e,m,g
    destino[0]=10*(x-1)+y
    destino[1]=10*(x-1)+y+1
    destino[2]=10*(x-1)+y-1
    destino[3]=10*(x+1)+y
    destino[4]=10*(x+1)+y+1
    destino[5]=10*(x+1)+y-1
    destino[6]=10*x+y+1
    destino[7]=10*x+y-1
    for i in range(8):
        if destino[i]==d:
            k=1
        else:
            k=0
    if(m[1]=="B" and k==1):
        if(e=="000" or e[1]=="N"):
            chess[x][y]="000"
            chess[w][z]="RB."
                      
    elif(m[1]=="N" and k==1):
        if(e=="000" or e[1]=="B"):
            chess[x][y]="000"
            chess[w][z]="RN."
    else:
        print("movimiento no valido")
        g=g-1

interfaz_inicial()
mostrar_tablero()


while g!=800:
    
    turno()
    d=0
    n=0
    val_cc()
        
    if(m[0]=="C"):
        val_caballo()
        mostrar_tablero()
        k=0
        
    elif(m[0]=="P"):
        val_peon()
        mostrar_tablero()
        k=0
        
    elif(m[0]=="A"):
        val_alfil()
        mostrar_tablero()
        k=0

    elif(m[0]=="T"):
        val_torre()
        mostrar_tablero()
        k=0

    elif(m[0]=="r"):
        val_reina()
        mostrar_tablero()
        k=0

    elif(m[0]=="R"):
        val_rey()
        mostrar_tablero()
        k=0
    
    else:
        print("movimiento no valido")
        g=g-1
    g=g+1
    



