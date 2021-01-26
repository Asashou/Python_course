def roman_to_num(roman: str):
    look_up = {'I':1, 'V':5, "X":10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num = 0
    for ind, l in enumerate(roman):
        try:
            value = look_up[l]
            try:
                next = roman[ind + 1]
                if value < look_up[next]:
                    value = -1 * value
            except:
                value = value

            num += value
        except:
            raise TypeError('The provided Roman number cannot be recognized')

    return num

