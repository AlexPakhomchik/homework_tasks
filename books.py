import os

path = ''

class FindBooks:
    directory = path

    @property
    def folder(self):
        return self.directory

    @folder.setter
    def folder(self, new_folder):
        if not new_folder:
            self.directory = new_folder

    def search_word(self, word):
        with os.scandir(self.directory) as books:
            for i in books:
                os.chdir(self.directory)
                x = open(i.name)
                while True:
                    try:
                        line = x.readline()
                    except UnicodeDecodeError:
                        pass
                    if not line:
                        break
                    if word in line:
                        print(i.name)
                        break

    def find_overlap(self, *args):
        for word in args:
            print(f'Поиск слова "{word}" начался, найдены следующие книги:\n')
            self.search_word(word)
            print('\nПоиск закончен')
            print('_______________________________________________________')


a = FindBooks()
