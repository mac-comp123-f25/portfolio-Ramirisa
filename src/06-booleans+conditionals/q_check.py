def has_q(x):
    if 'q' in x:
        result = True
    else:
        result = False
    return result

print(has_q('quest'))

if _name_ == "_main_":
    assert has_q("quick") ==True
    assert has_q("math") == False
    print ("All tests passed")



























