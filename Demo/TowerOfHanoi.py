def move(n, x, y, z):
    if n == 1:
        print x + '-->' + z
        return
    move(n - 1, x, z, y)
    print x + '-->' + z
    move(n - 1, y, x, z)

move(5, 'A', 'B', 'C')