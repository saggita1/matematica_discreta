from sympy import symbols, Sum, binomial, pretty

# símbolos e fórmula de a
n, m, j, k = symbols('n m j k')
a_menos_j = Sum((-1)**k * binomial(j, k) *  (1 - k + j)**m, (k, 0, j))


def gerar_formula_potencias(m_val, n_val):
    # Expressão geral para a soma das m-ésimas potências
    soma_expr = Sum(binomial(n_val, j + 1) * a_menos_j.subs(m,m_val), (j, 0, m_val))
    return soma_expr

def enesimo(n, m):
    soma = 0
    n_natural = 1
    while n_natural <= n:
        soma += n_natural**m
        n_natural += 1
    
    return soma


# recebimento de M e N
m_val = int(input("\nDigite o valor de M: "))
n_val = int(input("Digite o valor de N: "))
formula_gerada = gerar_formula_potencias(m_val, n_val)


# impressão
print(f"\nA fórmula para a soma das {m_val}-ésimas potências dos números naturais até {n_val} é:")
print(pretty(formula_gerada, use_unicode=True))
print(f"\nO resultado é {enesimo(n_val, m_val)}\n")