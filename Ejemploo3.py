def rectangulo_area(largo, ancho):
    area1 = largo * ancho
    return area1
def triangulo_area(base, altura):
    area2 = 0.5 * base * altura
    return area2
def principal():
    x = 4
    y = 6
    print(f"Área del rectángulo: {rectangulo_area(x, y)}")

    b = 5
    h = 8
    print(f"Área del triángulo: {triangulo_area(b, h)}")

principal()
