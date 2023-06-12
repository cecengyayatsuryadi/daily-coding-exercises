confidence = input("Apakah anda bersemangat menjalani hidup? (y/n) ")


def pilihan_hidup(confidence):
    if confidence:
        return "Mode hard"
    else:
        return "Mode easy"


print(pilihan_hidup(True))
