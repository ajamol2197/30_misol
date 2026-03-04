# 1
def son(a):
    if a > 0:
        return "musbat"
    else:
        return "musbat yoki nol"


y = son(-3)
print(y)


# 2
def son(a):
    if a == 2:
        return "True"
    else:
        return "false"


t = son(2)
print(t)

# 3
def son(a):
    if a > 100:
        return "katta"
    else:
        return "kichik"


y = son(345)
print(y)

# 4
def son(a, b):
    if a == b:
        return "teng"
    else:
        return "teng emas"


y = son(9, 9)
print(y)

# 5
def yosh(a):
    if a >= 18:
        return "ruxsat beriladi"
    else:
        return "ruxsat berilmaydi"


y = yosh(17)
print(y)

# 6
def son(a):
    if a == 0:
        return "nol"
    else:
        return "nol emas"


y = son(0)
print(y)

# 7
def harf(a):
    if a.isupper():
        return "katta harf"
    else:
        return "kichik harf"


y = harf("i")
print(y)

# 8
def parol(a):
    if a < 8:
        return "juda qisqa"
    else:
        return "qabul qilindi"


y = parol(7)
print(y)

# 9
def matn(a):
    if a == " ":
        return "bosh matn"
    else:
        return "matn mavjud"

y = matn(0 )
print(y)

# 10
def son(a):
    if 10 > a < 20:
        return "oraliq"
    else:
        return "oraliq emas"


y = son(89)
print(y)


# 11
def ism(a):
    if a == "admin":
        return "xush kilibsiz admid"
    else:
        return "oddiy foydalanuvchi"


y = ism("admin")
print(y)

# 12
def matn(a):
    if a == "salom":
        return "salomlashuv bor"
    else:
        return "salomlashuv yoq"


y = matn("salom")
print(y)

# 13
def harf(a):
    if a[-1] == "a":
        return "true"

    return "false"


y = harf("slaa")
print(y)

# 14
def soz(a):
    if a > 5:
        return "Uzun so‘z"
    else:
        return "qisqa soz"


y = soz(6)
print(y)

# 15
def log(a):
    if a == " ":
        return "xato login"

    return "togri login"


y = log(" ")
print(y)

# 16
def son(a):
    if a / 2 and a / 3:
        return "mos keladi"
    else:
        return "mos emas"


y = son(6)
print(y)

# 17
def emile(a):
    if a != "@":
        return "Noto‘g‘ri emaie"

    return "togri"


y = emile("aldchb")
print(y)

# 18
def san(a):
    if a.isdight:
        return "raqam bor"

    return "raqam yoq"


y = san("afxcd1")
print(y)

# 19
def par(a):
    if a.isalpha():
        return "faqat harf"

    return "boshqa belgilar bor"


y = par("hgfxcvbnj678vr")
print(y)

# 20
def ism(a):
    if a[1] == "a":
        return "ism xato yozlgan"

    return "togri yozilgan"


y = ism("Alo")
print(y)


# 21
def baho(a):
    if 90 <= a < 100:
        return "A"
    elif 70 <= a < 89:
        return "B"
    elif 50 <= a < 69:
        return "C"
    else:
        return "yiqildi"


y = baho(87)
print(y)

# 22
def oy(a):
    if a == 12 and a == 1 and a == 2:
        return "qish"

    return "qish emas"


y = oy(11)
print(y)

# 23
def son(a, b):
    if a > b:
        return "1-son katta"

    return "2- son katta yoki teng"


y = son(12, 23)
print(y)

# 24
def pill(a):
    if a[::-1]:
        return "pilidrom"

    return "pilidrom emas"


y = pill("alla")
print(y)

# 25
def par(a, b):
    if a == "user" and b == 1234:
        return "Tizimga kirdi"

    return "xato"


y = par("user", 1234)
print(y)

# 26
def son(a):
    if a == 2:
        return " musbat juft "
    else:
        return "boshqa"


y = son(2)
print(y)

# 27
def harf(harf):
    unlilar = "aeiouAEIOUo‘O‘"

    if harf in unlilar:
        return "Unli"
    else:
        return "Undosh"


print(harf("a"))

# 28
def matn(matn):
    if matn.islower() and matn.isalpha():
        return "Faqat kichik harf"
    else:
        return "Boshqa belgilar bor"


print(matn("salom"))

# 29
def son(a, b):
    if a > 0 and b > 0:
        return "Ikkalasi ham musbat"
    else:
        return "Kamida bittasi manfiy yoki nol"

y = son(5, 3)
print(y)

# 30
def son(a):
    if a < 0:
        return "manfiy"
    elif a == 0:
        return "nol"

    return "musbat"


y = son(9)
print(y)
