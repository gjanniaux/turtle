"""
Ceci est un module de dessin de polygones !
"""
class MonPolygone:
    """Classe mère pour tous les polygones"""

    geometrie = {"MonCarre":(4, 90), "MonHexagone":(6, 60), "MonTriangle":(3, 120), "MonPentagone":(5, 72)}

    def __init__(self, x, y, cote):
        """Constructeur personnalisé avec position de départ et longueur de côté"""
        self.pos_x = x
        self.pos_y = y
        self.distance = cote
        self.ep_trait = 1
        self.couleur_trait = "black"
        self.couleur_plein = "white"
        print(self.__class__.__name__)

    def habillage(self, ep, couleur, fond = "white"):
        """Fonction pour donner l'épaisseur de trait
           Et les couleurs de trait et de fond"""
        self.ep_trait = ep
        self.couleur_trait = couleur
        self.couleur_plein = fond

    def depart(self, turtleplus):
        """Positionne le crayon au point de départ"""
        turtleplus.penup()  # Soulever le crayon
        turtleplus.setx(self.pos_x)
        turtleplus.sety(self.pos_y)
        turtleplus.pendown()  # Descendre le crayon
        # Donner l'épaisseur de trait et la couleur
        turtleplus.pensize(self.ep_trait)
        turtleplus.pencolor(self.couleur_trait)
        turtleplus.fillcolor(self.couleur_plein)

    # Méthode pour dessiner le polygone
    def dessine(self, turtleplus):
        """Dessiner le polygone sur l'objet turtle fourni en paramètre"""
        # Corps de la fonction
        self.depart(turtleplus)
        # Je peux exploiter le paramètre/variable distance
        turtleplus.begin_fill()
        for nb in range(0, MonPolygone.geometrie[self.__class__.__name__][0]):
            turtleplus.forward(self.distance)
            turtleplus.left(MonPolygone.geometrie[self.__class__.__name__][1])
        turtleplus.end_fill()

    # Affichage personnalisé
    def __repr__(self):
        return "Polygone positionné en " + str(self.pos_x) + "," + str(self.pos_y)

class MonCarre(MonPolygone):
    """Classe fille pour gérer les carrés"""
    #Corps de la classe
    pass

class MonHexagone(MonPolygone):
    """Classe fille pour gérer les hexagones"""
    # Corps de la classe
    pass
class MonTriangle(MonPolygone):
    """Classe fille pour gérer les triangles"""
    # Corps de la classe
    pass

class MonPentagone(MonPolygone):
    """Classe fille pour gérer les pentagones"""
    # Corps de la classe
    pass
