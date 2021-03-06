# Estruturas de repetição (loops)

a = 0
b = 10
letter = "python"
element = 5
var_list = [2,4,6,8,13]

# while
while a <= b:               # Enquant 0 for <= 10
    print(a)                # Imprima "a"
    a += 1                  # Soma +1 a cada loop

# for                       Variáveis de controle (a,b,i,j) podem ter qualquer nome válido
for i in range(10):         # i = 0 e range faz a contagem de 0 ao número colocado na função(nesse caso, 10)
    print (i)

for j in letter:            # "j" irá assumir uma letra de "python" a cada iteração, e o camando print o exibirá
    print(j,end="")

print("\n")                 # Quebra de linha para organização

# in / not in
print(element in var_list)      # element(5) está na lista?      False
print(element not in var_list)  # element(5) está fora da lista? True

print("\n")                 # Quebra de linha para organização

#  Lógica (and - or - not - xor)
number_1 = 0
number_2 = 10

print (number_1 < number_2 and number_2 != number_1)            # 0 é menor que 10? E 10 é diferente de 0?
print (number_1 < number_2 or number_2 != number_1)             # 0 é menor que 10? OU 10 é diferente de 0?
print (number_1 < number_2 and not(number_2 != number_1))       # 0 é menor que 10? E negar(10 é diferente de 0)?
print (number_1 < number_2 ^ number_2 == number_1)              # 0 é menor que 10? exclusivo ou 10 é igual a 0?
