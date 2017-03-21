import sys
from setuptools import setup, Extension
from distutils.sysconfig import get_python_inc

import os
from glob import *

CEGUI_BASEDIR = os.environ["CEGUI_DIR"]
is_64bits = sys.maxsize > 2**32
BOOST_LIBRARYDIR = os.environ["BOOST_LIBRARYDIR"]



setup(
    name = "PyCEGUI",
    version = "0.8",
    description = "Python bindings for CEGUI library",
    long_description =
"""Crazy Eddie's GUI System is a free library providing windowing
and widgets for graphics APIs / engines where such functionality
is not natively available, or severely lacking. The library is
object orientated, written in C++, and targeted at games developers
who should be spending their time creating great games, not building GUI sub-systems.

note: For Linux and MacOSX packages, see http://www.cegui.org.uk, we provide them
      in SDKs. Distutils package is only provided for Windows since it's hard to
      install the binding there as it involves lots of wrappers and nasty tricks.
      Shame on you Windows!""",
    author = "CEGUI team",
    author_email = "team@cegui.org.uk",
    #maintainer = "Martin Preisler", # authors get shadowed by this
    #maintainer_email = "preisler.m@gmail.com",
    url = "http://www.cegui.org.uk",
    license = "MIT",
    platforms = ["Windows", "Linux", "MacOSX"],
    
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: C++"
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Widget Sets",
    ],
    
    # the first string is directory where the files should go
    # - leave empty for C:/Python26 for example
    data_files = [
        ("Lib/site-packages", ["pycegui.pth"]),
        # we have to bundle CEGUIBase.dll, CEGUIOpenGLRenderer.dll, etc...
        ("Lib/site-packages/PyCEGUI",
        # this is obviously a workaround, I would be happy to hear what the clean
        # solution should look like
            glob(".\PyCEGUI\*.pyd") +
            glob(os.path.join(BOOST_LIBRARYDIR, "boost_python*.dll")) +
            [
                CEGUI_BASEDIR + "/bin/CEGUIBase-0.dll",
                CEGUI_BASEDIR + "/bin/freetype.dll",
                CEGUI_BASEDIR + "/bin/pcre.dll",
                CEGUI_BASEDIR + "/bin/minizip.dll",
                CEGUI_BASEDIR + "/bin/CEGUIOpenGLRenderer-0.dll",
                CEGUI_BASEDIR + "/bin/glew.dll",
            ]
        ),
        ("Lib/site-packages/PyCEGUI/extra_dlls",
            [
                CEGUI_BASEDIR + "/bin/zlib.dll",
                CEGUI_BASEDIR + "/bin/CEGUICommonDialogs-0.dll",
                CEGUI_BASEDIR + "/bin/CEGUICoreWindowRendererSet.dll",
                CEGUI_BASEDIR + "/bin/CEGUISillyImageCodec.dll",
                CEGUI_BASEDIR + "/bin/silly.dll",
                CEGUI_BASEDIR + "/bin/libpng.dll",
                CEGUI_BASEDIR + "/bin/jpeg.dll",
                CEGUI_BASEDIR + "/bin/CEGUIExpatParser.dll",
                CEGUI_BASEDIR + "/bin/libexpat.dll",
            ]
        ),
        # distutils doesn't allow to bundle folders (or to be precise: I have no idea how to do that)
        # therefore I do this the ugly way!
        ("Lib/site-packages/PyCEGUI/datafiles/animations",
           glob(os.path.join(CEGUI_BASEDIR + "/datafiles/animations", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/configs",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/configs", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/fonts",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/fonts", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/imagesets",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/imagesets", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/layouts",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/layouts", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/looknfeel",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/looknfeel", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/lua_scripts",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/lua_scripts", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/schemes",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/schemes", "*")),
        ),
        ("Lib/site-packages/PyCEGUI/datafiles/xml_schemas",
            glob(os.path.join(CEGUI_BASEDIR + "/datafiles/xml_schemas", "*")),
        )
    ]
)
