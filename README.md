 # Projetos de Algoritmos Python 🐍
<div align="center">
 
*Repositório didático com exemplos em Python que demonstram classes comuns de
complexidade de algoritmos (notação Big-O). Cada exemplo é autocontido e
voltado para aprendizado — inclui explicações, medições simples e dicas de
experimentos.*

</div>

## 🚀 Como executar

Abra um terminal, navegue até a raiz do repositório e execute os exemplos na
pasta `examples`:

```powershell
cd C:\Users\pc 10\Desktop\Dev\Algoritmos_Py
python .\examples\constant_time.py
python .\examples\logarithmic_time.py
python .\examples\quadratic_time.py
```

Para isolar o ambiente (opcional):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

---

## 📁 Estrutura

- `examples/constant_time.py` — O(1): operação de custo constante.
- `examples/logarithmic_time.py` — O(log n): busca binária.
- `examples/quadratic_time.py` — O(n^2): laços aninhados (brute-force).

## 🧩 Descrição dos exemplos

- constant_time.py (O(1)) — acesso por índice repetido e operação aritmética.
- logarithmic_time.py (O(log n)) — busca binária iterativa em lista ordenada.
- quadratic_time.py (O(n^2)) — contagem de pares com dois laços aninhados.

## ✅ Saídas de exemplo (ilustrativas)

- constant_time.py: n=1_000 → avg ≈ 0.05 µs; n=10_000 → avg ≈ 0.08 µs
- logarithmic_time.py: n=1_000 → avg ≈ 1.6 µs; n=100_000 → avg ≈ 3.0 µs
- quadratic_time.py: n=100 → avg ≈ 0.0004 s; n=400 → avg ≈ 0.0043 s

> Observação: números ilustrativos — resultados variam com hardware, SO e
> versão do Python.

## 🧪 Dicas para experimentos

- Aumente `trials` para reduzir ruído.
- Rode múltiplas repetições e calcule estatísticas (média, mediana).
- Use valores moderados de `n` em algoritmos quadráticos para evitar longos
	tempos de execução.

## ✨ Próximas melhorias sugeridas

- Adicionar exemplos de O(n) e O(n log n) (p.ex. busca linear e merge sort).
- Gerar gráficos comparativos com `matplotlib` a partir de resultados em CSV.
- Implementar um pequeno runner que agregue resultados e exporte para análise.

## 👩‍💻 Autora

- Gabriela Silva — mantenedora (GitHub: `gabiissilvaa`).

---

Se quiser que eu inclua um sumário (TOC), instruções para Linux/macOS ou mais
exemplos (O(n), O(n log n)), diga qual opção prefere e eu atualizo o README.

