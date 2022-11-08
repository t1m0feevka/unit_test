###1###
def func1(a, b, list):

    for i in a:
        if i in b:
            if i in list:
                continue
            list.append(i)
    return list


print(func1([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], []))

###2###

def func2(text):

    s = 0
    text_split = text.split()
    for i in text_split:
        if 'a' in i:
            s += 1
    return s


print(func2('I am a good developer. I am also a writer'))

# ###3###


def func3(g):

    if g % 3 == 0:
        g /= 3

    return g == 3


print(func3(9))
