from ting_file_management.queue import Queue


def with_content(postion: int, phrase: str, need_content: bool):
    if need_content:
        return {"linha": postion, "conteudo": phrase}
    return {"linha": postion}


def exists_word(word: str, instance: Queue, need_content: bool = False):
    """Aqui irá sua implementação"""
    result = []
    for index in range(len(instance)):
        row = instance.search(index)

        list = [
            with_content(position + 1, line, need_content)
            for position, line in enumerate(row["linhas_do_arquivo"])
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
    return exists_word(word, instance, True)
