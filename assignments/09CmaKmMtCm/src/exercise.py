def main():
    # Escribe tu código abajo de esta línea
    num = int(input("Introduce los cm: "))
    if num<100:
        print(num,"cm")
    elif num<1000:
        x=num//100
        y=num-(x*100)
        print(x,"m")
        if y!=0:
            print(y,"cm")
    else:
        x=num//100000
        y=(num-(x*100000))//100
        z=(num-(x*100000)-(y*100))
        if x!=0:
            print(x,"km")
        if y!=0:
            print(y,"m")
        if z!=0:
            print(z,"cm")

if __name__ == '__main__':
    main()
