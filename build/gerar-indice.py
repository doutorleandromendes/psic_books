#!/usr/bin/env python3
"""
Gera o índice remissivo a partir das âncoras de conceito.

Convenção: todo conceito recebe um título com id explícito no formato
    ## O estádio do espelho {#c-estadio-do-espelho}

Termos adicionais (sinônimos, formas em francês, remissivas) vivem em
book/termos.yaml e apontam para uma âncora existente:
    lalangue: c-lalangue
    alíngua: c-lalangue

Num EPUB refluível não existe página. Índice remissivo por número de
página é impossível — o que funciona é âncora nomeada com link. É isso
que este script produz.
"""

import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
if len(sys.argv) < 2:
    raise SystemExit("uso: gerar-indice.py <tomo>   ex.: iii-operacao")
LIVRO = RAIZ / "tomos" / sys.argv[1]
SAIDA = LIVRO / "98-indice-termos.md"

PADRAO_TITULO = re.compile(r"^#{2,4}\s+(.+?)\s*\{#(c-[a-z0-9-]+)\}\s*$", re.M)


def chave_ordenacao(s: str) -> str:
    """Ordena ignorando acentos e caixa — 'Álgebra' junto de 'algebra'."""
    nfkd = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def coletar_ancoras() -> dict[str, str]:
    entradas: dict[str, str] = {}
    for md in sorted(LIVRO.glob("*.md")):
        if md.name.startswith(("98-", "99-")):
            continue
        texto = md.read_text(encoding="utf-8")
        for titulo, ancora in PADRAO_TITULO.findall(texto):
            titulo_limpo = re.sub(r"[*_`]", "", titulo).strip()
            entradas[titulo_limpo] = ancora
    return entradas


def coletar_remissivas() -> dict[str, str]:
    arquivo = LIVRO / "termos.yaml"
    if not arquivo.exists():
        return {}
    remissivas: dict[str, str] = {}
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        linha = linha.split("#", 1)[0].strip()
        if not linha or ":" not in linha:
            continue
        termo, ancora = linha.split(":", 1)
        remissivas[termo.strip()] = ancora.strip()
    return remissivas


def main() -> int:
    entradas = coletar_ancoras()
    entradas.update(coletar_remissivas())

    if not entradas:
        print("nenhuma âncora de conceito encontrada", file=sys.stderr)
        return 1

    ancoras_validas = set(coletar_ancoras().values())
    orfas = {t: a for t, a in entradas.items() if a not in ancoras_validas}
    for termo, ancora in orfas.items():
        print(f"aviso: '{termo}' aponta para âncora inexistente '{ancora}'",
              file=sys.stderr)

    linhas = [
        "# Índice de termos",
        "",
        "::: {.indice-termos}",
        "",
    ]

    letra_atual = ""
    for termo in sorted(entradas, key=chave_ordenacao):
        if entradas[termo] not in ancoras_validas:
            continue
        inicial = chave_ordenacao(termo)[:1].upper()
        if inicial != letra_atual:
            letra_atual = inicial
            linhas += ["", f"**{inicial}**", ""]
        linhas.append(f"- [{termo}](#{entradas[termo]})")

    linhas += ["", ":::", ""]

    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    total = sum(1 for a in entradas.values() if a in ancoras_validas)
    print(f"índice gerado — {total} entradas, {len(ancoras_validas)} conceitos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
