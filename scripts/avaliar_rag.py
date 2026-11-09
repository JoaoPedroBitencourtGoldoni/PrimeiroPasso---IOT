"""Avaliação reproduzível da recuperação lexical (não avalia a qualidade do LLM)."""
import csv
import json
from pathlib import Path
from app.rag import retriever

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evidencias" / "consultas_rag.csv"
OUTPUT = ROOT / "evidencias" / "resultado_rag.json"


def main():
    with CASES.open(encoding="utf-8", newline="") as handle:
        cases = list(csv.DictReader(handle))
    results = []
    for case in cases:
        docs = retriever.search(case["consulta"])
        returned = [doc["id"] for doc in docs]
        expected = case["fonte_esperada"].strip()
        passed = expected in returned if expected else not returned
        results.append({"caso": case["caso"], "consulta": case["consulta"],
                        "fonte_esperada": expected or None, "fontes_recuperadas": returned,
                        "aprovado": passed})
    count = sum(item["aprovado"] for item in results)
    report = {"metodo": "TF-IDF, cosseno, top-3, limiar 0.035",
              "total": len(results), "aprovados": count,
              "taxa_acerto": round(count / len(results), 3) if results else None,
              "observacao": "Teste de recuperação; não é validação do texto do LLM.",
              "casos": results}
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Recuperação RAG: {count}/{len(results)} casos; relatório: {OUTPUT}")
    if count != len(results):
        print("Alguns casos falharam; consulte o relatório. Não altere as evidências manualmente.")


if __name__ == "__main__":
    main()
