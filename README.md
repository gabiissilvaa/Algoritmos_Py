# Algoritmos_Py

Uma coleção pequena de exemplos em Python que ilustram princípios de
complexidade de algoritmos (notação Big-O). Cada exemplo mede tempos
simplesmente para demonstrar o comportamento assintótico (comparação
empírica) — não são micro-benchmarks profissionais.

## Objetivos do projeto

- Demonstrar operações com complexidade O(1), O(log n) e O(n^2).
- Fornecer scripts fáceis de executar para ensino e experimentação.
- Explicar como interpretar os tempos medidos e limitações das medições.

## Estrutura do repositório

- `examples/constant_time.py`  — O(1): acesso por índice e operação aritmética.
- `examples/logarithmic_time.py` — O(log n): busca binária em lista ordenada.
- `examples/quadratic_time.py` — O(n^2): laços aninhados contando pares.
- `README.md` — este arquivo.

## Pré-requisitos

- Python 3.8+ (testado com CPython 3.x). Não há dependências externas.
- Um terminal (PowerShell no Windows foi usado nas instruções).

Recomendação (opcional): criar um ambiente virtual antes de rodar os
scripts:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

## Como executar

Use os comandos abaixo no PowerShell (cada comando roda um exemplo):

```powershell
python .\examples\constant_time.py
python .\examples\logarithmic_time.py
python .\examples\quadratic_time.py
```

Cada script imprime tempos médios para alguns tamanhos de entrada. Os
parâmetros internos (por exemplo, número de trials) são ajustados nos
próprios scripts para equilibrar ruído e custo computacional.

## Descrição dos exemplos (contratos e comportamento)

- `constant_time.py`
	- Entrada: uma lista `lst` de tamanho n.
	- Saída: tempo médio por operação (acesso por índice repetido).
	- Complexidade: O(1) por operação — tempo por operação não cresce com n.
	- Observação: lista deve ter pelo menos 1 elemento (lista vazia gera
		IndexError).

- `logarithmic_time.py`
	- Entrada: lista ordenada `arr` de tamanho n e um `target` aleatório.
	- Saída: tempo médio por busca (busca binária iterativa).
	- Complexidade: O(log n) por busca — cada passo corta pela metade o
		espaço de busca.
	- Observação: retorna -1 quando não encontra o elemento.

- `quadratic_time.py`
	- Entrada: lista `arr` de tamanho n e um `target` fixo.
	- Saída: tempo médio por execução da contagem de pares (laços aninhados).
	- Complexidade: O(n^2) — todos os pares i<j são verificados.
	- Observação: tempo cresce muito rápido com n; usar n moderado para
		experimentos locais.

## Exemplos de saída (execução local)

- `constant_time.py` (exemplo):

	n=1_000    avg time/op ≈ 0.052 µs
	n=10_000   avg time/op ≈ 0.079 µs
	n=100_000  avg time/op ≈ 0.066 µs

- `logarithmic_time.py` (exemplo):

	n=1_000    avg time/search ≈ 1.59 µs
	n=10_000   avg time/search ≈ 2.19 µs
	n=100_000  avg time/search ≈ 2.97 µs

- `quadratic_time.py` (exemplo):

	n=100   avg time/run ≈ 0.000403 s
	n=200   avg time/run ≈ 0.000869 s
	n=400   avg time/run ≈ 0.004309 s

Observação: valores numéricos são da minha execução local; sua máquina
poderá apresentar números diferentes.

## Interpretação das medições

- Big-O descreve crescimento assintótico. As medições mostram comportamento
	empírico para pequenos conjuntos de tamanhos n e ajudam a visualizar a
	diferença entre classes de complexidade.
- Variações no tempo (ruído) vêm de cache, escalonamento do SO, diferenças
	na implementação do Python e outros fatores. Para reduzir ruído, aumente
	o número de trials nos scripts ou use ferramentas como `timeit`.

## Troubleshooting

- Recebe `IndexError` no `constant_time.py`? Certifique-se de que a lista
	gerada não é vazia (os scripts atuais usam n >= 1).
- Execuções muito lentas no `quadratic_time.py`? Use valores menores de n
	(p.ex. 100, 200) ou reduza `trials` no script.
- Se `python` não for reconhecido, verifique sua instalação do Python e a
	variável PATH.

## Sugestões de continuidade

- Adicionar exemplos para O(n) (varredura linear) e O(n log n) (merge
	sort com contagem de tempo).
- Gerar gráficos com `matplotlib` comparando tempos empíricos por n.
- Incluir testes automatizados e um pequeno benchmark harness que
	serializa resultados em CSV para análise posterior.

## Licença

Sinta-se livre para usar e adaptar estes exemplos para fins educacionais.

