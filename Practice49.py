merged_dict = d1.copy()
    for key, value in d2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
