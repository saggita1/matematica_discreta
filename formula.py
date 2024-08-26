from sympy import symbols, Sum, binomial, simplify, pretty

# Definindo as variáveis simbólicas
n, m, j, k = symbols('n m j k')

# Definindo a fórmula para a_menos_j
a_menos_j = Sum((-1)**k * binomial(j, k) * (1 - k + j)**m, (k, 0, j)).doit()

# Função para gerar a fórmula simbólica
def gerar_formula_potencias(m_val, n_val):
    # Expressão geral para a soma das m-ésimas potências
    soma_expr = Sum(binomial(n_val, j + 1) * a_menos_j.subs(j, m_val - j), (j, 0, m_val))
    return soma_expr

# Exemplo de uso para m = 2 e n = 5
m_val = 2
n_val = symbols('n')  # n_val pode ser um símbolo ou um número
formula_gerada = gerar_formula_potencias(m_val, n_val)

# Utilizando o pretty para imprimir a fórmula de forma mais legível
print(f"A fórmula para a soma das {m_val}-ésimas potências dos números naturais até {n_val} é:")
print(pretty(formula_gerada, use_unicode=True))
