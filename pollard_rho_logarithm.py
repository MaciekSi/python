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


# calculate value of X based on alfas and betas from collision
def count_X(alfa1, beta1, alfa2, beta2, _p):
    beta_dif = float((beta2-beta1) % (_p-1))
    alfa_dif = float(alfa1-alfa2)
    while (beta_dif / alfa_dif) % 1.0 != 0.0:
        beta_dif = float(beta_dif + (_p-1))
    return int(beta_dif / alfa_dif)


def pollard_rho(sets, _y, _g, _p):
    # alfa- power of _y value
    alfa = 0
    # beta- power of _g value
    beta = 10

    A = ((_g ** beta) * (_y ** alfa)) % _p
    while True:
        set_number = A % 3
        # if no collision detected values are added to sets as values with unique key
        values_tosave = (alfa, beta)
        A_tosave = A

        if set_number == 0:
            if A in sets.S0.keys():
                (_alfa, _beta) = sets.S0[A]
                return count_X(alfa, beta, _alfa, _beta, _p)
            else:
                alfa = alfa + 1
                beta = beta
                A = A * _y % _p

        if set_number == 1:
            if A in sets.S1.keys():
                (_alfa, _beta) = sets.S1[A]
                return count_X(alfa, beta, _alfa, _beta, _p)
            else:
                alfa *= 2
                beta *= 2
                A = A ** 2 % _p

        if set_number == 2:
            if A in sets.S2.keys():
                (_alfa, _beta) = sets.S2[A]
                return count_X(alfa, beta, _alfa, _beta, _p)
            else:
                alfa = alfa
                beta = beta + 1
                A = A * _g % _p

        sets.addToGroup(set_number, A_tosave, values_tosave)


if __name__ == '__main__':
    _g = 3
    _y = 48
    _p = 101
    print(pollard_rho(Sets(), _y, _g, _p))
