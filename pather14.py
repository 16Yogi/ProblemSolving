for i in range(ord('a'),ord('f')):
    for j in range(ord('a'),ord('f')-(i-ord('a'))):
        print(chr(j),end="")
    print("")