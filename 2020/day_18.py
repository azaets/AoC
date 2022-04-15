import re

def e_is_numb(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

def calculate(expr):
    act = None
    numb1 = None
    parenth_numb = [numb1]
    parenth_act = [act]
    parenth_count = 0

    for idx, e in enumerate(expr):
        if e_is_numb(e):
            if parenth_numb[parenth_count] is None:
                parenth_numb[parenth_count] = int(e)
            else:
                if parenth_act[parenth_count] == 'SUM':
                    parenth_numb[parenth_count] += int(e)
                elif parenth_act[parenth_count] == 'MULT':
                    parenth_numb[parenth_count] *= int(e)
        elif e == '+':
            parenth_act[parenth_count] = 'SUM'
        elif e == '*':
            parenth_act[parenth_count] = 'MULT'
        elif e == '(':
            if parenth_numb[parenth_count] is not None:
                parenth_numb.append(None)
                parenth_act.append(None)
                parenth_count += 1
            else:
                parenth_numb[parenth_count] = 0
                parenth_act[parenth_count] = 'SUM'
                parenth_numb.append(None)
                parenth_act.append(None)
                parenth_count += 1

        elif e == ')':
            if parenth_numb[parenth_count] is not None:
                parenth_count -= 1
                if parenth_act[parenth_count] == 'SUM':
                    parenth_numb[parenth_count] += parenth_numb.pop()
                elif parenth_act[parenth_count] == 'MULT':
                    parenth_numb[parenth_count] *= parenth_numb.pop()

                parenth_act.pop()

    return parenth_numb[0]

def calculate2(expr):
    act = None
    numb1 = None
    parenth_numb = [numb1]
    parenth_act = [act]
    parenth_count = 0

    for idx, e in enumerate(expr):
        if e_is_numb(e):
            if parenth_numb[parenth_count] is None:
                parenth_numb[parenth_count] = int(e)
            else:
                if parenth_act[parenth_count] == 'SUM':
                    parenth_numb[parenth_count] += int(e)
                elif parenth_act[parenth_count] == 'MULT':
                    parenth_numb[parenth_count] *= int(e)
        elif e == '+':
            parenth_act[parenth_count] = 'SUM'
        elif e == '*':
            parenth_act[parenth_count] = 'MULT'
        elif e == '(':
            if parenth_numb[parenth_count] is not None:
                parenth_numb.append(None)
                parenth_act.append(None)
                parenth_count += 1
            else:
                parenth_numb[parenth_count] = 0
                parenth_act[parenth_count] = 'SUM'
                parenth_numb.append(None)
                parenth_act.append(None)
                parenth_count += 1

        elif e == ')':
            if parenth_numb[parenth_count] is not None:
                parenth_count -= 1
                if parenth_act[parenth_count] == 'SUM':
                    parenth_numb[parenth_count] += parenth_numb.pop()
                elif parenth_act[parenth_count] == 'MULT':
                    parenth_numb[parenth_count] *= parenth_numb.pop()

                parenth_act.pop()

    return parenth_numb[0]


def part_2(data):
    class num(int):
        def __sub__(self, b):
            return num(int(self) * int(b))

        def __mul__(self, b):
            return num(int(self) + int(b))

    out = 0
    for d in data:
        d = d.replace('*', '-')
        d = d.replace('+', '*')
        d = re.sub('(\d+)', r'num(\1)', d)
        out += eval(d)
    return out

    # print(data)
    # out = 0
    #
    # from copy import deepcopy
    #
    # for d in data:
    #     d = [_ for _ in d]
    #     new_exp = deepcopy(d)
    #
    #     p_left_count = 0
    #     p_right_count = 0
    #
    #     i = 0
    #     while i < len(new_exp):
    #         # new_exp = deepcopy(d)
    #         if d[i] == '+':
    #             if p_left_count == 0:
    #                 new_exp.insert(i-1, '(')
    #             elif p_left_count == p_right_count:
    #                 pass
    #             else:
    #                 i_left_p = i
    #                 while p_left_count != 0:
    #                     if new_exp[i_left_p] == '(':
    #                         p_left_count -= 1
    #                     i_left_p -= 1
    #                 new_exp.insert(i_left_p, '(')
    #
    #             i += 2
    #
    #         elif d[i] == '(':
    #             p_left_count += 1
    #         elif d[i] == ')':
    #             p_right_count += 1
    #
    #         i += 1
    # return out


def part_1(data):
    # print(data)
    out = 0

    for d in data:
        out += calculate(d)

    return out


if __name__ == '__main__':
    with open('input/18.txt') as f:
        _lines = [_.replace(' ', '') for _ in f.read().splitlines()]

    print(part_1(_lines))
    print(part_2(_lines))