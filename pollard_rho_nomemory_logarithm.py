
def count_value(alfa, beta):
    return ((_g ** beta) * (_y ** alfa)) % _p


def count_X(alfa1, beta1, alfa2, beta2, _p):
    beta_dif = float((beta1-beta2) % (_p-1))
    alfa_dif = float(alfa2-alfa1)
    while (beta_dif / alfa_dif) % 1.0 != 0.0:
        beta_dif = float(beta_dif + (_p-1))
    return int(beta_dif / alfa_dif)


def step(A, (alfa, beta)):
    set_number = A % 3
    if set_number == 0:
        return (A ** 2 % _p), (alfa * 2, beta * 2)
    if set_number == 1:
        return ((A * _y) % _p), (alfa + 1, beta)
    if set_number == 2:
        return ((A * _g) % _p), (alfa, beta + 1)


def iterate(A, param_A, B, param_B):
    (alfa_A, beta_A) = param_A
    (alfa_B, beta_B) = param_B
    A, (alfa_A, beta_A) = step(A, (alfa_A, beta_A))
    B, (alfa_B, beta_B) = step(B, (alfa_B, beta_B))
    B, (alfa_B, beta_B) = step(B, (alfa_B, beta_B))
    return A, (alfa_A, beta_A), B, (alfa_B, beta_B)


def pollard_rho(_y, _g, _p):
    # alfa- power of _y value
    alfa_A = 0
    alfa_B = 0
    # beta- power of _g value
    beta_A = 0
    beta_B = 0

    A = 1
    B = 1
    A, (alfa_A, beta_A), B, (alfa_B, beta_B) \
        = iterate(A, (alfa_A, beta_A), B, (alfa_B, beta_B))

    while A != B:
        A, (alfa_A, beta_A), B, (alfa_B, beta_B) \
            = iterate(A, (alfa_A, beta_A), B, (alfa_B, beta_B))

    return count_X(alfa_A, beta_A, alfa_B, beta_B, _p)


if __name__ == '__main__':
    _g = 3
    _y = 48
    _p = 101
    print(pollard_rho(_y, _g, _p))
