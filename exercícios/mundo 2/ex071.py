print('='*40)
print(f'{"BANCO CEV":^40}')
print('='*40)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:

        if totced > 0:
            print(f'Total de {totced} células  de R$ {ced}')
        if ced == 50:
            ced = 20
            totced
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

