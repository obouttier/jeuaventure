"""
Programme réalisé par Bouttier Oscar, 1G5
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("entre_new.jpg")
image2=pygame.image.load("salon_new.jpg")
image3=pygame.image.load("escalier_new.jpg")
image4=pygame.image.load("sous_sol_new.jpg")
image5=pygame.image.load("piece_new.jpg")
image6=pygame.image.load("salle_de_bain_new.jpg")
image7=pygame.image.load("bibliotheque_new.jpg")
image8=pygame.image.load("chambre_new.jpg")
image9=pygame.image.load("chambre_2_new.jpg")
image10=pygame.image.load("sortie_new.jpg")
text1 = font.render("Cette entrée est assez atypique mais, elle est dans son charme...", True, (255, 255, 255))
text2 = font.render("Ici nous sommes dans le salon, un peu trop de chaises à mon gout...", True, (255, 255, 255))
text3 = font.render("Ici les escaliers, je me demande qu'est-ce qui s'y trouve en haut.", True, (255, 255, 255))
text4 = font.render("Voici le sous-sol, une telle quantité de vin est énorme.", True, (255, 255, 255))
text5 = font.render("Une pièce étrange, un bureau probablement...", True, (255, 255, 255))
text6 = font.render("La salle de bain, je crois que ce chateau devient un peu luxueux...", True, (255, 255, 255))
text7 = font.render("Voilà une bibliothèque, au moins il y a des livres !", True, (255, 255, 255))
text8 = font.render("Voici une chambre, c'est rouge...", True, (255, 255, 255))
text9 = font.render("La deuxième chambre, on dirait un mixte de ancien et de récent...", True, (255, 255, 255))
text10 = font.render("Voici le chateau, il est classique d'apparence...", True, (255, 255, 255))



pieceNow=1


def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(70,850)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(70,850))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(70,850))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(70,850))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(70,850))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(70,850))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(70,850))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(70,850))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(70,850))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(70,850))



def decision(direction,piece):
    print("Vous allez dans la direction",direction)
    savePiece=piece
    #N : le personnage désire aller au nord
    if direction=='n':
        if piece==1:
            piece=2
        elif piece==5:
            piece=6
        elif piece==2:
            piece=7
        elif piece==3:
            piece=8
        elif piece==10:
            piece=1
    #S : le personnage désire aller au sud
    elif direction=='s':
        if piece==2:
            piece=1
        elif piece==6:
            piece=5
        elif piece==7:
            piece=2
        elif piece==8:
            piece=3
        elif piece==1:
            piece=10
    #E : le personnage désire aller à l'est
    elif direction=='e':
        if piece==2:
            piece=3
        elif piece==3:
            piece=4
        elif piece==5:
            piece=2
        elif piece==6:
            piece=7
        elif piece==7:
            piece=8
        elif piece==8:
            piece=9
    #O : le personnage désire aller à l'ouest
    elif direction=='o':
        if piece==3:
            piece=2
        elif piece==4:
            piece=3
        elif piece==2:
            piece=5
        elif piece==7:
            piece=6
        elif piece==8:
            piece=7
        elif piece==9:
            piece=8
    if savePiece==piece:
        print("Déplacement impossible")
    else:
        print("Déplacement effectué")
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            pieceNow=decision(event.unicode,pieceNow)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(pieceNow)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

