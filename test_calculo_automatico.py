import sympy as sp
from math import pi

from calculo_automatico_derivadas import (
    continuidade,
    met_derivada_primeira,
    met_derivada_segunda,
    met_intervalo_fechado
)

x = sp.symbols('x')


def run_tests():
    print("=== TESTES DE CONTINUIDADE ===")
    print("Polinômio:", continuidade(x**2 + 1))
    print("Racional 1/x:", continuidade(1/x))
    print("Raiz sqrt(x-2):", continuidade(sp.sqrt(x - 2)))

    print("\n=== TESTES 1ª DERIVADA ===")
    print("x^2:", met_derivada_primeira(x**2))
    print("sin(x):", met_derivada_primeira(sp.sin(x)))
    print("1/x:", met_derivada_primeira(1/x))

    print("\n=== TESTES 2ª DERIVADA ===")
    print("x^3:", met_derivada_segunda(x**3))
    print("sin(x):", met_derivada_segunda(sp.sin(x)))

    print("\n=== TESTES INTERVALO FECHADO ===")
    print("x^2 em [-2,2]:", met_intervalo_fechado(x**2, [-2, 2]))
    print("1/x em [-1,1]:", met_intervalo_fechado(1/x, [-1, 1]))
    print("sin(x) em [0,2π]:", met_intervalo_fechado(sp.sin(x), [0, 2*pi]))
    print("sin(20x) em [0,2π]:", met_intervalo_fechado(sp.sin(20*x), [0, 2*pi]))


if __name__ == "__main__":
    run_tests()