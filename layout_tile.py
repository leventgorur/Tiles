# ROOM_SIZE = [69.5, 73]
# GROUT_SIZE = 0.25
# TOLERANCE_X = 0.25
# TOLERANCE_Y = 0.25
# PACKAGE_TILES = {"A":2,"B":2,"C":1,"D":2}

# A = [16, 24]
# B = [16, 16]
# C = [8, 16]
# D = [8, 8]

# TILE_TYPES = [A, B, C, D]

# def min_package():
#     min = 0
#     for i in TILE_TYPES:
#         min += min_tile(TILE_TYPES(i)) * int(PACKAGE_TILES[TILE_TYPES(i)])
#     return

# def min_tile(x):
#     print(min(x))
#     #return(y)


# min_package()


ROOM_SIZE = [69.5, 73]
GROUT_SIZE = 0.25
TOLERANCE_X = 0.25
TOLERANCE_Y = 0.25
PACKAGE_TILES = {"A":2,"B":2,"C":1,"D":2}

A = [16, 24]
B = [16, 16]
C = [8, 16]
D = [8, 8]

TILE_TYPES = [A, B, C, D]
"""
You can find the greatest common diviser in each side x and y

8 is the OBEB in our case
Draw a room and allow tiles in 8 by 8 to be placed.

"""
def min_package():
    min = 0
    for i in TILE_TYPES:
        x = TILE_TYPES[i]
        y = int(PACKAGE_TILES[x])
        print(x,y)
        min += min_tile(x) * y 
    return

def min_tile(x):
    print(min(x))
    #return(y)


def main():
    print("PACKAGE_TILES: ", PACKAGE_TILES)
    print(PACKAGE_TILES.keys())
    print("LIST(keys): ",list(PACKAGE_TILES.keys()))
    print(PACKAGE_TILES.values())
    print("LIST(values): ", list(PACKAGE_TILES.values()))
    print()
    print("TILE_TYPES: ", TILE_TYPES)
    print("TILE_TYPES[2]: ", TILE_TYPES[2])
    print("min(TILE_TYPES[2]): ", min(TILE_TYPES[2]))
    print("max(TILE_TYPES[2]): ", max(TILE_TYPES[2]))
    print("A", A)
    print("min(A)",min(A))

if __name__ == "__main__":
    main()


