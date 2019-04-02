import random


class Joueur:
    '''
    Classe générale de joueur. Vous est fournie.
    '''

    def __init__(self, couleur):
        '''
        Le constructeur global de Joueur.

        Args :
            couleur, la couleur qui sera jouée par le joueur.
        '''
        assert couleur in ["jaune", "rouge"], "Piece: couleur invalide."
        self.couleur = couleur

    def obtenir_type_joueur(self):
        '''
        Cette méthode sera implémentée par JoueurHumain et JoueurOrdinateur

        Returns :
            'Ordinateur' ou 'Humain'
        '''
        #Utilisation de type pour déterminer les types des classes filles de la classe Joueur
        if type(self) is JoueurOrdinateur:
            return "Ordinateur"
        if type(self) is JoueurHumain:
            return "Humain"

    def jouer_sur_grille(self, grille):
        '''
        Cette méthode sera implémentée par JoueurHumain et JoueurOrdinateur.

        Args :
            grille, la grille sur laquelle le joueur joue
        '''
        #coup représente la colonne sur laquelle le joueur veut placer un jeton
        #validite est un bool prenant comme valeur la possibilité que le coup s'execute ou pas
        #message est l'information à envoyer au joueur lorsqu'il effectue un placement de jeton impossible
        if self.obtenir_type_joueur() == "Humain":
            while True:
                try:
                    coup = int(input("Quelle est la colonne ou vous désirez jouer? "))
                    break
                except ValueError:
                    print("la valeur de la colonne doit etre un entier")
            validite, message = grille.valider_coup(coup)
            while (validite != True):
                print(message)
                while True:
                    try:
                        coup = int(input("Quelle est la colonne ou vous désirez jouer? "))
                        break
                    except ValueError:
                        print("la valeur de la colonne doit etre un entier")
                validite, message = grille.valider_coup(coup)
            grille.jouer_coup(coup, self.couleur)
        else:
            coup = random.randint(0,6)
            print("Quelle est la colonne ou vous désirez jouer? ",coup)
            grille.jouer_coup(coup, self.couleur)
class JoueurHumain(Joueur):
    '''
    Classe modélisant un joueur humain.
    '''

    def __init__(self, couleur):
        '''
        Cette méthode va construire un objet Joueur et
        l'initialiser avec la bonne couleur.
        '''
        super().__init__(couleur)

    def obtenir_type_joueur(self):
        return "Humain"

    def jouer_sur_grille(self, grille):
        '''
        Demande à l'usager à quelle colonne il désire jouer.

        Tant que le coup entré par l'utilisateur n'est pas valide
        (pensez à grille.valider_coup()), on lui affiche le
        message d'erreur retournée par grille.valider_coup() et
        on lui redemande de choisir un coup.

        Une fois que l'on a obtenu un coup valide, on appelle ici
        grille.jouer_coup().

        Args :
            grille, la grille sur laquelle le joueur joue
        '''
        Joueur.jouer_sur_grille(self, grille)

class JoueurOrdinateur(Joueur):
    '''
    Classe modélisant un joueur ordinateur.
    '''

    def __init__(self, couleur):
        '''
        Cette méthode va construire un objet Joueur et
        l'initialiser avec la bonne couleur.
        '''
        super().__init__(couleur)

    def obtenir_type_joueur(self):
        return "Ordinateur"

    def jouer_sur_grille(self, grille):
        '''
        Méthode qui va choisir aléatoirement un coup parmi les
        coups possibles sur la grille. Pensez à utiliser
        random.choice() et grille.obtenir_coups_possibles() pour
        vous faciliter la tâche.

        Une fois que l'on a obtenu un coup valide, on appelle ici
        grille.jouer_coup().

        N.B. Vous pouvez sans aucun problème implémenter un
                joueur ordinateur plus avancé qu'un simple choix
                aléatoire. Il s'agit seulement du niveau minimum requis.

        Args :
            grille, la grille sur laquelle le joueur joue
        '''
        Joueur.jouer_sur_grille(self, grille)

