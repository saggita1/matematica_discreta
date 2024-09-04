import sympy as sp

def coeficiente_a(m, j):
    """
    Calcula o coeficiente a_(m-j) de acordo com a fórmula fornecida.
    """
    k = sp.symbols('k', integer=True)
    somatorio = sp.Sum((-1)**k * sp.binomial(j, k) * (1 - k + j)**m, (k, 0, j)).doit()
    return somatorio

def gerar_formula(m):
    """
    Gera a fórmula da soma das potências de 1^m a n^m utilizando a fórmula fornecida.
    """
    n = sp.symbols('n', integer=True)
    
    soma = 0
    for j in range(m + 1):
        coef_a = coeficiente_a(m, j)
        termo = sp.binomial(n, j + 1) * coef_a
        soma += termo
    
    # Simplificando a expressão final
    soma_simplificada = sp.simplify(soma)
    
    return soma_simplificada

# Exemplo de uso:
m = int(input("Digite o valor de m: "))

print(f"Calculando a fórmula para m = {m}\n")

formula = gerar_formula(m)

print("\nA fórmula simplificada para a soma das potências de 1^m a n^m é:")
sp.pretty_print(formula, use_unicode=True)
