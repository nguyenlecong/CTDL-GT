from utils import san_sinh_mang


def sap_xep_noi_bot(mang):
    n = len(mang)

    # for i in range(n):  # i = [0, n-1]
    #     tiep_tuc = False
    #     for j in range(n-2, i-1, -1):  # j = [n-2, i]
    #         if mang[j] > mang[j+1]:
    #             mang[j], mang[j+1] = mang[j+1], mang[j]
    #             tiep_tuc = True

    #     if tiep_tuc:
    #         print(i+1, '-', mang)

    #     if tiep_tuc == False:
    #         break

    for i in range(n-1, 0, -1):
        tiep_tuc = False
        for j in range(i):
            if mang[j] > mang[j+1]:
                mang[j], mang[j+1] = mang[j+1], mang[j]
                tiep_tuc = True
        if tiep_tuc:
            print(n-i, '-', mang)

        if tiep_tuc == False:
            break


def main():
    mang = san_sinh_mang(10)
    print('Mang ban dau la:\n', mang)

    sap_xep_noi_bot(mang)
    print('Mang sau khi sap xep la:\n', mang)


if __name__ == '__main__':
    main()
