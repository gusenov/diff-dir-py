## Общие сведения:

*diff-dir.py* - это скрипт на Питоне для рекурсивного сравнения содержимого двух папок.

Скрипт принимает на **входе** пути к двум папкам: оригиналу и копии. 

Далее скрипт рекурсивно поимённо сравнивает файлы из копии с файлами из оригинала.

В **вывод** попадают:
- файлы из копии, которые не идентичны по содержимому соответствующим файлам в оригинале;
- файлы из копии, которые отсутствуют в оригинале.

## Примеры использования:

1. Вывод справки по опциям: 

```bash
$ python diff-dir.py -h
diff-dir.py -o <origindir> -c <clonedir>
```

2. Использование длинных опций:

```bash
$ python diff-dir.py --odir /o/ri/gin/al/ --cdir /c/lo/ne/
```

3. Использование коротких опций:

```bash
$ python diff-dir.py -o /or/igi/na/l/ -c /cl/on/e/
```

## Информация, использованная при реализации:

- [tutorialspoint.com/python/python_command_line_arguments.htm](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
- [tutorialspoint.com/python/os_walk.htm](https://www.tutorialspoint.com/python/os_walk.htm)
- [pyformat.info/#simple](https://pyformat.info/#simple)
