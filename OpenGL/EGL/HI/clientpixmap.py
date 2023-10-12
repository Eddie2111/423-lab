'''OpenGL extension HI.clientpixmap

This module customises the behaviour of the 
OpenGL.raw.EGL.HI.clientpixmap to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/HI/clientpixmap.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.HI.clientpixmap import *
from OpenGL.raw.EGL.HI.clientpixmap import _EXTENSION_NAME

def glInitClientpixmapHI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION