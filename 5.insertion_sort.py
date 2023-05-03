from utils import san_sinh_mang


def sap_xep_chen(mang):
    n = len(mang)
    for i in range(1, n):
        tam = mang[i]
        j = i
        while j > 0 and mang[j-1] > tam:
            mang[j] = mang[j-1]
            j = j - 1

        mang[j] = tam
        print(i, '-', mang)


def main():
    mang = san_sinh_mang(10)
    print('Mang ban dau la:\n', mang)

    sap_xep_chen(mang)
    print('Mang sau khi sap xep la:\n', mang)


if __name__ == '__main__':
    main()
