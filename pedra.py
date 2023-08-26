
lista1= ["pedra", "papel","tesoura"]
import random 
item_sorteado = random.choice(lista1) 
pts_pc = 0
pts_lau = 0

while pts_lau < 3 or pts_pc < 3:
    escolha = input("pedra, papel, tesoura: ")
    print(f"O item sorteado foi {item_sorteado}")
    print(f"Placar é Laura {pts_lau} vs PC{pts_pc}")
    if escolha == "pedra":
        if item_sorteado == "tesoura":
            pts_lau+=1
        elif item_sorteado == "papel":
            pts_pc+=1
        elif item_sorteado == "pedra":
            print("empate")

    if escolha == "tesoura":
        if item_sorteado == "pedra":
            pts_pc+=1
        elif item_sorteado == "papel":
            pts_lau+=1
        elif item_sorteado == "tesoura":
            print("empate!")
    

    if escolha == "papel":
        if item_sorteado == "tesoura":
            pts_pc+=1
        elif item_sorteado == "pedra":
            pts_lau+=1
        elif item_sorteado == "papel":
            print("empate!")

 
    

def placar():
    if pts_lau==3:
        print("Laura venceu")
    if pts_pc == 3:
        print("O pc venceu")
    return 
  



