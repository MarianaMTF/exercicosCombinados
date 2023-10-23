numeros=[]
while True:
  numero=input("digite um numero (digite "0" para sair):")
  if numero==0:
    break
  numeros.append(numero)
menor=numeros[0]
for i in numeros:
  if menor>i:
    menor=i
print(f"{menor} é o menor")
