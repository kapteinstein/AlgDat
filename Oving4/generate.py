import random
from sys import argv

def main():
    try:
        antall = int(argv[1])
        maks   = int(argv[2])
    except:
        antall = 100
        maks   = 100

    l = [random.randint(0, maks) for i in range(antall)]

    f = open('dataset.txt', 'w')
    f.write(' '.join(map(str, l)))
    #f.write(str(l).strip('[]').strip(','))
    f.close();

if __name__ == '__main__':
    main()
