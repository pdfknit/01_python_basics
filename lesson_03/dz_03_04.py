def thesaurus(*args):
    name_dict = {}
    for name in args:
        first_letter = name[0].title()
        if first_letter not in name_dict.keys():
            name_list = []
        else:
            name_list = name_dict.get(first_letter)
        name_list.append(name)
        name_dict[first_letter] = name_list

    return name_dict


def thesaurus_adv(*args):
    full_dict = {}
    full_name_list = list(args)

    for full_name in full_name_list:
        surname_1st_letter = full_name.split(' ')[1][0]
        full_dict[surname_1st_letter] = {}

    for surname_1st_letter in full_dict.keys():
        list_of_names = []
        for full_name in full_name_list:
            if full_name.split(' ')[1][0] == surname_1st_letter:
                list_of_names.append(full_name)
        full_dict[surname_1st_letter] = thesaurus(*list_of_names)

    # create sorted dictionary
    sorted_keys = sorted(full_dict.keys())
    sorted_full_dict = {}
    for key in sorted_keys:
        sorted_full_dict[key] = full_dict[key]

    return sorted_full_dict


args = ("Иван Иванов", "Мария Иванова", "Петр Осипов", "Илья Аитов", "Павел Гаврилов", "Пенни Ли", "Петр Петрович")
args_2 = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print('thesaurus\n', thesaurus(*args))
print('thesaurus_adv\n', thesaurus_adv(*args_2))
