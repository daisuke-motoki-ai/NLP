# jupyter software layer ドキュメント


## reloadの使用

以下のように変更することによって，モジュールを変更した際にいちいちjupyterやIpythonを起動し直さなくて良くなる．

```py
import my_func as mf
# $PYTHON_PROGRAM/my_setting.py
import my_setting as st
# $PYTHON_PROGRAM/my_init.py
import my_init as mi

reload(mf)
reload(st)
reload(mi)
```

ref. [reloadで強制import](http://python.dogrow.net/?p=65)
