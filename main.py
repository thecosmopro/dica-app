meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFFL": "bir şakaya karşılık cevap",
            "SHEESH": "Onaylamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek/Sinirlenmek"
}

kullanici_istek = input("Hangi kelimeyi soracaksın (Büyük Harflerle Yaz)?").upper()

if kullanici_istek in meme_dict.keys():
    print("Girdiğiniz kelimenin anlamı:", meme.dict[kullanici_istek])
    
else:
    print("Sözlükte Bu kelime yok")
