#!/usr/bin/env bash
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOMO="${1:?uso: build.sh <tomo> [saida]   ex.: build.sh iii-operacao}"
LIVRO="$RAIZ/tomos/$TOMO"
[ -d "$LIVRO" ] || { echo "tomo inexistente: $LIVRO" >&2; exit 1; }
SAIDA="${2:-$RAIZ/dist}"
mkdir -p "$SAIDA"

# ── 1. Índice remissivo, regenerado a cada build ──
python3 "$RAIZ/build/gerar-indice.py" "$TOMO"

# ── 2. UUID estável por build ──
UUID="$(python3 -c 'import uuid; print(uuid.uuid4())')"
META_TMP="$(mktemp /tmp/meta.XXXXXX.yaml)"
sed "s|PLACEHOLDER-GERADO-NO-BUILD|$UUID|" "$LIVRO/metadata.yaml" > "$META_TMP"

# ── 3. Ordem dos capítulos: numérica pelo prefixo do arquivo ──
mapfile -t CAPS < <(find "$LIVRO" -maxdepth 1 -name '[0-9][0-9]-*.md' | sort)

if [ ${#CAPS[@]} -eq 0 ]; then
  echo "erro: nenhum capítulo encontrado em $LIVRO" >&2
  exit 1
fi

echo "capítulos:"
printf '  %s\n' "${CAPS[@]##*/}"

# ── 4. Compilação ──
#   --split-level=1     um arquivo XHTML por H1 → navegação e busca melhores
#   --toc-depth=3       sumário até o nível do conceito
#   +fenced_divs        ::: {.classe} → <div class="classe">
#   +bracketed_spans    [texto]{.classe} → <span class="classe">
#   --epub-title-page   folha de rosto gerada a partir dos metadados
pandoc \
  --from=markdown+fenced_divs+bracketed_spans+smart+footnotes \
  --to=epub3 \
  --metadata-file="$META_TMP" \
  --resource-path="$RAIZ:$RAIZ/assets:$LIVRO" \
  --css="$RAIZ/assets/css/epub.css" \
  --toc \
  --toc-depth=3 \
  --split-level=1 \
  --epub-title-page=true \
  --output="$SAIDA/curso-$TOMO.epub" \
  "${CAPS[@]}"

rm -f "$META_TMP"

# ── 5. Verificação estrutural ──
python3 - "$SAIDA/curso-$TOMO.epub" <<'PY'
import sys, zipfile
caminho = sys.argv[1]
with zipfile.ZipFile(caminho) as z:
    nomes = z.namelist()
    ruim = z.testzip()
    assert ruim is None, f"entrada corrompida: {ruim}"
    assert nomes[0] == "mimetype", "mimetype precisa ser a primeira entrada"
    mimetype = z.read("mimetype").decode()
    assert mimetype == "application/epub+zip", f"mimetype inválido: {mimetype}"
    xhtml = [n for n in nomes if n.endswith(".xhtml")]
    tem_nav = any("nav" in n for n in xhtml)
    print(f"OK — {len(nomes)} entradas, {len(xhtml)} documentos XHTML, "
          f"nav={'sim' if tem_nav else 'NÃO'}")
PY

echo "→ $SAIDA/curso-$TOMO.epub"
