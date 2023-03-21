from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def afiseaza_carti(participant):
    if participant == player:
        print("Acestea sunt cartile tale:")
        for cards in player:
            print(cards, end=" ")
    else:
        print(f"\nAdversarul are aceasta carte:\n{computer[0]}")


def calc_scor(participant):
    score = 0
    for card in participant:
        score += card
    return score


def ai_castigat(participant, computer):
    if calc_scor(participant) > calc_scor(computer):
        print("Ai castigat!")
    elif calc_scor(participant) < calc_scor(computer):
        print("Ai pierdut!")
    else:
        print("Egalitate")

def ad_carte(participant):
    participant.append(random.choice(cards))
    calc_scor(participant)
    if participant[-1] == 11 and calc_scor(participant) > 21:
        participant[-1] = 1
    afiseaza_carti(participant)
    return calc_scor(participant)


functie = {
    "afisare": afiseaza_carti,
    "calculare": calc_scor,
    "adaugare": ad_carte,
    "final": ai_castigat,
}
"""Atribuire carti initiale si afisare"""

joaca = True
player = []
computer = []
player.append(random.choice(cards))
player.append(random.choice(cards))
computer.append(random.choice(cards))
computer.append(random.choice(cards))
functie["afisare"](player)
functie["afisare"](computer)
while joaca:
    raspuns = input("Doriti sa mai primiti o carte: 'da' sau 'nu'\n").lower()
    if raspuns != "da":
        joaca = False
        functie["final"](player, computer)
    else:
        functie["adaugare"](player)
        functie["adaugare"](computer)