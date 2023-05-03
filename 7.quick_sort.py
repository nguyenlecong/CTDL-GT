from utils import san_sinh_mang


def phan_vung(mang, duoi, tren):
    i = duoi - 1  # chi muc cua phan tu nho hon moc
    moc = mang[tren]  # pivot
    # Dua lan luot cac phan tu nho hon moc len tren
    for j in range(duoi, tren):
        if mang[j] < moc:
            i = i + 1
            mang[i], mang[j] = mang[j], mang[i]

    mang[i+1], mang[tren] = mang[tren], mang[i+1]

    return i+1


def sap_xep_nhanh(mang, duoi, tren):
    if duoi < tren:
        vitri = phan_vung(mang, duoi, tren)

        sap_xep_nhanh(mang, duoi, vitri-1)
        sap_xep_nhanh(mang, vitri+1, tren)


def main():
    mang = san_sinh_mang(10)
    print('Mang ban dau la:\n', mang)

    sap_xep_nhanh(mang, 0, len(mang)-1)
    print('Mang sau khi sap xep la:\n', mang)


if __name__ == '__main__':
    main()
