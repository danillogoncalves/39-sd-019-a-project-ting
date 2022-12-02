from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""
    result = []
    for index in range(len(instance)):
        row = instance.search(index)

        list = [
            {"linha": (position + 1)}
            for position, line in enumerate(row['linhas_do_arquivo'])
            if word.lower() in line.lower()
        ]

        item = {
            "palavra": word,
            "arquivo": row["nome_do_arquivo"],
            "ocorrencias": list,
        }

        if list:
            result.append(item)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
