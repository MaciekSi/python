class Sets:
    S0 = {}
    S1 = {}
    S2 = {}

    def addToGroup(self, group_number, A, values):
        if group_number == 0:
            self.S0[A] = values
        if group_number == 1:
            self.S1[A] = values
        if group_number == 2:
            self.S2[A] = values


def extended_euclid(num1, num2):
    if num2 == 0:
        return num1, 1, 0
    else:
        gcd, inv, division_rest = extended_euclid(num2, num1 % num2)
        new_inv = division_rest
        new_div_rest = inv - (num1 / num2) * division_rest
        return gcd, new_inv, new_div_rest


def modular_inverse(number, field):
    gcd, mod_inv, division_rest = extended_euclid(number, field)
    return mod_inv % field


def count_X(alfa1, beta1, alfa2, beta2, order):
    alfa_dif = (alfa1 - alfa2) % order
    beta_dif = (beta2 - beta1) % order
    alfa_dif_mod_inv = modular_inverse(alfa_dif, order)
    result = (beta_dif * alfa_dif_mod_inv) % order
    if ((_g**result) % _p) == _y:
        return result
    else:
        return result + order


# returns x value for equation: _g^x = _y (mod _p) for _p being strong prime number (_p = 2 * _p` + 1)
def pollard_rho(sets, _y, _g, _p):
    # alfa- power of _y value
    alfa = 0
    # beta- power of _g value
    beta = 0

    if ((float(_p) - 1.0) / 2.0) % 1.0 != 0.0:
        return -1
    _p_order = (_p - 1) / 2

    A = ((_g ** beta) * (_y ** alfa)) % _p

    i = 0
    while i < _p_order:
        set_number = A % 3
        # if no collision detected values are added to sets as values with unique key
        values_tosave = (alfa, beta)
        A_tosave = A

        if set_number == 0:
            if A in sets.S0.keys():
                (_alfa, _beta) = sets.S0[A]
                return count_X(alfa, beta, _alfa, _beta, _p_order)
            else:
                alfa = (alfa * 2) % _p_order
                beta = (beta * 2) % _p_order
                A = (A ** 2) % _p

        if set_number == 1:
            if A in sets.S1.keys():
                (_alfa, _beta) = sets.S1[A]
                return count_X(alfa, beta, _alfa, _beta, _p_order)
            else:
                alfa = alfa + 1 % _p_order
                beta = beta
                A = (A * _y) % _p

        if set_number == 2:
            if A in sets.S2.keys():
                (_alfa, _beta) = sets.S2[A]
                return count_X(alfa, beta, _alfa, _beta, _p_order)
            else:
                alfa = alfa
                beta = (beta + 1) % _p_order
                A = (A * _g) % _p

        sets.addToGroup(set_number, A_tosave, values_tosave)
        i += 1
    return -2


if __name__ == '__main__':
    _g = 2
    _y = 21
    _p = 107
    print(pollard_rho(Sets(), _y, _g, _p))
