'''OpenGL extension ARB.shader_viewport_layer_array

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_viewport_layer_array to provide a more 
Python-friendly API

Overview (from the spec)
	
	The gl_ViewportIndex and gl_Layer built-in variables were introduced by
	the in OpenGL 4.1. These variables are available in un-extended OpenGL
	only to the geometry shader. When written in the geometry shader, they
	cause geometry to be directed to one of an array of several independent
	viewport rectangles or framebuffer attachment layers, respectively.
	
	In order to use any viewport or attachment layer other than zero, a
	geometry shader must be present. Geometry shaders introduce processing
	overhead and potential performance issues. The AMD_vertex_shader_layer
	and AMD_vertex_shader_viewport_index extensions allowed the gl_Layer
	and gl_ViewportIndex outputs to be written directly from the vertex shader
	with no geometry shader present.
	
	This extension effectively merges the AMD_vertex_shader_layer and
	AMD_vertex_shader_viewport_index extensions together and extends them further
	to allow both outputs to be written from tessellation evaluation shaders.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shader_viewport_layer_array.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.shader_viewport_layer_array import *
from OpenGL.raw.GL.ARB.shader_viewport_layer_array import _EXTENSION_NAME

def glInitShaderViewportLayerArrayARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION