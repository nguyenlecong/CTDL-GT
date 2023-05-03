from utils import san_sinh_mang


def sap_xep_nhanh(mang):
    if len(mang) > 1:
        nho_hon = []
        bang = []
        lon_hon = []

        p = mang[0]
        for x in mang:
            if x < p:
                nho_hon.append(x)
            elif x == p:
                bang.append(x)
            else:
                lon_hon.append(x)

        return sap_xep_nhanh(nho_hon) + bang + sap_xep_nhanh(lon_hon)

    else:
        return mang


def main():
    mang = san_sinh_mang(10)
    print('Mang ban dau la:\n', mang)

    mang = sap_xep_nhanh(mang)
    print('Mang sau khi sap xep la:\n', mang)


if __name__ == '__main__':
    main()
