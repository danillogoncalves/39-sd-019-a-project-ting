import sys

# https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if not path_file[len(path_file) - 4:] == '.txt':
            sys.stderr.write('Formato inválido\n')
        else:
            with open(path_file, encoding='utf-8', mode='r') as file:
                return file.read().split('\n')
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
