from urllib.request import urlopen
from bs4 import BeautifulSoup
def tabla_campeonato():
    nombres = []
    victorias = []
    empates = []
    derrotas = []
    puntos = []
    Goles_a_favor = []
    Goles_en_contra = []
    Goles_totales = []
    print('¿ Desea introducir equipos predeterminados ?')
    opcion = input().upper()

    print('¿ Cuantos equipos pertenecen a la liga ?')
    print('Recuerda que tu liga puede ser de maximo 20 equipos')
    equipos = int(input())

    if opcion == 'SI':
        print('Ingrese el url de la pagina....')
        url = input()
        url = str(url)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        titulares = soup.find_all(True, {'class':['d-none d-md-inline']})
        nombres = list(titulares)
        cad = ''
        limit = 0
        acum = ''
        nom = ''
        lista = []
        for i in range(len(nombres)):
            cad += str(nombres[i])
        for i in range(len(cad)):
            if i == 0:
                continue
            elif ord(cad[i]) == 62:
                limit += 1
            elif ord(cad[i]) == 60:
                limit -= 1
                acum += ' '
            elif limit == 1:
                acum += str(cad[i])
        for i in range(len(acum)):
            if i == 0:
                nom += acum[i]
            elif ord(acum[i]) == 32 and ord(acum[i-1]) == 32:
                nom = nom[:-1]
                lista.append(nom)
                nom = ''
            else:
                nom += acum[i]
        if equipos > 0 and equipos < 21:
            for i in range(equipos):
                print('Ingrese el numero de partidos jugados por {}'.format(lista[i]))
                partidos = int(input())
                print('ahora ingresa el numero de victorias, empates y derrotas del equipo')
                print('Recuerde ingresar tres datos distintos, no seguidos')
                v = int(input())
                victorias.append(v)
                e = int(input())
                empates.append(e)
                d = int(input())
                derrotas.append(d)
                total = v + e + d
                if total == partidos:
                    print('ahora ingresa el numero de goles a favor y goles en contra de tu equipo')
                    print('Recuerde ingresar dos datos distintos, no seguidos')
                    ga = int(input())
                    Goles_a_favor.append(ga)
                    gf = int(input())
                    Goles_en_contra.append(gf)
                    pts = (v * 3) + (e * 1) + (d * 0)
                    puntos.append(pts)
                    gt = ga - gf
                    Goles_totales.append(gt)
                else:
                    print('Los numeros no coinciden, intente de nuevo')
            Posiciones = []
            while len(puntos) != 0:
                i = 0
                mayor = puntos[0]
                while i < len(puntos):
                    if puntos[i] > mayor:
                        mayor = puntos[i]
                        i += 1
                    else:
                        i += 1
                Posiciones.append(mayor)
                puntos.remove(mayor)
            print('{}{:^15}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Nombre de equipo', 'victorias', 'empates', 'derrotas', 'G/A', 'G/C', 'G/T'))
            for j in range(0, equipos):
                print('{}{:^20}{:^12}{:^12}{:^8}{:^8}{:^8}'.format(nombres[j], victorias[j], empates[j], derrotas[j], Goles_a_favor[j], Goles_en_contra[j], Goles_totales[j]))
            Mas_goles = []
            while len(Goles_a_favor) != 0:
                i = 0
                mayor = Goles_a_favor[0]
                while i < len(Goles_a_favor):
                    if Goles_a_favor[i] > mayor:
                        mayor = Goles_a_favor[i]
                        i += 1
                    else:
                        i += 1
                Mas_goles.append(mayor)
                Goles_a_favor.remove(mayor)
            Menos_goles = []
            while len(Goles_en_contra) != 0:
                i = 0
                mayor = Goles_en_contra[0]
                while i < len(Goles_en_contra):
                    if Goles_en_contra[i] > mayor:
                        mayor = Goles_en_contra[i]
                        i += 1
                    else:
                        i += 1
                Menos_goles.append(mayor)
                Goles_en_contra.remove(mayor)
            print('A partir de estos datos, podemos concluir que....')
            print('La mayor cantidad de goles anotados fue {} y la menor cantidad fue {}'.format(Mas_goles[0], Mas_goles[-1]))
            print('La mayor cantidad de goles recibidos fue {} y la menor cantidad fue {}'.format(Menos_goles[0], Menos_goles[-1]))
            print('La mayor cantidad de puntos fue {} y la menor cantidad fue {}'.format(Posiciones[0], Posiciones[-1]))
        else:
            print('Este numero excede la cantidad de datos, ingrese otro numero')
    elif opcion == 'NO':    
        if equipos > 0 and equipos < 21:
            for i in range(1, equipos + 1):
                print('Ingresa el nombre del {}° equipo'.format(i))
                nombre = input()
                nombres.append(nombre)
                print('Ingrese el numero de partidos jugados por el equipo')
                partidos = int(input())
                print('ahora ingresa el numero de victorias, empates y derrotas del equipo')
                print('Recuerde ingresar tres datos distintos, no seguidos')
                v = int(input())
                victorias.append(v)
                e = int(input())
                empates.append(e)
                d = int(input())
                derrotas.append(d)
                total = v + e + d
                if total == partidos:
                    print('ahora ingresa el numero de goles a favor y goles en contra de tu equipo')
                    print('Recuerde ingresar dos datos distintos, no seguidos')
                    ga = int(input())
                    Goles_a_favor.append(ga)
                    gf = int(input())
                    Goles_en_contra.append(gf)
                    pts = (v * 3) + (e * 1) + (d * 0)
                    puntos.append(pts)
                    gt = ga - gf
                    Goles_totales.append(gt)
                else:
                    print('Los numeros no coinciden, intente de nuevo')
            Posiciones = []
            while len(puntos) != 0:
                i = 0
                mayor = puntos[0]
                while i < len(puntos):
                    if puntos[i] > mayor:
                        mayor = puntos[i]
                        i += 1
                    else:
                        i += 1
                Posiciones.append(mayor)
                puntos.remove(mayor)
            print('{}{:^15}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Nombre de equipo', 'victorias', 'empates', 'derrotas', 'G/A', 'G/C', 'G/T'))
            for j in range(0, equipos):
                print('{}{:^20}{:^12}{:^12}{:^8}{:^8}{:^8}'.format(nombres[j], victorias[j], empates[j], derrotas[j], Goles_a_favor[j], Goles_en_contra[j], Goles_totales[j]))
            Mas_goles = []
            while len(Goles_a_favor) != 0:
                i = 0
                mayor = Goles_a_favor[0]
                while i < len(Goles_a_favor):
                    if Goles_a_favor[i] > mayor:
                        mayor = Goles_a_favor[i]
                        i += 1
                    else:
                        i += 1
                Mas_goles.append(mayor)
                Goles_a_favor.remove(mayor)
            Menos_goles = []
            while len(Goles_en_contra) != 0:
                i = 0
                mayor = Goles_en_contra[0]
                while i < len(Goles_en_contra):
                    if Goles_en_contra[i] > mayor:
                        mayor = Goles_en_contra[i]
                        i += 1
                    else:
                        i += 1
                Menos_goles.append(mayor)
                Goles_en_contra.remove(mayor)
            print('A partir de estos datos, podemos concluir que....')
            print('La mayor cantidad de goles anotados fue {} y la menor cantidad fue {}'.format(Mas_goles[0], Mas_goles[-1]))
            print('La mayor cantidad de goles recibidos fue {} y la menor cantidad fue {}'.format(Menos_goles[0], Menos_goles[-1]))
            print('La mayor cantidad de puntos fue {} y la menor cantidad fue {}'.format(Posiciones[0], Posiciones[-1]))
        else:
            print('Este numero excede la cantidad de datos, ingrese otro numero')
    else:
        print('opcion incorrecta, por favor reinicia el programa')
tabla_campeonato()
