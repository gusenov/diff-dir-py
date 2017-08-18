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

```bash
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

## Примеры использования

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

## Исходный код

- [Как считываются аргументы командной строки](https://github.com/gusenov/diff-dir-py/blob/master/diff-dir.py#L75)
- [Как рассчитывается MD5-хеш от файла](https://github.com/gusenov/diff-dir-py/blob/master/diff-dir.py#L44)
- [Как файлы сравниваются построчно](https://github.com/gusenov/diff-dir-py/blob/master/diff-dir.py#L52)

## Информация, использованная при реализации

- [tutorialspoint.com/python/python_command_line_arguments.htm](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
- [tutorialspoint.com/python/os_walk.htm](https://www.tutorialspoint.com/python/os_walk.htm)
- [pyformat.info/#simple](https://pyformat.info/#simple)
- [stackoverflow.com/questions/12330522/reading-a-file-without-newlines](https://stackoverflow.com/questions/12330522/reading-a-file-without-newlines)
- [stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-£](https://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3)
- [stackoverflow.com/questions/3860519/see-line-breaks-and-carriage-returns-in-editor](https://stackoverflow.com/questions/3860519/see-line-breaks-and-carriage-returns-in-editor)
