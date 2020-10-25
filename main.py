import random, string

amount = int(input('Quantidade de códigos nitro para gerar: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codigos.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GERADO] {code}')
    value += 1
