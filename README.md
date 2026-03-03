# Automação de Cálculos em Cálculo Diferencial

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=for-the-badge)
![Math](https://img.shields.io/badge/math-%23000000.svg?style=for-the-badge&logo=python&logoColor=white)
![SymPy](https://img.shields.io/badge/SymPy-%233B5249.svg?style=for-the-badge&logo=python&logoColor=white)

Este projeto fornece um conjunto de ferramentas para **automatizar cálculos recorrentes** em  Cálculo Diferencial I, como análise de continuidade, métodos da primeira e segunda derivada e determinação de máximos e mínimos em intervalos fechados.

O código foi desenvolvido com **foco em legibilidade, robustez e clareza conceitual**, priorizando a compreensão do processo matemático sobre otimizações agressivas de desempenho.

---

## Objetivo do Projeto

- Automatizar cálculos repetitivos comuns em Cálculo I.
- Reduzir erros manuais em análises de funções e esboço de gráficos à mão.
- Servir como base para algoritmos maiores e mais complexos.
- Facilitar manutenção, adaptação e expansão futura do código.
- Manter o código **fácil de ler, entender e explicar**, mesmo para quem não é programador profissional.

---

## Estrutura do Código

O projeto é dividido em funções independentes, cada uma responsável por um conceito matemático específico:

- `continuidade(funcao)`  
  Determina o domínio de continuidade da função no conjunto dos reias.

- `met_derivada_primeira(funcao)`  
  Aplica o método da primeira derivada para encontrar:
  - pontos críticos;
  - intervalos de crescimento;
  - intervalos de decrescimento.

- `met_derivada_segunda(funcao)`  
  Aplica o método da segunda derivada para analisar:
  - concavidade;
  - candidatos a pontos de inflexão.
  **importante salientar que nem toda solução da derivada segunda é um ponto de inflexão!**

- `met_intervalo_fechado(funcao, intervalo)`  
  Determina máximo e mínimo absolutos em um intervalo fechado, utilizando:
  - pontos críticos finitos, quando disponíveis;
  - amostragem numérica como alternativa robusta em casos mais complexos.

Cada função pode ser usada **isoladamente**, sem necessidade de executar o restante do código. O que permite maior desempenho, organização e manutenção.

---

## Pontos Fortes

- **Alta legibilidade:**  
  O código prioriza clareza e organização, evitando construções excessivamente compactas ou difíceis de interpretar.

- **Separação de responsabilidades:**  
  Cada função resolve um único problema matemático bem definido.

- **Robustez contra erros comuns:**  
  Tratamento explícito de exceções como:
  - divisão por zero (ZeroDivionError);
  - valores indefinidos (ValueError);
  - overflow numérico (OverFlowError);
  - limitações do cálculo simbólico.

- **Uso consciente de matemática simbólica:**  
  A maior parte das saídas é simbólica, permitindo:
  - análise exata;
  - manipulação algébrica posterior;
  - melhor rastreabilidade do raciocínio matemático.

- **Escalabilidade conceitual:**  
  O código pode ser incorporado a sistemas maiores, relatórios automáticos ou rotinas de análise mais complexas.

---

## ⚠️ Limitações Conhecidas

- **Saídas predominantemente simbólicas:**  
  As funções retornam objetos do SymPy.  
  Isso é uma escolha deliberada para preservar exatidão e clareza matemática, mas pode exigir conversão para tipos numéricos (`float`) em aplicações maiores para garantir portabilidade.

- **Aproximações numéricas em casos complexos:**  
  Quando a análise simbólica não é viável (por exemplo, conjuntos infinitos de pontos críticos), o método do intervalo fechado utiliza **amostragem numérica**, o que:
  - é aceitável em contextos de engenharia;
  - não garante exatidão matemática absoluta.

- **Não otimizado para alto desempenho:**  
  O foco do projeto não é velocidade máxima ou grandes volumes de dados, mas sim **confiabilidade, entendimento, manutenção**.

---

## 🔄 Conversão para Saídas Numéricas

Embora as saídas sejam simbólicas, a conversão para valores numéricos pode ser feita facilmente quando necessário, por exemplo:

```python
valor_numerico = float(expressao_sympy)
```

---
**Autor:** Vitor Sousa,
Estudante de Engenharia Civil - UFMG
