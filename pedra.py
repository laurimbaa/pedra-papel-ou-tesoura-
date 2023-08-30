import random

lista1 = ["pedra", "papel", "tesoura"]
pts_pc = 0
pts_lau = 0

while pts_lau < 3 and pts_pc < 3:
    item_sorteado = random.choice(
        lista1
    )  
    escolha = input("pedra, papel, tesoura: ")
    print(f"O item sorteado foi {item_sorteado}")
   
    if escolha == "pedra":
        if item_sorteado == "tesoura":
            pts_lau += 1
        elif item_sorteado == "papel":
            pts_pc += 1
        else:
            print("Empate")

    elif escolha == "tesoura":
        if item_sorteado == "pedra":
            pts_pc += 1
        elif item_sorteado == "papel":
            pts_lau += 1
        else:
            print("Empate!")

    elif escolha == "papel":
        if item_sorteado == "tesoura":
            pts_pc += 1
        elif item_sorteado == "pedra":
            pts_lau += 1
        else:
            print("Empate!")

    print(f"Placar é Laura: {pts_lau} vs PC: {pts_pc}")
    


def placar():
    if pts_lau == 3:
        print("Laura venceu")
    elif pts_pc == 3:
        print("O pc venceu")


placar() 




