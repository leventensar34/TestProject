"""
Elinizde uzunca bir string olsun.

 "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

"""
satir = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

frekans = dict()

for karakter in satir:
    if (karakter in frekans):
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i, j in frekans.items():
    print(i, ":", j)
