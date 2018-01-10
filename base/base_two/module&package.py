#package is paper file,it must include _init_.py
#module is a .py file in the package
#inport package.module
try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python':2.7})
#pip install web.py