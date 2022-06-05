#Exercicio 1
n1 = int(input('escreva um numero: '))
n2 = int(input('escreva um numero: '))
if n1 > n2:
    print('o primeiro numero é maior')
else:
    print('o segundo numero é maior')



#Exercicio 2
n1 = int(input('escreva um numero: '))
if n1 > 0:
    print('O numero é positivo')
else:
    print('o numero é negativo')



#Exercicio 3
s = input('Escreva [F] para Feminino ou [M] para Masculino: ')
if s == 'f':
    print('Sexo: Feminino')
elif s == 'm':
    print('Sexo: Masculino')
else:
    print('Sexo invalido')



#Exercicio 4
x = input('Digite uma letra: ')
if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
    print('A letra é vogal')
else:
    print('A letra é consoante')



#Exercicio 5
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda  nota: '))
if (n1+n2)/2 == 10:
    print('Aprovado com Distinção')
elif (n1+n2)/2 < 7:
    print('Reprovado')
elif (n1+n2)/2 >= 7:
    print('Aprovado')



#Exercicio 6
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1>n2 and n1>n3:
    print('O primeiro numero é maior ')
if n2>n1 and n2>n3:
    print('O segundo numero é maior ')
if n3>n2 and n3>n1:
    print('O terceiro numero é maior ')



#Exercicio 7
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
maior = a
menor = c
if b > a:
    maior = b
if c > a:
    maior = c
if a < c:
    menor = a
if b < c:
    menor = b
print(f'O maior numero é {maior}')
print(f' o menor numero é {menor}')



#Exercicio 8
p1 = float(input('Escreva o preço do primeiro produto: '))
p2 = float(input('Escreva o preço do segundo produto: '))
p3 = float(input('Escreva o preço do terceiro produto: '))
if p1<p2 and p1<p3:
    print('Compre o primeiro produto, pois é mais barato')
if p2<p1 and p2<p3:
    print('Compre o segundo produto, pois é mais barato')
if p3<p1 and p3<p2:
    print('Compre o terceiro produto, pois é mais barato')



#Exercicio 9
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
if a < c:
    a, c = c, a
if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
print(f'A ordem decrescente é {a}, {b} e {c}')



#Exercicio 10
print('Qual turno você estuda? [M]matutino [V]vespertino [N]noturno')
turno = input('---')
if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa Tarde!')
elif turno == 'n':
    print('Boa noite!')
else:
    print('valor invalido!')



#Exercicio 11
x = int(input('digite uma nota: '))
while x <= 0 or x > 10:
    print('A nota deve estar entre 0 e 10')
    x = int(input('digite uma nota: '))



#Exercicio 12
senha = 1
user = 1

while senha == user:
    user = input('digite o nome de usuario: ')
    senha = input('digite sua senha: ')
    if senha == user:
        print('a senha nao pode ser igual ao nome de usuario')
print('loading...')



#Exercicio  13
nome = input('qual é o seu nome? --- ')
while len(nome) <= 3:
    print('nome deve conter mais de tres caracteres')
    nome = input('qual é o seu nome? --- ')

idade = int(input('qual é sua idade? ---'))
while idade > 150 and idade < 0:
    print('idade deve estar entre 0 e 150')
    idade = int(input('qual é sua idade? ---'))

salario = float(input('quanto é o seu salario? ---'))
while salario <= 0:
    print('salario deve ser maior que 0')
    salario = float(input('quanto é o seu salario? ---'))

genere = input('[M]masculino [F]feminino ---')
while genere != 'm' and genere != 'f':
    print('digite apenas [M] ou [F]')
    genere = input('[M]masculino [F]feminino ---')

est_civil = input('Estado civil: [S]solteiro [C]casado [V]viuvo [D]divorciado ---')
while est_civil != 's' and est_civil != 'c' and est_civil!= 'v' and est_civil != 'd':
    print('digite apenas [S],[C],[V],[D]')



#exercicio 14
a = 80000
b = 200000
count = 0
while a < b:
    print(f'a={a} \nb={b}')
    print(count)
    a += (3/100)*a
    b += (1.5/100)*b
    count += 1



#exercicio 15
def populacao():
    a = int(input('População do pais A: '))
    ta = float(input('Taxa de crescimento do pais A: '))
    b = int(input('População do pais B: '))
    tb = float(input('Taxa de crescimento do pais B:'))
    count = 0
    while a < b:
        print(f'País A:{a} \nPaís B:{b}')
        print(f'Ano: {count}')
        count += 1
        a += (ta/100)*a
        b += (tb/100)*b
    print('Deseja continuar? [Y]sim - [N]não')
    again = input('---')
    if again == 'y':
        populacao()
    else:
        print('tenha um bom dia!')
populacao()



#Exercicio 16
print(list(range(1,21)))
for i in range(1,21):
    print(i)



#exercicio 17
a = int(input('n1 --- '))
b = int(input('n2 --- '))
c = int(input('n3 --- '))
d = int(input('n4 --- '))
e = int(input('n5 --- '))
maior = a
if b > a:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d
if e > maior:
    maior = e
print(f'O maior número é: {maior}')



#exercicio 18
a = int(input('Número 1: '))
b = int(input('Número 2: '))
c = int(input('Número 3: '))
d = int(input('Número 4: '))
e = int(input('Número 5: ' ))
print('Soma:',a+b+c+d+e)
print('Média:',(a+b+c+d+e)/5)

#exercicio 19
for i in range(1,51,2):
    print(i)



#Exercicio 20
a = int(input('menor número --- '))
b = int(input('maior número ---'))
for i in range(a,b):
    print(i)