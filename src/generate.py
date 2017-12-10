from sys import argv
from random import randint

def makeconfig(f):
    """
    Generates a config file at random.
    """
    ALPHABETSIZE = 26
    rotorcount = randint(3, 5)
    for i in range(rotorcount):
        f.write("ROTOR =")
        rotor = []
        while len(rotor) < ALPHABETSIZE:
            c = randint(0, 25)
            if c not in rotor:
                rotor.append(c)
        for j in rotor:
            f.write(" " + str(j))
        f.write("\n")

    notches = []
    for i in range(rotorcount - 1):
        notches.append(randint(0, ALPHABETSIZE - 1))
    f.write("NOTCHES =")
    for i in notches:
        f.write(" " + str(i))
    f.write("\n")

    reflector = [-1 for i in range(ALPHABETSIZE)]
    for i in range(len(reflector)):
        if reflector[i] == -1:
            c = randint(0, ALPHABETSIZE - 1)
            while c in reflector:
                c = randint(0, ALPHABETSIZE - 1)
            reflector[i] = c
            reflector[c] = i
    f.write("REFLECTOR =")
    for i in reflector:
        f.write(" " + str(i))
    f.write("\n")

    plugboard = []
    while len(plugboard) < ALPHABETSIZE:
        c = randint(0, ALPHABETSIZE - 1)
        if c not in plugboard:
            plugboard.append(c)
    f.write("PLUGBOARD =")
    for i in plugboard:
        f.write(" " + str(i))
    f.write("\n")

if __name__ == "__main__":
    if len(argv) < 2:
        print("Use generator as generator OUTPUT")
        exit()

    f = open(argv[1], 'w')
    makeconfig(f)
    f.close()
