import random

aleatorio=random.randint(1, 100)
for i in range(1, 6):
  numero=int(input("escolha um numero:"))
  if numero==aleatorio:
    print("você ganhou")
  elif numero<aleatorio:
    print("um pouco mais")
  elif numero>aleatorio:
    print("um pouco menos")
  elif i==5:
    print("você perdeu")
