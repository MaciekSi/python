import Crypto.Util.number as number

def generate(bits):
    order = number.getPrime(bits-1)
    potentially_prime = (order * 2) + 1
    if number.isPrime(potentially_prime):
        return potentially_prime
    else:
        return generate(bits)


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


def count_X(alfa1, beta1, alfa2, beta2):
    alfa_dif = (alfa1 - alfa2) % order
    beta_dif = (beta2 - beta1) % order
    alfa_dif_mod_inv = modular_inverse(alfa_dif, order)
    result = (beta_dif * alfa_dif_mod_inv) % order
    if ((_g**result) % _p) == _y:
        return result
    else:
        return result + order


def step(A, params):
    alfa, beta = params
    set_number = A % 3
    if set_number == 0:
        return (A ** 2 % _p), ((alfa * 2)%order, (beta * 2)%order)
    if set_number == 1:
        return ((A * _y) % _p), ((alfa + 1)%order, beta)
    if set_number == 2:
        return ((A * _g) % _p), (alfa, (beta + 1)%order)


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

    return count_X(alfa_A, beta_A, alfa_B, beta_B)


if __name__ == '__main__':
    number_of_bits = 40
    _p = generate(40)
    _g = 8
    _x = 512
    _y = (_g**_x) % _p
    order = (_p-1)/2
    print(pollard_rho(_y, _g, _p))