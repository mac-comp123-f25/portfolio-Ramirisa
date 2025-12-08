def apply_l_system(system_dict):

    assert type(system_dict) is dict, "Input must be a dictionary."


    assert len(system_dict) == 3, "Dictionary must have exactly 3 entries."


    assert "axiom" in system_dict, "Missing key: axiom"
    assert "rules" in system_dict, "Missing key: rules"
    assert "n" in system_dict, "Missing key: n"


    axiom = system_dict["axiom"]
    rules = system_dict["rules"]
    n = system_dict["n"]


    current = axiom
    for _ in range(n):
        new_string = ""
        for ch in current:
            if ch in rules:
                new_string += rules[ch]
            else:
                new_string += ch
        current = new_string

    return current
