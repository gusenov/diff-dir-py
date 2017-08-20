## Общие сведения

*diff-dir.py* - это скрипт на Питоне для рекурсивного сравнения содержимого двух папок.

Скрипт рекурсивно поимённо сравнивает файлы из копии с файлами из оригинала.
Сравнение на идентичность проводится путем расчёта и сверки MD5-хешей от файлов.
Также можно включить построчное сравнение файлов.

## Входные данные

Скрипт принимает на входе пути к двум папкам: оригиналу и копии.

Путь к оригиналу указывается через длинную опцию **--odir** (в коротком варианте **-o**).

Путь к копии указывается через длинную опцию **--cdir** (в коротком варианте **-с**).

## Выходные данные

В вывод всегда попадают:
- файлы из копии, которые не идентичны по содержимому соответствующим файлам в оригинале;
- файлы из копии, которые отсутствуют в оригинале.

В вывод никогда не попадают:
- файлы из оригинала, которые отсутствуют в копии.

Формат вывода:

```text
* относительный/путь/к/файлу
- относительный/путь/к/файлу
```

Обозначения:

- звёздочка обозначает, что файл из копии не идентичен по содержимому соответствующему файлу в оригинале;
- минус обозначает, что файл из копии отсутствуют в оригинале.

## Переводы строк

В некоторых случаях файлы являются идентичными за исключением способа [перевода строки](https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4_%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8).
Если сравнивать такие файлы через их MD5-хеши, то они будут считаться различными.

```bash
$ python diff-dir.py --odir tests/line-endings/lf/ --cdir tests/line-endings/cr+lf/
* _languages.js
```

Поэтому у скрипта есть длинная опция **--line-by-line** (в коротком варианте **-l**), которая включает дополнительное сравнение файлов по строкам.
При использовании этой опции, если у файлов различные MD5-хеши, но при построковом сравнении они равны, то эти файлы будут считаться идентичными.

```bash
$ python diff-dir.py -o tests/line-endings/lf/ -c tests/line-endings/cr+lf/ -l
```

Для того чтобы избежать построчного сравнения бинарных файлов в константе [BINARY](https://github.com/gusenov/diff-dir-py/blob/master/diff-dir.py#L10) перечислены расширения для которых не нужно проводить построчное сравнение.

## Примеры использования скрипта diff-dir.py в качестве инструмента

1. Вывод справки по коротким опциям:

```bash
$ python diff-dir.py -h
diff-dir.py -o <origindir> -c <clonedir> -l
```

2. Вывод справки по длинным опциям:

```bash
$ python diff-dir.py --help
diff-dir.py --odir <origindir> --cdir <clonedir> --line-by-line
```

3. Использование длинных опций:

```bash
$ python diff-dir.py --odir /o/ri/gin/al/ --cdir /c/lo/ne/ --line-by-line
```

4. Использование коротких опций:

```bash
$ python diff-dir.py -o /or/igi/na/l/ -c /cl/on/e/ -l
```

## Пакет [diff-dir-py](https://pypi.python.org/pypi/diff-dir-py) в [Python Package Index](https://pypi.python.org/pypi)

Установка пакета в *~/.local/lib/python3.5/site-packages/*:

```bash
$ pip install diff-dir-py --user
```

Использование пакета в своём коде:

Функция *diffdir.cmp* является генератором кортежей из двух элементов: (путь к файлу, статус по нему).

```python
import diffdir

origin = "/o/ri/gin/al/"
clone = "/c/lo/ne/"

difference = diffdir.cmp(origin, clone, True)

for path, status in difference:
    print("{} {}".format(status, path))
```

Результат исполнения вышеприведённого кода:

```text
* относительный/путь/к/файлу
- относительный/путь/к/файлу
```

Удаление пакета:

```bash
$ pip uninstall diff-dir-py
```

## Исходный код проекта

- [Как считываются аргументы командной строки](https://github.com/gusenov/diff-dir-py/blob/master/diffdir/diff-dir.py#L75)
- [Как рассчитывается MD5-хеш от файла](https://github.com/gusenov/diff-dir-py/blob/master/diffdir/diff-dir.py#L44)
- [Как файлы сравниваются построчно](https://github.com/gusenov/diff-dir-py/blob/master/diffdir/diff-dir.py#L52)
- [Как импортируется модуль в названии, которого есть минус](https://github.com/gusenov/diff-dir-py/blob/master/diffdir/__init__.py#L1)

## Информация, использованная при реализации

Стандартная библиотека:

- [tutorialspoint.com/python/python_command_line_arguments.htm](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
- [tutorialspoint.com/python/os_walk.htm](https://www.tutorialspoint.com/python/os_walk.htm)
- [pyformat.info/#simple](https://pyformat.info/#simple)

Юникод:

- [stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-£](https://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3)

Переводы строк:

- [stackoverflow.com/questions/12330522/reading-a-file-without-newlines](https://stackoverflow.com/questions/12330522/reading-a-file-without-newlines)
- [stackoverflow.com/questions/3860519/see-line-breaks-and-carriage-returns-in-editor](https://stackoverflow.com/questions/3860519/see-line-breaks-and-carriage-returns-in-editor)

Импорт модулей:

- [stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them](https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them)
- [stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it](https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it)
- [stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string](https://stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string)
- [ru.stackoverflow.com/questions/420987/Обращение-к-функции-заданной-в-init-py](https://ru.stackoverflow.com/questions/420987/%D0%9E%D0%B1%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%BD%D0%BE%D0%B9-%D0%B2-init-py)
- [ibm.com/developerworks/ru/library/l-python_part_5/index.html](https://www.ibm.com/developerworks/ru/library/l-python_part_5/index.html)
- [pep8.ru/doc/tutorial-3.1/6.html](http://pep8.ru/doc/tutorial-3.1/6.html)
- [stackoverflow.com/questions/36515197/python-import-module-from-a-package](https://stackoverflow.com/questions/36515197/python-import-module-from-a-package)

Каталог пакетов [Python Package Index](https://pypi.python.org/pypi):

- [peterdowns.com/posts/first-time-with-pypi.html](http://peterdowns.com/posts/first-time-with-pypi.html)
- [docs.python.org/3.7/distutils/packageindex.html](https://docs.python.org/3.7/distutils/packageindex.html)
- [packaging.python.org/tutorials/distributing-packages](https://packaging.python.org/tutorials/distributing-packages)
- [pypi.python.org/pypi?:action=list_classifiers](https://pypi.python.org/pypi?%3Aaction=list_classifiers)
- [packaging.python.org/guides/using-testpypi](https://packaging.python.org/guides/using-testpypi)

Система управления пакетами pip:

- [stackoverflow.com/questions/34514703/pip-install-from-pypi-works-but-from-testpypi-fails-cannot-find-requirements](https://stackoverflow.com/questions/34514703/pip-install-from-pypi-works-but-from-testpypi-fails-cannot-find-requirements)
- [pip.pypa.io/en/stable/reference/pip_uninstall](https://pip.pypa.io/en/stable/reference/pip_uninstall)