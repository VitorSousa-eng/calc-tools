import sympy as sp
import math

x = sp.symbols('x')


def continuidade(funcao):
    """
    Retorna o domínio de continuidade da função.
    """
    try:
        dominio = sp.calculus.util.continuous_domain(funcao, x, sp.S.Reals)
        return dominio
    except Exception:
        return sp.S.EmptySet


def met_derivada_primeira(funcao):
    """
    Método da primeira derivada:
    - pontos críticos
    - intervalos de crescimento
    - intervalos de decrescimento
    """
    derivada = sp.diff(funcao, x)

    try:
        pontos_criticos = sp.solveset(derivada, x, domain=sp.S.Reals)
    except Exception:
        pontos_criticos = sp.S.EmptySet

    try:
        intervalo_crescimento = sp.solve_univariate_inequality(
            derivada > 0, x, domain=sp.S.Reals
        )
    except Exception:
        intervalo_crescimento = sp.S.EmptySet

    try:
        intervalo_decrescimento = sp.solve_univariate_inequality(
            derivada < 0, x, domain=sp.S.Reals
        )
    except Exception:
        intervalo_decrescimento = sp.S.EmptySet

    return {
        "pontos_criticos": pontos_criticos,
        "crescimento": intervalo_crescimento,
        "decrescimento": intervalo_decrescimento
    }


def met_derivada_segunda(funcao):
    """
    Método da segunda derivada:
    - pontos de inflexão
    - concavidade
    """
    derivada_segunda = sp.diff(funcao, x, 2)

    try:
        pontos_inflexao = sp.solveset(derivada_segunda, x, domain=sp.S.Reals)
    except Exception:
        pontos_inflexao = sp.S.EmptySet

    try:
        concavidade_cima = sp.solve_univariate_inequality(
            derivada_segunda > 0, x, domain=sp.S.Reals
        )
    except Exception:
        concavidade_cima = sp.S.EmptySet

    try:
        concavidade_baixo = sp.solve_univariate_inequality(
            derivada_segunda < 0, x, domain=sp.S.Reals
        )
    except Exception:
        concavidade_baixo = sp.S.EmptySet

    return {
        "pontos_inflexao": pontos_inflexao,
        "concavidade_cima": concavidade_cima,
        "concavidade_baixo": concavidade_baixo
    }


def met_intervalo_fechado(funcao, intervalo, n_amostras=400):
    """
    Método do intervalo fechado para máximo e mínimo.
    Usa pontos críticos quando forem finitos.
    Caso contrário, usa amostragem numérica.
    """
    a = intervalo[0]
    b = intervalo[1]

    if a > b:
        aux = a
        a = b
        b = aux

    try:
        derivada = sp.diff(funcao, x)
        pontos_criticos = sp.solveset(derivada, x, domain=sp.S.Reals)
    except Exception:
        pontos_criticos = sp.S.EmptySet

    pontos_avaliacao = []
    pontos_avaliacao.append(a)
    pontos_avaliacao.append(b)

    if isinstance(pontos_criticos, sp.FiniteSet):
        for ponto in pontos_criticos:
            try:
                valor = float(ponto)
                if valor >= a and valor <= b:
                    pontos_avaliacao.append(valor)
            except Exception:
                pass
    else:
        try:
            f_num = sp.lambdify(x, funcao, "math")
            passo = (b - a) / n_amostras
            i = 0

            while i <= n_amostras:
                ponto = a + i * passo
                pontos_avaliacao.append(ponto)
                i += 1
        except Exception:
            pass

    valores = {}
    for ponto in pontos_avaliacao:
        try:
            valor_funcao = funcao.subs(x, ponto)
            valor_numerico = float(valor_funcao)

            if math.isfinite(valor_numerico):
                valores[ponto] = valor_numerico
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        except OverflowError:
            pass
        except Exception:
            pass

    if len(valores) == 0:
        return {"erro": "Não foi possível avaliar a função no intervalo."}

    minimo_ponto = None
    minimo_valor = None
    maximo_ponto = None
    maximo_valor = None

    for ponto in valores:
        valor = valores[ponto]

        if minimo_valor is None or valor < minimo_valor:
            minimo_valor = valor
            minimo_ponto = ponto

        if maximo_valor is None or valor > maximo_valor:
            maximo_valor = valor
            maximo_ponto = ponto

    return {
        "ponto_minimo": minimo_ponto,
        "valor_minimo": minimo_valor,
        "ponto_maximo": maximo_ponto,
        "valor_maximo": maximo_valor
    }
