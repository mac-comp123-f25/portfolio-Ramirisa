def name_subst(name, text):
    return text.replace("ZZZ", name)
result = name_subst("Zay", "Whatup ZZZ, good stuff yesterday")
print(result)