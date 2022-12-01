class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        # if not len(self._data):
        #     return None
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        """Aqui irá sua implementação"""
        # if not len(self._data):
        #     return None
        if not 0 <= index < len(self._data):
            raise IndexError
        return self._data[index]
