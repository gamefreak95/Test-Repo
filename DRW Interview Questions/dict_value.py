def get_dict_value(dct, path):
    keys = path.split(".")
    #print(keys)
    current = dct
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
            print("this is the key: "+ key + " and this is the value: " + str(current))
        else:
            return None
    return current

dct = {"a": {"b": {"c": {"d": 42}}}}
result1 = get_dict_value(dct, "a.b.c")    # ➞ 42
result2 = get_dict_value(dct, "a.b.c.d")
result3 = get_dict_value(dct, "a.c.d")

print(result1)
print(result2)
print(result3)