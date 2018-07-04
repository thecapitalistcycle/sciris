# Import version information
from .version import version, versiondate

# Import core functions
from . import core

# Simplifying...
from .corelib.utils import *
from .corelib.colortools import *
from .corelib.odict import *
from .corelib.dataframe import *
from .corelib.fileio import loadspreadsheet, export_file # WARNING, make consistent

# Import web functions
try:
    from . import web
    webtext = 'with web library'
except Exception as webapp_exception:
    import traceback as _traceback
    web_error = _traceback.format_exc()
    webtext = 'without web library (see sciris.web_error for details)'

scirislicense = 'Sciris %s (%s)' % (version, versiondate)
print(scirislicense + ' ' + webtext)

del scirislicense, webtext # Remove unneeded variables