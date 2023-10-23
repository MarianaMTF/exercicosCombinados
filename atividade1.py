notas=[]
while True:
  nota=input("digite sua nota (digite "0" para sair):")
  if nota==0:
    break
  notas.append(nota)
media=sum(notas)/len(notas)
print(f"sua media é {media}")
