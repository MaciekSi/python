from random import randint

_g = 3
_y = 44
_p = 101

class Sets:
    S0 = {}
    S1 = {}
    S2 = {}

    def addToGroup(self, group_number, A, values) :
        if group_number == 0:
            self.S0[A] = values
        if group_number == 1:
            self.S1[A] = values
        if group_number == 2:
            self.S2[A] = values


# returns value for provided alfa and beta
def count_A(alfa, beta):
    return ((_g ** beta) * (_y ** alfa)) % _p


def count_X(alfa1, beta1, alfa2, beta2):
    print(alfa1, alfa2, beta1, beta2, (beta1 - beta2) % (_p - 1))
    return ((beta1 - beta2) % (_p - 1)) / (alfa2 - alfa1)


def pollard_rho(sets):
    # alfa- power of _y value
    alfa = 0
    # beta- power of _g value
    beta = 10

    while True:
        A = count_A(alfa, beta)
        group_number = A % 3
        print("alfa:  " + str(alfa) + "  beta:  " + str(beta) + "  value:  " + str(A) + "  group:  " + str(group_number))
        old_values = (alfa, beta)
        if group_number == 0:
            if A in sets.S0.keys():
                (_alfa, _beta) = sets.S0[A]
                return count_X(alfa, beta, _alfa, _beta)
            else:
                alfa *= 2
                beta *= 2

        if group_number == 1:
            if A in sets.S1.keys():
                (_alfa, _beta) = sets.S1[A]
                return count_X(alfa, beta, _alfa, _beta)
            else:
                alfa = alfa + 1
                beta = beta

        if group_number == 2:
            if A in sets.S2.keys():
                (_alfa, _beta) = sets.S2[A]
                return count_X(alfa, beta, _alfa, _beta)
            else:
                alfa = alfa
                beta = beta + 1

        sets.addToGroup(group_number, A, old_values)


print(pollard_rho(Sets()))
