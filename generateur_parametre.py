from random import randint,choice

# Remplacer "ascii_letters" par choice(cip) si vous le voulez
#cip = ["ascii_lowercase","ascii_uppercase","ascii_letters"]


def gen(db):
    """
    """

    min_lenght_carc = 4
    max_lenght_carc = randint(min_lenght_carc+1,8)

    min_lenght_carac_special = 2
    max_lenght_carac_special = min_lenght_carc

    min_nbr_key = 3
    max_nbr_key = randint(min_nbr_key+1,100)

    min_add_carac_b = 99
    max_add_carac_b = randint(min_add_carac_b+1,800)

    text = f"""
        "cipher": "ascii_letters",
        "substitue with": "configs/{db}",
        "cipher punctuation": "true",
        "cipher space": true,
        "cipher accent": "true",
        "cipher digits": "true",
        "len_caractere": [{min_lenght_carc},{max_lenght_carc}],
        "len_carac_special": [{min_lenght_carac_special},{max_lenght_carac_special}],
        "nombre_cle": [{min_nbr_key},{max_nbr_key}],
        "mini": {min_add_carac_b},
        "maxi": {max_add_carac_b},
        "rolling":{randint(0,999)}
    """

    return "{\n"+text+"\n}"


def get_random_setting(db):
    f = open("configs/setting.json", "w")
    f.write(gen(db))
    f.close()
