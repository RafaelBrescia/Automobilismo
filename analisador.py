import json


def ler_registros(caminho):
    """Lê o arquivo de notas e retorna uma lista de alunos."""
    registros = []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for numero, linha in enumerate(arquivo, start=1):
                linha = linha.strip()

                try:
                    partes = linha.split(":")

                    if len(partes) != 2:
                        raise ValueError("formato esperado: Nome: nota")

                    nome = partes[0].strip()
                    nota = float(partes[1].strip())

                    if nota < 0 or nota > 10:
                        raise ValueError("nota fora do intervalo 0-10")

                    registros.append({
                        "nome": nome,
                        "nota": nota
                    })

                except ValueError as erro:
                    print(f"Linha {numero} ignorada: {erro}")

    except FileNotFoundError:
        print(f'Erro: arquivo "{caminho}" não encontrado.')

    return registros


def calcular_estatisticas(registros):
    """Calcula média, maior nota, menor nota e total de alunos."""
    soma = 0
    total = 0
    maior = registros[0]["nota"]
    menor = registros[0]["nota"]

    for aluno in registros:
        nota = aluno["nota"]

        soma += nota
        total += 1

        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

    return {
        "media": soma / total,
        "maior": maior,
        "menor": menor,
        "total": total
    }


def classificar_aluno(nota):
    """Retorna o status do aluno de acordo com a nota."""
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def imprimir_relatorio(registros, estatisticas):
    """Imprime o relatório final no terminal."""
    print("=" * 42)
    print("     RELATÓRIO DE NOTAS — TURMA 2026.1")
    print("=" * 42)
    print(f"{'ALUNO':<22} {'NOTA':>5}  STATUS")
    print("-" * 42)

    registros_ordenados = sorted(
        registros,
        key=lambda aluno: aluno["nota"],
        reverse=True
    )

    for aluno in registros_ordenados:
        print(
            f"{aluno['nome']:<22} "
            f"{aluno['nota']:>5.1f}  "
            f"{aluno['status']}"
        )

    print("-" * 42)
    print(
        f"Média: {estatisticas['media']:.2f}   "
        f"Maior: {estatisticas['maior']:.1f}   "
        f"Menor: {estatisticas['menor']:.1f}"
    )
    print("=" * 42)


def salvar_relatorio(registros, estatisticas, destino):
    """Salva o relatório em um arquivo JSON."""
    relatorio = {
        "turma": "2026.1",
        "estatisticas": estatisticas,
        "alunos": registros
    }

    with open(destino, "w", encoding="utf-8") as arquivo:
        json.dump(
            relatorio,
            arquivo,
            ensure_ascii=False,
            indent=2,
            sort_keys=True
        )

    print(f'Relatório salvo em "{destino}".')


if __name__ == "__main__":
    dados = ler_registros("notas.txt")

    if len(dados) > 0:
        for aluno in dados:
            aluno["status"] = classificar_aluno(aluno["nota"])

        estatisticas = calcular_estatisticas(dados)

        imprimir_relatorio(dados, estatisticas)
        salvar_relatorio(dados, estatisticas, "relatorio.json")
    else:
        print("Nenhum registro válido encontrado.")