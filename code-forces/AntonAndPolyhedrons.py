from functools import reduce

polyhedrons = int(input())
shapes = [input() for i in range(polyhedrons)]
faces = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}

print(reduce(lambda x, y: x + y, list(map(lambda x: faces[x], shapes))))
