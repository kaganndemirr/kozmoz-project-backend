# Standard Library
import getpass

# Local Django
from kozmoz.settings.base import *

if getpass.getuser() in ['root']:
    from kozmoz.settings.production import *
else:
    from kozmoz.settings.staging import *
