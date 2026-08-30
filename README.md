# O Curso — Teoria Psicanalítica

Quatro tomos em EPUB3, derivados do currículo sistemático de teoria
psicanalítica. Coleção irmã da série monográfica em
[`psic_epubs`](https://github.com/doutorleandromendes/psic_epubs)
(Volumes 1–7, um por escola).

Onde os volumes monográficos aprofundam **uma** tradição, os tomos aqui
põem as tradições **lado a lado** — e cobrem o que nenhum volume cobre:
a psicopatologia lida pelas escolas, a operação clínica, e as fronteiras
do campo.

| Tomo | Título | Capítulos | Estado |
|---|---|---|---|
| I | As Tradições | 14 | fontes completas |
| II | As Formas do Sofrimento | 14 | fontes completas |
| III | A Operação Clínica | 12 | **fontes completas — em escrita** |
| IV | As Fronteiras | 12 | fontes completas |

Arquitetura, aritmética de consolidação e estado das fontes: [`PLANO.md`](PLANO.md).

## Estrutura

    tomos/<tomo>/NN-nome.md     capítulos, ordenados pelo prefixo numérico
    tomos/<tomo>/metadata.yaml  metadados EPUB do tomo
    tomos/<tomo>/termos.yaml    remissivas do índice — termo: c-ancora
    assets/css/epub.css         estilo, degradável
    assets/img/                 diagramas (svg fonte, png rasterizado 2×)
    build/                      pipeline
    fontes/curado/              JSON do currículo convertido em md
    fontes/transcricoes/        exportações das sessões originais

`fontes/` é matéria-prima, não texto publicável. Os capítulos são escritos
a partir dela, não montados com ela.

## Build

    ./build/build.sh iii-operacao          # → dist/curso-iii-operacao.epub
    ./build/build.sh i-tradicoes ~/Desktop

Requer `pandoc` (≥ 3.0) e `python3`. O índice remissivo (`98-indice-termos.md`)
é regenerado a cada build a partir das âncoras `{#c-...}` nos títulos e das
remissivas em `termos.yaml`.

Num EPUB refluível não existe número de página — o índice resolve por âncora
nomeada. Entre tomos não há link possível: remissiva externa é referência
nomeada (tomo + capítulo), nunca link quebrado.

## Convenções

Prosa desenvolvida, densa, sem estrutura telegrafada. Citações diretas e
completas, ancoradas em edição publicada, traduzidas com o tradutor creditado.
Mini-biografia na primeira aparição de cada autor, com a população clínica
nomeada e o viés amostral implicado. Implicação técnica ao fim de cada seção.
Exemplos literários e culturais, sem defaults heteronormativos. Honestidade
crítica sobre as fraquezas conceituais — exposição não hagiográfica.
Sintaxe pandoc apenas no `.md` canônico, no fechamento do capítulo.

Estudo independente, não clínico. Uso pessoal — contém citação direta de obra
sob direito autoral.
