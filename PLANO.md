# Plano de arquitetura — *O Curso*

Quatro tomos independentes. Registro dos volumes da série.
Coleção própria: `Teoria Psicanalítica — O Curso`, irmã da série monográfica
`Teoria Psicanalítica — Estudo Sistemático` (Volumes 1–7).

## A aritmética

O currículo tem 215 blocos curados (~163 mil palavras em registro de nota).
O registro dos volumes roda a ~7.500 palavras por capítulo. Escrever 215
capítulos nesse registro daria ~1,6 milhão de palavras.

A resolução não é baixar o registro. É consolidar a granularidade: os blocos do
currículo não são capítulos, são notas de aula. Consolidados **4:1** por eixo
conceitual, os 215 blocos viram **~52 capítulos**, distribuídos em quatro tomos:

| Tomo | Capítulos | Palavras |
|---|---|---|
| I — As Tradições | 14 | ~105.000 |
| II — As Formas do Sofrimento | 14 | ~105.000 |
| III — A Operação Clínica | 12 | ~90.000 |
| IV — As Fronteiras | 12 | ~90.000 |

Cada tomo é um livro normal de 300 a 350 páginas. O registro fica intacto.

**Custo do fatiamento.** O índice remissivo deixa de resolver por hyperlink entre
tomos — EPUB não linka entre arquivos. Remissiva externa vira referência nomeada
(tomo + capítulo), nunca link quebrado. E o princípio de escrever cada eixo uma
única vez degrada nas fronteiras: cada tomo precisa de autossuficiência mínima,
o que implica alguma re-exposição deliberada nos pontos de costura.

## O princípio de consolidação

Consolidar **por eixo conceitual, não por ordem cronológica do curso**. A mesma
escola reaparece em Freud, depois em Depressão, depois em Transferência — três
vezes, em três registros. No currículo isso é pedagogia; num livro é redundância.
Cada eixo é escrito uma vez, no lugar em que rende mais, e referenciado por
âncora nas demais ocorrências.

## Relação com a série de volumes

A Parte I do currículo cobre as mesmas escolas que os Volumes 1–7 cobrirão em
profundidade monográfica. Este volume **não repete** essa exposição. O Livro I
aqui é o *mapa comparativo* — o que só aparece quando as tradições são postas
lado a lado — e remete aos volumes para o tratamento monográfico. É o único
arranjo em que os dois objetos não competem.

## Estrutura

### Tomo I — As Tradições (14 capítulos)
Fontes: `fase1`–`fase5`, Fase VI (a recuperar). Reorganizado por problema:
o aparelho e sua economia; a defesa como objeto; o objeto interno; o ambiente;
o campo intersubjetivo; o significante; e os cinco problemas epistemológicos da
Fase VI, que fecham o livro.

### Tomo II — As Formas do Sofrimento (14 capítulos)
Fontes: `p2m01`–`p2m11`. Ordem preservada — a sequência clínica já é o eixo.
Os módulos neuróticos (1–5) recebem peso maior, conforme decidido no currículo.

### Tomo III — A Operação Clínica (13 capítulos)
Fontes: `psm00`–`psm06`, sete unidades, 39 blocos, 315.280 caracteres.
`psm07` e `psm08` nunca foram escritos — confirmado; removidos do plano e a
remover do `SECTIONS` do site. É a Parte de melhor razão esforço/resultado:
8.084 caracteres por bloco, quase em prosa plena, com transcrição para seis
das sete unidades e o curado do `psm01` já em densidade equivalente.

**Mapa de capítulos** (fonte → capítulo):

| # | Capítulo | Fonte | Chars |
|---|---|---|---|
| 1 | O exame psíquico como instrumento | psm00 intro–B5 | 13.191 |
| 2 | As funções e a ponte para a psicanálise | psm00 B6–B10 | 12.303 |
| 3 | O que conta como material clínico | psm01 B1, B3 | 13.461 |
| 4 | A associação livre e seus limites | psm01 B2, B4 | 17.217 |
| 5 | Detailed inquiry e pontuação | psm01 B5, B6 | 17.242 |
| 6 | O corpo antes da fala | psm02 B1–B2 | 30.683 |
| 7 | Contratransferência e campo emocional | psm02 B3–B4 | 32.409 |
| 8 | O sonho na sessão, e o sonho de Irma | psm03 B1–B2, adendo | 26.033 |
| 9 | O sonho pelas tradições | psm03 B3–B5 | 25.888 |
| 10 | A transferência como sinal estrutural | psm04 B1–B3 | 25.805 |
| 11 | Transferência borderline e psicótica | psm04 B4–B5 | 24.560 |
| 12 | A resistência e o silêncio | psm05 B1–B3 | 42.983 |
| 13 | A sessão como unidade | psm06 B1–B4 | 33.478 |

