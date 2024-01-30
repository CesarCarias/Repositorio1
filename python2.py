name = input('Cual es su nombre?:').title()
print(f'Hola {name}')

week_day = input('En que dia deseas entrar a la discoteca?: ').lower().strip()

if (week_day == 'viernes') or (week_day == 'sabado'):
    print(f'Muy bien, es {week_day}')
    time = int(input('A que hora quieres ingresar?: '))

    if 25 > time > 19:
        print(f'Muy bien, esta en el rango horario indicado')
        age = int(input('Cuantos años tiene: '))

        if age >= 18:
            print(f'Bienvenido {name}, pase adelante')

        else:
            print('No tiene suficiente edad')

    else:
        print('La discoteca esta cerrada')

else:
        print('La discoteca esta cerrada hoy')