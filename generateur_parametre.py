from random import randint,choice
from configs.confing_setting import carac_sub


def get_random_carac_spe(default_string=False):
    """
    les caractères de la variable carac_special auront
    un nombre de carcatères plus petite.

    Si default_string est vraie les carcatères ne seront pas choisit
    de manière pseudo aléatoire
    
    liste des lettres fréquentes en français / englais:
    fr: e a s i n t r l u o d c h p
    """

    default_carac_spe = "easintrluodchPEASINTRLUODCHP"

    if default_string is True:
        return default_carac_spe
    else:
        carac_special = ""
        n = int(len(carac_sub)/2)

        for e in range(n):
            carac_special = carac_special + choice(carac_sub)
        
        return carac_special 


def gen(db):
    """
    Génère des paramètres aléatoires
    """

    min_lenght_carc = 4
    max_lenght_carc = randint(min_lenght_carc+1,8)

    min_lenght_carac_special = 3
    max_lenght_carac_special = min_lenght_carc

    min_nbr_key = 3
    max_nbr_key = randint(min_nbr_key+1,100)

    min_add_carac_b = 24
    max_add_carac_b = randint(min_add_carac_b+1,200)

    min_len_carac_group_b = randint(4,5)
    max_len_carac_group_b = randint(min_len_carac_group_b,10)

    rolling_min = 100
    rolling_max = 500

    text = f"""
        "cipher": "ascii_letters",
        "carac_special": "{get_random_carac_spe(default_string=(False,True))}",
        "substitue with": "configs/{db}",
        "cipher punctuation": "true",
        "cipher accent": "true",
        "cipher digits": "true",
        "len_caractere": [{min_lenght_carc},{max_lenght_carc}],
        "len_carac_special": [{min_lenght_carac_special},{max_lenght_carac_special}],
        "nombre_cle": [{min_nbr_key},{max_nbr_key}],
        "len_carac_group_b":[{min_len_carac_group_b},{max_len_carac_group_b}],
        "mini": {min_add_carac_b},
        "maxi": {max_add_carac_b},
        "rolling":{randint(rolling_min,rolling_max)}
    """

    return "{\n"+text+"\n}"


def get_random_setting(db):
    f = open("configs/setting.json", "w")
    f.write(gen(db))
    f.close()





