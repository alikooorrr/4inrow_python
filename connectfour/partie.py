from grille import Grille
from joueur import JoueurOrdinateur, JoueurHumain


class PartieConnectFour:
    def __init__(self, nom_fichier=None):
        '''
        Méthode d'initialisation d'une partie.
        '''
        self.grille = Grille()

        self.gagnant_partie = None
        self.partie_nulle = False

        if nom_fichier is not None:
            self.charger(nom_fichier)
        else:
            self.initialiser_joueurs()

    def initialiser_joueurs(self):
        '''
        On initialise ici quatre attributs : joueur_jaune,
        joueur_rouge, joueur_courant et couleur_joueur_courant.

        joueur_courant est initialisé par défaut au joueur_jaune
        et couleur_joueur_courant est initialisée à "jaune".

        Pour créer les objets joueur, faites appel à
        creer_joueur().

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.
        '''
        self.decision = input("Voulez vous une nouvelle partie ou charger la derniere? N ou C ")
        while self.decision != "N" and self.decision != "C":
            self.decision = input("Voulez vous une nouvelle partie ou charger la derniere? N ou C ")
        if self.decision == "C":
            print("Les information de la derniere partie : ")
        else:
            self.joueur_jaune = self.creer_joueur("jaune")
            self.joueur_courant = self.joueur_jaune
            self.couleur_joueur_courant = "jaune"
            self.joueur_rouge = self.creer_joueur("rouge")

    def creer_joueur(self, couleur):
        '''
        Demande à l'usager quel type de joueur ('Humain' ou
        'Ordinateur') il désire pour le joueur de la couleur en
        entrée.

        Tant que l'entrée n'est pas valide, on continue de
        demander à l'utilisateur.

        Faites appel à self.creer_joueur_selon_type() pour créer
        le joueur lorsque vous aurez le type.

        Args :
            couleur, la couleur pour laquelle on veut le type
                de joueur.

        Returns :
            Un objet Joueur, de type JoueurHumain
            si l'usager a entré 'Humain', JoueurOrdinateur s'il a
            entré 'Ordinateur'.
        '''
        #type_joueur comporte un string determinant le type du joueur(Humain ou Ordinateur)
        type_joueur = input("Quel type de joueur désirez-vous pour la couleur "+couleur+" ? Entrez Humain ou Ordinateur ")
        while type_joueur != "Humain" and type_joueur != "Ordinateur":
            type_joueur = input("Le type entré est invalide \nQuel type de joueur désirez-vous pour la couleur "+couleur+ " ? Entrez Humain ou Ordinateur ")
        return self.creer_joueur_selon_type(type_joueur,couleur)

    def creer_joueur_selon_type(self, type_joueur, couleur):
        '''
        Crée l'objet Joueur approprié, selon le type passé en
        paramètre.

        Pour créer les objets, vous n'avez qu'à faire appel à
        leurs constructeurs, c'est-à-dire à
        JoueurHumain(couleur), par exemple.

        Args :
            type, le type de joueur, "Ordinateur" ou "Humain"
            couleur, la couleur du pion joué par le jouer,
                "jaune" ou "rouge"

        Returns :
            Un objet JoueurHumain si le
            type est "Humain", JoueurOrdinateur sinon
        '''
        return JoueurHumain(couleur) if type_joueur == "Humain" else JoueurOrdinateur(couleur)

    def jouer(self):
        '''
        Méthode représentant la boucle principale de jeu.

        Celle-ci fonctionne comme une boucle infinie. Pour chaque
        itération, on affiche la grille avec print(self.grille)
        et on joue un tour. Si la partie est terminée, on quitte
        la boucle. Sinon, on change de joueur.

        Quand on sort de la boucle principale, on fait le
        traitement de la fin de partie.

        Utilisez les fonctions partie_terminee(), jouer_tour(),
        changer_joueur() et traitement_fin_partie() pour vous
        faciliter la tâche.
        '''

        #open("partie_nulle.txt", "w").close()
        infinie = False
        while(infinie != True):
            print(self.grille)
            self.jouer_tour()
            self.sauvegarder("partie_sauvegardee.txt")
            open("partie_nulle.txt","w").write(self.grille.convertir_en_chaine())
            infinie = True
            if(self.partie_terminee()== True):
                self.traitement_fin_partie()
                print("Voici la ligne lui ayant permis de gagner !")
                self.grille.surligner_sequence_gagnante()
                print(self.grille)
            else:
                self.changer_joueur()
                infinie = False


    def jouer_tour(self):
        '''
        Cette méthode commence par afficher à quel joueur c'est
        tour de jouer. Ensuite, on fait jouer le joueur courant
        sur la grille.
        '''
        print("C'est au tour du joueur "+self.couleur_joueur_courant+" de jouer.")
        self.joueur_courant.jouer_sur_grille(self.grille)

    def partie_terminee(self):
        '''
        Méthode vérifiant si la partie est terminée.

        Si la grille est pleine, on ajuste l'attribut
        partie_nulle à True.

        Si la grille possède un gagnant, on assigne la couleur du
        joueur courant à l'attribut gagnant_partie.

        Returns :
            True si la partie est terminée, False sinon
        '''
        if self.grille.est_pleine():
            self.partie_nulle = True
        if self.grille.possede_un_gagnant():
            self.gagnant_partie = self.couleur_joueur_courant
        return True if self.grille.possede_un_gagnant() or self.grille.est_pleine() else False

    def changer_joueur(self):
        '''
        En fonction de la couleur du joueur courant actuel, met à
        jour les attributs joueur_courant et couleur_joueur_courant.
        '''
        if self.couleur_joueur_courant == "jaune":
            self.joueur_courant = self.joueur_rouge
            self.couleur_joueur_courant = "rouge"
        else:
            self.joueur_courant = self.joueur_jaune
            self.couleur_joueur_courant ="jaune"

    def traitement_fin_partie(self):
        '''
        Méthode qui gère le comportement de fin de partie.

        Si l'attribut gagnant_partie n'est pas None, on surligne
        la séquence gagnante de la grille et on affiche un
        message approprié pour féliciter le gagnant en plus
        d'afficher la grille avec la séquence gagnante surlignée.

        Sinon, on affiche le message d'un match nul.
        '''
        if(self.gagnant_partie is not None):
            self.grille.surligner_sequence_gagnante()
            print("!!!!!!!!!!! Félicitation le joueur "+self.couleur_joueur_courant+" a gagné la partie !!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!! Vous n'avez pas démérité mais un match nul s'impose !!!!!!!!!!!!")

    def sauvegarder(self, nom_fichier):
        '''
        Sauvegarde une partie dans un fichier. Le fichier
        contiendra:
        - Une ligne indiquant la couleur du joueur courant.
        - Une ligne contenant le type du joueur jaune.
        - Une ligne contenant le type du joueur rouge.
        - Le reste des lignes correspondant à la grille. Voir la
          méthode convertir_en_chaine de la grille pour le
          format.

        Args :
            nom_fichier, le string du nom du fichier où sauvegarder.
        '''
        open(nom_fichier, "w").write(self.couleur_joueur_courant+"\n"+(str)(type(self.joueur_jaune))+"\n"+(str)(type(self.joueur_rouge))+"\n"+self.grille.convertir_en_chaine())

    def charger(self, nom_fichier):
        '''
        Charge une partie dans à partir d'un fichier. Le fichier
        a le même format que la méthode de sauvegarde.
        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.

        Args:
            nom_fichier: Le string du nom du fichier à charger.
        '''
        self.couleur_joueur_courant = open(nom_fichier, "r").readline()
        with open(nom_fichier,"r") as f:
            for i in range(2):
                self.joueur_jaune = f.readline()
        with open(nom_fichier,"r") as f:
            for i in range(3):
                self.joueur_rouge = f.readline()
        chaine = open("partie_nulle.txt", "r").read()
        self.grille.charger_dune_chaine(chaine)
        print("Couleur joueur courant: ", self.couleur_joueur_courant)
        print("Type joueur jaune: ", self.joueur_jaune)
        print("Type joueur rouge: ", self.joueur_rouge)