Notas de execução:

- O `psm00` é objeto de outra natureza — semiologia descritiva, não comparação
  entre escolas. Não suporta 7×: expande 2–3×, e isso é o correto. Capítulos 1
  e 2 saem menores que os demais, deliberadamente.
- **Lacuna interna:** `psm06` Bloco 2 ("O Meio da Sessão") tem 360 caracteres e
  o texto declara *conteúdo pendente de recepção*. Existe apenas o sumário do
  que cobriria — desenvolvimento não-linear, desvios como material, retornos a
  temas abandonados, intensificação afetiva, timing da intervenção. O Capítulo
  13 precisa escrevê-lo do zero a partir das fontes primárias.

### Tomo IV — As Fronteiras (12 capítulos)
Fontes: `p3m01`–`p3m12`. A Parte mais comprimida (2.598 chars/bloco) e a que
mais depende de recuperação da conversa original.

### Apêndices — distribuídos por tomo
- Dicionário lacaniano — 34 verbetes, blocos `.eop-block` → Tomo I (conversa `af452fd7`)
- Leituras literárias — *Lord of the Flies*, Sandman, Bourgeois → Tomo IV (`d57f4fca`, `9ac51478`)
- Índice remissivo — um por tomo, `build/gerar-indice.py <tomo>`

## Estado das fontes

| Unidade | Curado | Transcrição | Ação |
|---|---|---|---|
| fase1 | sim | **parcial** (10/11 textos, 47%) | falta *Pulsões e seus Destinos* + *Repressão* Bl. 1 |
| fase2 | sim | sim (44%) | pronto |
| fase3 | sim | sim (30%) | pronto |
| fase4 | sim | sim (45%) | pronto |
| fase5 | sim | sim (60%) | pronto |
| fase6 | **não** | **não** | recuperar de `c0057b9b` |
| p2m01–p2m11 | sim (4.348 chars/bloco) | **não** | curado serve como fonte |
| psm00, psm02–06 | sim | sim | pronto |
| psm01 | sim (7.987 chars/bloco) | **não** | curado já em prosa quase plena — dispensável |
| psm07, psm08 | **não** | **não** | não existem |
| p3m01–p3m12 | sim (2.598 chars/bloco) | **não** | o mais comprimido — reescrita mais livre |

## Nota sobre as fontes

Nenhuma transcrição contém turnos de diálogo — todas são exportações apenas da
saída. As intervenções, correções e objeções do autor ao longo do curso não
existem em arquivo algum; só nas conversas cruas. Elas entram como notas
marginais atribuídas, garimpadas por busca dirigida a cada capítulo.

A curadoria preservou as citações ancoradas e o esqueleto argumentativo; o que
ela descartou foi desenvolvimento de prosa. Como a reescrita roda a ~7× o
registro curado, esse descarte é andaime, não informação.

## Pendências no repositório `psic`

- `fase6.json` nunca foi gerado
- `psm07.json` e `psm08.json` configurados em `SECTIONS` mas ausentes
- `psm01.txt` ausente
- `p3m12.json` existe no repo mas **não está em `SECTIONS`** — invisível no site

## Build

    ./build/build.sh iii-operacao        # → dist/curso-iii-operacao.epub
    ./build/build.sh i-tradicoes

Capítulos são `tomos/<tomo>/NN-nome.md`, ordenados pelo prefixo numérico.
O índice remissivo (`98-`) é regenerado a cada build a partir das âncoras
`{#c-...}` e de `tomos/<tomo>/termos.yaml`.

## Ordem de execução proposta

Tomo III primeiro: já está a 8.084 chars/bloco, tem transcrição para seis das
sete unidades, e é o único conteúdo que nenhum volume monográfico vai cobrir.
Depois II, depois IV, e o I por último — porque ele depende de saber o que os
Volumes 1–7 já terão dito para não duplicá-los.
