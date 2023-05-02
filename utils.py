import random


def san_sinh_mang(n):
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(-100, 100)
        mang.append(so_ngau_nhien)

    return mang


def san_sinh_mang_tang_dan(n):
    mang = []
    so_dang_nhien = random.randint(-100, 100)
    mang.append(so_dang_nhien)

    for i in range(1, n):
        tang = random.randint(0, 10)
        so = mang[i-1] + tang
        mang.append(so)

    return mang
