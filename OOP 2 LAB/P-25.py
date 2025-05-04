
dict1 = {'Tausif': 85, 'Mursalin': 75, 'Moho': 90}
dict2 = {'Tausif': 95, 'Rafi': 80, 'Mursalin': 65}


merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value


print(f"Merged dictionary : {merged_dict}")
