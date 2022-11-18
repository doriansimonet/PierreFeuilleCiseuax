from random import randint
def game(pointJoueur, pointBot):
    resultat = ""
    if pointJoueur < 3 and pointBot < 3 :
        coups = ["pierre", "feuille", "ciseaux"]
        coupJoueur = input("choissisez entre pierre, feuille ou ciseaux : ")
        if coupJoueur != "pierre" and coupJoueur != "feuille" and coupJoueur != "ciseaux" :
            print("Veuillez choisir une valeur conforme, recommencez ")
            return game(pointJoueur, pointBot)
        coupBot = coups[randint(0,2)]
        if coupJoueur == coupBot :
            print(coupJoueur, "contre", coupBot, "c'est une égalité")
            return game(pointJoueur, pointBot)
        if coupJoueur == "ciseaux":
            if coupBot == "pierre" :
                print("Perdu, la pierre casse les ciseaux")
                return game(pointJoueur, pointBot + 1)
            if coupBot == "feuille":
                print("Gagné, les ciseaux coupent la feuille")
                return game(pointJoueur + 1, pointBot)
        if coupJoueur == "pierre":
            if coupBot == "feuille" :
                print("Perdu, la feuille couvre la pierre")
                return game(pointJoueur, pointBot + 1)
            if coupBot == "ciseaux" :
                print("Gagné, la pierre casse les ciseaux")
                return game(pointJoueur + 1, pointBot)
        if coupJoueur == "feuille" :
            if coupBot == "ciseaux" :
                print("Perdu, les ciseaux coupent la feuille")
                return game(pointJoueur, pointBot + 1)
            if coupBot == "pierre" :
                print("Gagné, la feuille couvre la pierre")
                return game(pointJoueur + 1, pointBot)
    elif pointJoueur > pointBot :
        resultat = "félicitations vous avez gagné " + str(pointJoueur) + " contre " + str(pointBot)
        return resultat
    else:
        resultat = "Dommage vous avez perdu " + str(pointJoueur) + " contre " + str(pointBot)
        return resultat

print(game(0, 0))