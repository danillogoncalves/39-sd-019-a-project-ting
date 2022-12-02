from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return
    list = txt_importer(path_file)
    dist = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(list),
        'linhas_do_arquivo': list,
    }

    instance.enqueue(dist)
    print(dist)


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    if not len(instance):
        return print('Não há elementos')
    dist = instance.dequeue()
    print(f"Arquivo {dist['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
