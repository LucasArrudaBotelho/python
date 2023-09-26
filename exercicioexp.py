from datetime import date

diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year
diaNascimento = int(input("dia do nascimento:"))
mesNascimento = int(input("mes do nascimento:"))
anoNascimento = int(input("ano do nascimento:"))

print(f"{diaAtual}/{mesAtual}/{anoAtual}")

if(mesNascimento < mesAtual):
print("sim o mes de nascimento é menor que mes atual")

else:
    print("o mes de nascimento é maior que mes atual")
    print(não fiz aniversario)



