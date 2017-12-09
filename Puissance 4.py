#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#sert a coder sous linux / GNU / MAC


from turtle import *
# Initialisation des paramètres et du jeu
sc=getscreen()
ht()


def initJeu():# crée la liste sur laquelle le jeu se déroule  
    global jeu
    global joueur
    global nbrCoups
    joueur=1
    jeu = [[0,0,0,0,0,0,0], # on fait une liste pour remplir le tableau
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]
    nbrCoups=0 
    sc.clear()#remet le quad a 0 pour qu'il soit toujours vide 
    quadrillage()

    
def quadrillage():#crée le quadrillage
    tracer(False)
    for i in range(0,7):
        up()
        goto(-350,-300+100*i)
        down()
        fd(700)

    left(90)
    for i in range(0,8):
        up()
        goto(-350+100*i,-300)
        down()
        fd(600)

    update()#met à jour 
    up() 
    home()
    goto(0,-340)
    down()
    write("Appuyez sur Espace pour rejouer.",False,'center',("Arial", 16, "bold"))
    update()



def determineCase(x,y):
    #initialise les valeurs de I et J pour remettre a 0 à chaque utilisations
    global i
    global j
    i=0
    j=0
    
    j=int((x+350)//100)
    i=int((y+300)//100)
    print(i,j)#les deux print sont pour debuguer, afficher les coord de i et j dans la console
    print(x,y)
    return i,j

def pionJoueur1(i,j):#crée les pions 
    up()
    home()
    goto(-300+100*j,-300+100*i+10)
    begin_fill()
    circle(40)
    end_fill()
    
def pionJoueur2(i,j):
    up()
    home()
    goto(-300+100*j,-300+100*i+10)
    begin_fill()
    circle(40,None,4)
    end_fill()
    
def continuer(): # défini si il y a un gagnant
    global jeu
    global nbrCoups
    global joueur
    onContinue=True
    #compris entre 1 et 16 car 1*1*1*1=1 et 2*2*2*2=16 (numéro du joueur )

    for i in range(0,5):  #On teste si une ligne est gagnante
        if jeu[i][0]*jeu[i][1]*jeu[i][2]*jeu[i][3] in [1,16] or jeu[i][1]*jeu[i][2]*jeu[i][3]*jeu[i][4] in [1,16]\
           or jeu[i][2]*jeu[i][3]*jeu[i][4]*jeu[i][5] in [1,16] or jeu[i][3]*jeu[i][4]*jeu[i][5]*jeu[i][6] in [1,16]:
            onContinue=False
            
    for j in range(0,6): #On teste si une colonne est gagnante
        if jeu[0][j]*jeu[1][j]*jeu[2][j]*jeu[3][j] in [1,16] or (jeu[1][j]*jeu[2][j]*jeu[3][j]*jeu[4][j] in [1,16])\
           or jeu[2][j]*jeu[3][j]*jeu[4][j]*jeu[5][j] in [1,16]:
            onContinue=False

    #on test les diagonales "montantes" ## le BackSlash sert a revenir a la ligne au sein d'une meme ligne 
    if jeu[0][0]*jeu[1][1]*jeu[2][2]*jeu[3][3] in [1,16] or jeu[0][1]*jeu[1][2]*jeu[2][3]*jeu[3][4] in [1,16] \
       or jeu[0][2]*jeu[1][3]*jeu[2][4]*jeu[3][5] in [1,16] or jeu[0][3]*jeu[1][4]*jeu[2][5]*jeu[3][6] in [1,16]\
       or jeu[1][0]*jeu[2][1]*jeu[3][2]*jeu[4][3] in [1,16] or jeu[1][1]*jeu[2][2]*jeu[3][3]*jeu[4][4] in [1,16]\
       or jeu[1][2]*jeu[2][3]*jeu[3][4]*jeu[4][5] in [1,16] or jeu[1][3]*jeu[2][4]*jeu[3][5]*jeu[4][6] in [1,16]\
       or jeu[2][0]*jeu[3][1]*jeu[4][2]*jeu[5][3] in [1,16] or jeu[2][1]*jeu[3][2]*jeu[4][3]*jeu[5][4] in [1,16]\
       or jeu[2][2]*jeu[3][3]*jeu[4][4]*jeu[5][5] in [1,16] or jeu[2][3]*jeu[3][4]*jeu[4][5]*jeu[5][6] in [1,16]:
        onContinue=False

    #on test les diagonales descendantes
    if jeu[0][6]*jeu[1][5]*jeu[2][4]*jeu[3][3] in [1,16] or jeu[0][5]*jeu[1][4]*jeu[2][3]*jeu[3][2] in [1,16] \
       or jeu[0][4]*jeu[1][3]*jeu[2][2]*jeu[3][1] in [1,16] or jeu[0][3]*jeu[1][2]*jeu[2][1]*jeu[3][0] in [1,16]\
       or jeu[1][6]*jeu[2][5]*jeu[3][4]*jeu[4][3] in [1,16] or jeu[1][5]*jeu[2][4]*jeu[3][3]*jeu[4][2] in [1,16]\
       or jeu[1][4]*jeu[2][3]*jeu[3][2]*jeu[4][1] in [1,16] or jeu[1][3]*jeu[2][2]*jeu[3][1]*jeu[4][0] in [1,16]\
       or jeu[2][6]*jeu[3][5]*jeu[4][4]*jeu[5][3] in [1,16] or jeu[2][5]*jeu[3][4]*jeu[4][3]*jeu[5][2] in [1,16]\
       or jeu[2][4]*jeu[3][3]*jeu[4][2]*jeu[5][1] in [1,16] or jeu[2][3]*jeu[3][2]*jeu[4][1]*jeu[5][0] in [1,16]:
        onContinue=False 
        
            
        

    return onContinue

def gagnant(numeroJoueur): #affiche le gagnant 
    up()
    home()
    goto(0,350)
    down()
    if numeroJoueur==0:
        write("Match NUL",False,'center',("Arial", 16, "bold"))
    else:
        write("Le joueur " + str(numeroJoueur) + " est GAGNANT",False,'center',("Arial", 16, "bold"))

    

def play(x,y):#partie qui fait apparaitre les pion et qui rempli la liste
    global joueur
    global jeu
    global nbrCoups
    case=determineCase(x,y)
    #### partie a optimisé
    ###### les print servent à afficher dans la console la liste, ca me sert principalement a débuguer dans les cas ou les pions réécrivait sur les précédents 

    if (i not in [0,1,2,3,4,5]) or (j not in [0,1,2,3,4,5,6]):
        up()
        home()
        goto(0,320)
        down()
        write("mauvaise case",False,'center',("Arial", 16, "bold"))
        return
    if jeu[0][j] not in [1,2]:
        if joueur == 1:
            jeu[0][j] = 1
            print(jeu)
            pionJoueur1(0,j)
        else:
            jeu[0][j]=2
            print(jeu)
            pionJoueur2(0,j)
            nbrCoups=nbrCoups+1
        if continuer()==False: # Si la fonction continuer, alors on affiche le gagnant
            if joueur==1:
                gagnant(1)
            elif joueur==-1:
               gagnant(2)
            else:
                gagnant(0)
            sc.onclick(None) # On arrete d'écouter l'evenement onclick
        else:
            joueur=joueur*(-1) # On change le joueur

    elif jeu[1][j] not in [1,2]:
        if joueur == 1:
            jeu[1][j] = 1
            print(jeu)
            pionJoueur1(1,j)
        else:
            jeu[1][j]=2
            print(jeu)
            pionJoueur2(1,j)
            nbrCoups=nbrCoups+1
        if continuer()==False: # Si la fonction continuer, alors on affiche le gagnant
            if joueur==1:
                gagnant(1)
            elif joueur==-1:
               gagnant(2)
            else:
                gagnant(0)
            sc.onclick(None) # On arrete d'écouter l'evenement onclick
        else:
            joueur=joueur*(-1) # On change le joueur

    elif jeu[2][j] not in [1,2]:
        if joueur == 1:
            jeu[2][j] = 1
            print(jeu)
            pionJoueur1(2,j)
        else:
            jeu[2][j]=2
            print(jeu)
            pionJoueur2(2,j)
            nbrCoups=nbrCoups+1
        if continuer()==False: # Si la fonction continuer, alors on affiche le gagnant
            if joueur==1:
                gagnant(1)
            elif joueur==-1:
               gagnant(2)
            else:
                gagnant(0)
            sc.onclick(None) # On arrete d'écouter l'evenement onclick
        else:
            joueur=joueur*(-1) # On change le joueur

    elif jeu[3][j] not in [1,2]:
        if joueur == 1:
            jeu[3][j] = 1
            print(jeu)
            pionJoueur1(3,j)
        else:
            jeu[3][j]=2
            print(jeu)
            pionJoueur2(3,j)
            nbrCoups=nbrCoups+1
        if continuer()==False: # Si la fonction continuer, alors on affiche le gagnant
            if joueur==1:
                gagnant(1)
            elif joueur==-1:
               gagnant(2)
            else:
                gagnant(0)
            sc.onclick(None) # On arrete d'écouter l'evenement onclick
        else:
            joueur=joueur*(-1) # On change le joueur

    elif jeu[3][j] not in [1,2]:
        if joueur == 1:
            jeu[3][j] = 1
            print(jeu)
            pionJoueur1(3,j)
        else:
            jeu[3][j]=2
            print(jeu)
            pionJoueur2(3,j)
            nbrCoups=nbrCoups+1
        if continuer()==False: # Si la fonction continuer, alors on affiche le gagnant
            if joueur==1:
                gagnant(1)
            elif joueur==-1:
               gagnant(2)
            else:
                gagnant(0)
            sc.onclick(None) # On arrete d'écouter l'evenement onclick
        else:
            joueur=joueur*(-1) # On change le joueur++-

    elif jeu[4][j] not in [1,2]:
        if joueur == 1:
            jeu[4][j] = 1
            print(jeu)
            pionJoueur1(4,j)
        else:
            jeu[4][j]=2
            print(jeu)
            pionJoueur2(4,j)
            nbrCoups=nbrCoups+1
        if continuer()==False: # Si la fonction continuer, alors on affiche le gagnant
            if joueur==1:
                gagnant(1)
            elif joueur==-1:
               gagnant(2)
            else:
                gagnant(0)
            sc.onclick(None) # On arrete d'écouter l'evenement onclick
        else:
            joueur=joueur*(-1) # On change le joueur

    elif jeu[5][j] not in [1,2]:
        if joueur == 1:
            jeu[5][j] = 1
            print(jeu)
            pionJoueur1(5,j)
        else:
            jeu[5][j]=2
            print(jeu)
            pionJoueur2(5,j)
            nbrCoups=nbrCoups+1
        if continuer()==False: # Si la fonction continuer, alors on affiche le gagnant
            if joueur==1:
                gagnant(1)
            elif joueur==-1:
               gagnant(2)
            else:
                gagnant(0)
            sc.onclick(None) # On arrete d'écouter l'evenement onclick
        else:
            joueur=joueur*(-1) # On change le joueur
    

        
    
  
# Programme principal
def main():
    initJeu()
    sc.onclick(play)
    sc.onkeypress(main,'space')
    sc.listen()

if __name__=='__main__':
    print(main())
    mainloop()
