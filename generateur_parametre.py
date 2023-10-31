from random import randint

def gen(db):
    """
    Génère des paramètres pseudo aléatoires
    """

    min_lenght_carc = 6
    max_lenght_carc = randint(min_lenght_carc+1,9)

    min_lenght_carac_special = 3
    max_lenght_carac_special = 6

    min_nbr_key = 3
    max_nbr_key = randint(min_nbr_key+1,50)

    min_add_carac_b = 24
    max_add_carac_b = randint(min_add_carac_b+1,100)

    min_len_carac_group_b = randint(4,5)
    max_len_carac_group_b = randint(min_len_carac_group_b,10)

    text = f"""
        "cipher": "ascii_letters",
        "carac_special": "easintrluodchEASINTRLUODCH0123456789!#$%&'()*+,-./:;<=>?\\"@[\\\]",
        "substitue_with": "configs/{db}",
        "cipher_punctuation": "True",
        "cipher_accent": "True",
        "cipher_digits": "True",
        "len_caractere": [{min_lenght_carc},{max_lenght_carc}],
        "len_carac_special": [{min_lenght_carac_special},{max_lenght_carac_special}],
        "nombre_cle": [{min_nbr_key},{max_nbr_key}],
        "len_carac_group_b":[{min_len_carac_group_b},{max_len_carac_group_b}],
        "mini": {min_add_carac_b},
        "maxi": {max_add_carac_b}
    """

    return "{\n"+text+"\n}"


def get_random_setting(db):
    f = open("configs/setting.json", "w")
    f.write(gen(db))
    f.close()


