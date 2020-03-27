_g = 3
_y = 48
_p = 101


def count_value(alfa, beta):
    return ((_g ** beta) * (_y ** alfa)) % _p


# calculate value of X based on alfas and betas from collision
def count_X(alfa1, beta1, alfa2, beta2):
    print(alfa2, beta2, alfa1, beta1)
    return ((beta2 - beta1) % (_p - 1)) / (alfa1 - alfa2)


def step(A, (alfa, beta)):
    set_number = A % 3
    if set_number == 0:
        return (A ** 2 % _p), (alfa * 2, beta * 2)
    if set_number == 1:
        return ((A * _g) % _p), (alfa, beta + 1)
    if set_number == 2:
        return ((A * _y) % _p), (alfa + 1, beta)


def pollard_rho():
    # alfa- power of _y value
    alfa_A = 0
    alfa_B = 0
    # beta- power of _g value
    beta_A = 0
    beta_B = 0

    A = 1
    B = 1

    A, (alfa_A, beta_A) = step(A, (alfa_A, beta_A))
    B, (alfa_B, beta_B) = step(B, (alfa_B, beta_B))
    B, (alfa_B, beta_B) = step(B, (alfa_B, beta_B))

    while A != B:
        A, (alfa_A, beta_A) = step(A, (alfa_A, beta_A))
        B, (alfa_B, beta_B) = step(B, (alfa_B, beta_B))
        B, (alfa_B, beta_B) = step(B, (alfa_B, beta_B))

    print(A, B)
    return count_X(alfa_B, beta_B, alfa_A, beta_A)


print(pollard_rho())
