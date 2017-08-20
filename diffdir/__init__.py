from importlib import import_module
p, m = 'diffdir.diff-dir.cmp'.rsplit('.', 1)
mod = import_module(p)
cmp = getattr(mod, m)
