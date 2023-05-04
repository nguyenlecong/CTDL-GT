def main():
    bangbam = dict()
    import random
    for _ in range(15):
        khoa = random.randint(0, 10)
        gia_tri = random.randint(0, 100)
        bangbam[khoa] = gia_tri
        print(bangbam)

    khoa = int(input("Nhap vao mot khoa: "))
    gia_tri = bangbam[khoa]
    print(gia_tri)


if __name__ == '__main__':
    main()
