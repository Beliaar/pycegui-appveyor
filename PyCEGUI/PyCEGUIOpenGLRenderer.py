import sys
import os
if sys.platform == "win32":
    os.environ["PATH"]= os.path.split(__file__)[0] + ";" + os.environ["PATH"]
from pyd.PyCEGUIOpenGLRenderer import *
