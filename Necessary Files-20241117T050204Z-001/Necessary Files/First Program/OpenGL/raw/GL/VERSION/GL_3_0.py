'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_VERSION_GL_3_0'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_VERSION_GL_3_0',error_checker=_errors._error_checker)
GL_ALPHA_INTEGER=_C('GL_ALPHA_INTEGER',0x8D97)
GL_BGRA_INTEGER=_C('GL_BGRA_INTEGER',0x8D9B)
GL_BGR_INTEGER=_C('GL_BGR_INTEGER',0x8D9A)
GL_BLUE_INTEGER=_C('GL_BLUE_INTEGER',0x8D96)
GL_BUFFER_ACCESS_FLAGS=_C('GL_BUFFER_ACCESS_FLAGS',0x911F)
GL_BUFFER_MAP_LENGTH=_C('GL_BUFFER_MAP_LENGTH',0x9120)
GL_BUFFER_MAP_OFFSET=_C('GL_BUFFER_MAP_OFFSET',0x9121)
GL_CLAMP_FRAGMENT_COLOR=_C('GL_CLAMP_FRAGMENT_COLOR',0x891B)
GL_CLAMP_READ_COLOR=_C('GL_CLAMP_READ_COLOR',0x891C)
GL_CLAMP_VERTEX_COLOR=_C('GL_CLAMP_VERTEX_COLOR',0x891A)
GL_CLIP_DISTANCE0=_C('GL_CLIP_DISTANCE0',0x3000)
GL_CLIP_DISTANCE1=_C('GL_CLIP_DISTANCE1',0x3001)
GL_CLIP_DISTANCE2=_C('GL_CLIP_DISTANCE2',0x3002)
GL_CLIP_DISTANCE3=_C('GL_CLIP_DISTANCE3',0x3003)
GL_CLIP_DISTANCE4=_C('GL_CLIP_DISTANCE4',0x3004)
GL_CLIP_DISTANCE5=_C('GL_CLIP_DISTANCE5',0x3005)
GL_CLIP_DISTANCE6=_C('GL_CLIP_DISTANCE6',0x3006)
GL_CLIP_DISTANCE7=_C('GL_CLIP_DISTANCE7',0x3007)
GL_COLOR_ATTACHMENT0=_C('GL_COLOR_ATTACHMENT0',0x8CE0)
GL_COLOR_ATTACHMENT1=_C('GL_COLOR_ATTACHMENT1',0x8CE1)
GL_COLOR_ATTACHMENT10=_C('GL_COLOR_ATTACHMENT10',0x8CEA)
GL_COLOR_ATTACHMENT11=_C('GL_COLOR_ATTACHMENT11',0x8CEB)
GL_COLOR_ATTACHMENT12=_C('GL_COLOR_ATTACHMENT12',0x8CEC)
GL_COLOR_ATTACHMENT13=_C('GL_COLOR_ATTACHMENT13',0x8CED)
GL_COLOR_ATTACHMENT14=_C('GL_COLOR_ATTACHMENT14',0x8CEE)
GL_COLOR_ATTACHMENT15=_C('GL_COLOR_ATTACHMENT15',0x8CEF)
GL_COLOR_ATTACHMENT16=_C('GL_COLOR_ATTACHMENT16',0x8CF0)
GL_COLOR_ATTACHMENT17=_C('GL_COLOR_ATTACHMENT17',0x8CF1)
GL_COLOR_ATTACHMENT18=_C('GL_COLOR_ATTACHMENT18',0x8CF2)
GL_COLOR_ATTACHMENT19=_C('GL_COLOR_ATTACHMENT19',0x8CF3)
GL_COLOR_ATTACHMENT2=_C('GL_COLOR_ATTACHMENT2',0x8CE2)
GL_COLOR_ATTACHMENT20=_C('GL_COLOR_ATTACHMENT20',0x8CF4)
GL_COLOR_ATTACHMENT21=_C('GL_COLOR_ATTACHMENT21',0x8CF5)
GL_COLOR_ATTACHMENT22=_C('GL_COLOR_ATTACHMENT22',0x8CF6)
GL_COLOR_ATTACHMENT23=_C('GL_COLOR_ATTACHMENT23',0x8CF7)
GL_COLOR_ATTACHMENT24=_C('GL_COLOR_ATTACHMENT24',0x8CF8)
GL_COLOR_ATTACHMENT25=_C('GL_COLOR_ATTACHMENT25',0x8CF9)
GL_COLOR_ATTACHMENT26=_C('GL_COLOR_ATTACHMENT26',0x8CFA)
GL_COLOR_ATTACHMENT27=_C('GL_COLOR_ATTACHMENT27',0x8CFB)
GL_COLOR_ATTACHMENT28=_C('GL_COLOR_ATTACHMENT28',0x8CFC)
GL_COLOR_ATTACHMENT29=_C('GL_COLOR_ATTACHMENT29',0x8CFD)
GL_COLOR_ATTACHMENT3=_C('GL_COLOR_ATTACHMENT3',0x8CE3)
GL_COLOR_ATTACHMENT30=_C('GL_COLOR_ATTACHMENT30',0x8CFE)
GL_COLOR_ATTACHMENT31=_C('GL_COLOR_ATTACHMENT31',0x8CFF)
GL_COLOR_ATTACHMENT4=_C('GL_COLOR_ATTACHMENT4',0x8CE4)
GL_COLOR_ATTACHMENT5=_C('GL_COLOR_ATTACHMENT5',0x8CE5)
GL_COLOR_ATTACHMENT6=_C('GL_COLOR_ATTACHMENT6',0x8CE6)
GL_COLOR_ATTACHMENT7=_C('GL_COLOR_ATTACHMENT7',0x8CE7)
GL_COLOR_ATTACHMENT8=_C('GL_COLOR_ATTACHMENT8',0x8CE8)
GL_COLOR_ATTACHMENT9=_C('GL_COLOR_ATTACHMENT9',0x8CE9)
GL_COMPARE_REF_TO_TEXTURE=_C('GL_COMPARE_REF_TO_TEXTURE',0x884E)
GL_COMPRESSED_RED=_C('GL_COMPRESSED_RED',0x8225)
GL_COMPRESSED_RED_RGTC1=_C('GL_COMPRESSED_RED_RGTC1',0x8DBB)
GL_COMPRESSED_RG=_C('GL_COMPRESSED_RG',0x8226)
GL_COMPRESSED_RG_RGTC2=_C('GL_COMPRESSED_RG_RGTC2',0x8DBD)
GL_COMPRESSED_SIGNED_RED_RGTC1=_C('GL_COMPRESSED_SIGNED_RED_RGTC1',0x8DBC)
GL_COMPRESSED_SIGNED_RG_RGTC2=_C('GL_COMPRESSED_SIGNED_RG_RGTC2',0x8DBE)
GL_CONTEXT_FLAGS=_C('GL_CONTEXT_FLAGS',0x821E)
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT=_C('GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT',0x00000001)
GL_DEPTH24_STENCIL8=_C('GL_DEPTH24_STENCIL8',0x88F0)
GL_DEPTH32F_STENCIL8=_C('GL_DEPTH32F_STENCIL8',0x8CAD)
GL_DEPTH_ATTACHMENT=_C('GL_DEPTH_ATTACHMENT',0x8D00)
GL_DEPTH_COMPONENT32F=_C('GL_DEPTH_COMPONENT32F',0x8CAC)
GL_DEPTH_STENCIL=_C('GL_DEPTH_STENCIL',0x84F9)
GL_DEPTH_STENCIL_ATTACHMENT=_C('GL_DEPTH_STENCIL_ATTACHMENT',0x821A)
GL_DRAW_FRAMEBUFFER=_C('GL_DRAW_FRAMEBUFFER',0x8CA9)
GL_DRAW_FRAMEBUFFER_BINDING=_C('GL_DRAW_FRAMEBUFFER_BINDING',0x8CA6)
GL_FIXED_ONLY=_C('GL_FIXED_ONLY',0x891D)
GL_FLOAT_32_UNSIGNED_INT_24_8_REV=_C('GL_FLOAT_32_UNSIGNED_INT_24_8_REV',0x8DAD)
GL_FRAMEBUFFER=_C('GL_FRAMEBUFFER',0x8D40)
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE',0x8215)
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE',0x8214)
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING=_C('GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING',0x8210)
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE=_C('GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE',0x8211)
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE',0x8216)
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE',0x8213)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME',0x8CD1)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE',0x8CD0)
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE',0x8212)
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE',0x8217)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE',0x8CD3)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER',0x8CD4)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL',0x8CD2)
GL_FRAMEBUFFER_BINDING=_C('GL_FRAMEBUFFER_BINDING',0x8CA6)
GL_FRAMEBUFFER_COMPLETE=_C('GL_FRAMEBUFFER_COMPLETE',0x8CD5)
GL_FRAMEBUFFER_DEFAULT=_C('GL_FRAMEBUFFER_DEFAULT',0x8218)
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT=_C('GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT',0x8CD6)
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER=_C('GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER',0x8CDB)
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT=_C('GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT',0x8CD7)
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE=_C('GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE',0x8D56)
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER=_C('GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER',0x8CDC)
GL_FRAMEBUFFER_SRGB=_C('GL_FRAMEBUFFER_SRGB',0x8DB9)
GL_FRAMEBUFFER_UNDEFINED=_C('GL_FRAMEBUFFER_UNDEFINED',0x8219)
GL_FRAMEBUFFER_UNSUPPORTED=_C('GL_FRAMEBUFFER_UNSUPPORTED',0x8CDD)
GL_GREEN_INTEGER=_C('GL_GREEN_INTEGER',0x8D95)
GL_HALF_FLOAT=_C('GL_HALF_FLOAT',0x140B)
GL_INDEX=_C('GL_INDEX',0x8222)
GL_INTERLEAVED_ATTRIBS=_C('GL_INTERLEAVED_ATTRIBS',0x8C8C)
GL_INT_SAMPLER_1D=_C('GL_INT_SAMPLER_1D',0x8DC9)
GL_INT_SAMPLER_1D_ARRAY=_C('GL_INT_SAMPLER_1D_ARRAY',0x8DCE)
GL_INT_SAMPLER_2D=_C('GL_INT_SAMPLER_2D',0x8DCA)
GL_INT_SAMPLER_2D_ARRAY=_C('GL_INT_SAMPLER_2D_ARRAY',0x8DCF)
GL_INT_SAMPLER_3D=_C('GL_INT_SAMPLER_3D',0x8DCB)
GL_INT_SAMPLER_CUBE=_C('GL_INT_SAMPLER_CUBE',0x8DCC)
GL_INVALID_FRAMEBUFFER_OPERATION=_C('GL_INVALID_FRAMEBUFFER_OPERATION',0x0506)
GL_MAJOR_VERSION=_C('GL_MAJOR_VERSION',0x821B)
GL_MAP_FLUSH_EXPLICIT_BIT=_C('GL_MAP_FLUSH_EXPLICIT_BIT',0x0010)
GL_MAP_INVALIDATE_BUFFER_BIT=_C('GL_MAP_INVALIDATE_BUFFER_BIT',0x0008)
GL_MAP_INVALIDATE_RANGE_BIT=_C('GL_MAP_INVALIDATE_RANGE_BIT',0x0004)
GL_MAP_READ_BIT=_C('GL_MAP_READ_BIT',0x0001)
GL_MAP_UNSYNCHRONIZED_BIT=_C('GL_MAP_UNSYNCHRONIZED_BIT',0x0020)
GL_MAP_WRITE_BIT=_C('GL_MAP_WRITE_BIT',0x0002)
GL_MAX_ARRAY_TEXTURE_LAYERS=_C('GL_MAX_ARRAY_TEXTURE_LAYERS',0x88FF)
GL_MAX_CLIP_DISTANCES=_C('GL_MAX_CLIP_DISTANCES',0x0D32)
GL_MAX_COLOR_ATTACHMENTS=_C('GL_MAX_COLOR_ATTACHMENTS',0x8CDF)
GL_MAX_PROGRAM_TEXEL_OFFSET=_C('GL_MAX_PROGRAM_TEXEL_OFFSET',0x8905)
GL_MAX_RENDERBUFFER_SIZE=_C('GL_MAX_RENDERBUFFER_SIZE',0x84E8)
GL_MAX_SAMPLES=_C('GL_MAX_SAMPLES',0x8D57)
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS=_C('GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS',0x8C8A)
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS=_C('GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS',0x8C8B)
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS=_C('GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS',0x8C80)
GL_MAX_VARYING_COMPONENTS=_C('GL_MAX_VARYING_COMPONENTS',0x8B4B)
GL_MINOR_VERSION=_C('GL_MINOR_VERSION',0x821C)
GL_MIN_PROGRAM_TEXEL_OFFSET=_C('GL_MIN_PROGRAM_TEXEL_OFFSET',0x8904)
GL_NUM_EXTENSIONS=_C('GL_NUM_EXTENSIONS',0x821D)
GL_PRIMITIVES_GENERATED=_C('GL_PRIMITIVES_GENERATED',0x8C87)
GL_PROXY_TEXTURE_1D_ARRAY=_C('GL_PROXY_TEXTURE_1D_ARRAY',0x8C19)
GL_PROXY_TEXTURE_2D_ARRAY=_C('GL_PROXY_TEXTURE_2D_ARRAY',0x8C1B)
GL_QUERY_BY_REGION_NO_WAIT=_C('GL_QUERY_BY_REGION_NO_WAIT',0x8E16)
GL_QUERY_BY_REGION_WAIT=_C('GL_QUERY_BY_REGION_WAIT',0x8E15)
GL_QUERY_NO_WAIT=_C('GL_QUERY_NO_WAIT',0x8E14)
GL_QUERY_WAIT=_C('GL_QUERY_WAIT',0x8E13)
GL_R11F_G11F_B10F=_C('GL_R11F_G11F_B10F',0x8C3A)
GL_R16=_C('GL_R16',0x822A)
GL_R16F=_C('GL_R16F',0x822D)
GL_R16I=_C('GL_R16I',0x8233)
GL_R16UI=_C('GL_R16UI',0x8234)
GL_R32F=_C('GL_R32F',0x822E)
GL_R32I=_C('GL_R32I',0x8235)
GL_R32UI=_C('GL_R32UI',0x8236)
GL_R8=_C('GL_R8',0x8229)
GL_R8I=_C('GL_R8I',0x8231)
GL_R8UI=_C('GL_R8UI',0x8232)
GL_RASTERIZER_DISCARD=_C('GL_RASTERIZER_DISCARD',0x8C89)
GL_READ_FRAMEBUFFER=_C('GL_READ_FRAMEBUFFER',0x8CA8)
GL_READ_FRAMEBUFFER_BINDING=_C('GL_READ_FRAMEBUFFER_BINDING',0x8CAA)
GL_RED_INTEGER=_C('GL_RED_INTEGER',0x8D94)
GL_RENDERBUFFER=_C('GL_RENDERBUFFER',0x8D41)
GL_RENDERBUFFER_ALPHA_SIZE=_C('GL_RENDERBUFFER_ALPHA_SIZE',0x8D53)
GL_RENDERBUFFER_BINDING=_C('GL_RENDERBUFFER_BINDING',0x8CA7)
GL_RENDERBUFFER_BLUE_SIZE=_C('GL_RENDERBUFFER_BLUE_SIZE',0x8D52)
GL_RENDERBUFFER_DEPTH_SIZE=_C('GL_RENDERBUFFER_DEPTH_SIZE',0x8D54)
GL_RENDERBUFFER_GREEN_SIZE=_C('GL_RENDERBUFFER_GREEN_SIZE',0x8D51)
GL_RENDERBUFFER_HEIGHT=_C('GL_RENDERBUFFER_HEIGHT',0x8D43)
GL_RENDERBUFFER_INTERNAL_FORMAT=_C('GL_RENDERBUFFER_INTERNAL_FORMAT',0x8D44)
GL_RENDERBUFFER_RED_SIZE=_C('GL_RENDERBUFFER_RED_SIZE',0x8D50)
GL_RENDERBUFFER_SAMPLES=_C('GL_RENDERBUFFER_SAMPLES',0x8CAB)
GL_RENDERBUFFER_STENCIL_SIZE=_C('GL_RENDERBUFFER_STENCIL_SIZE',0x8D55)
GL_RENDERBUFFER_WIDTH=_C('GL_RENDERBUFFER_WIDTH',0x8D42)
GL_RG=_C('GL_RG',0x8227)
GL_RG16=_C('GL_RG16',0x822C)
GL_RG16F=_C('GL_RG16F',0x822F)
GL_RG16I=_C('GL_RG16I',0x8239)
GL_RG16UI=_C('GL_RG16UI',0x823A)
GL_RG32F=_C('GL_RG32F',0x8230)
GL_RG32I=_C('GL_RG32I',0x823B)
GL_RG32UI=_C('GL_RG32UI',0x823C)
GL_RG8=_C('GL_RG8',0x822B)
GL_RG8I=_C('GL_RG8I',0x8237)
GL_RG8UI=_C('GL_RG8UI',0x8238)
GL_RGB16F=_C('GL_RGB16F',0x881B)
GL_RGB16I=_C('GL_RGB16I',0x8D89)
GL_RGB16UI=_C('GL_RGB16UI',0x8D77)
GL_RGB32F=_C('GL_RGB32F',0x8815)
GL_RGB32I=_C('GL_RGB32I',0x8D83)
GL_RGB32UI=_C('GL_RGB32UI',0x8D71)
GL_RGB8I=_C('GL_RGB8I',0x8D8F)
GL_RGB8UI=_C('GL_RGB8UI',0x8D7D)
GL_RGB9_E5=_C('GL_RGB9_E5',0x8C3D)
GL_RGBA16F=_C('GL_RGBA16F',0x881A)
GL_RGBA16I=_C('GL_RGBA16I',0x8D88)
GL_RGBA16UI=_C('GL_RGBA16UI',0x8D76)
GL_RGBA32F=_C('GL_RGBA32F',0x8814)
GL_RGBA32I=_C('GL_RGBA32I',0x8D82)
GL_RGBA32UI=_C('GL_RGBA32UI',0x8D70)
GL_RGBA8I=_C('GL_RGBA8I',0x8D8E)
GL_RGBA8UI=_C('GL_RGBA8UI',0x8D7C)
GL_RGBA_INTEGER=_C('GL_RGBA_INTEGER',0x8D99)
GL_RGB_INTEGER=_C('GL_RGB_INTEGER',0x8D98)
GL_RG_INTEGER=_C('GL_RG_INTEGER',0x8228)
GL_SAMPLER_1D_ARRAY=_C('GL_SAMPLER_1D_ARRAY',0x8DC0)
GL_SAMPLER_1D_ARRAY_SHADOW=_C('GL_SAMPLER_1D_ARRAY_SHADOW',0x8DC3)
GL_SAMPLER_2D_ARRAY=_C('GL_SAMPLER_2D_ARRAY',0x8DC1)
GL_SAMPLER_2D_ARRAY_SHADOW=_C('GL_SAMPLER_2D_ARRAY_SHADOW',0x8DC4)
GL_SAMPLER_CUBE_SHADOW=_C('GL_SAMPLER_CUBE_SHADOW',0x8DC5)
GL_SEPARATE_ATTRIBS=_C('GL_SEPARATE_ATTRIBS',0x8C8D)
GL_STENCIL_ATTACHMENT=_C('GL_STENCIL_ATTACHMENT',0x8D20)
GL_STENCIL_INDEX1=_C('GL_STENCIL_INDEX1',0x8D46)
GL_STENCIL_INDEX16=_C('GL_STENCIL_INDEX16',0x8D49)
GL_STENCIL_INDEX4=_C('GL_STENCIL_INDEX4',0x8D47)
GL_STENCIL_INDEX8=_C('GL_STENCIL_INDEX8',0x8D48)
GL_TEXTURE_1D_ARRAY=_C('GL_TEXTURE_1D_ARRAY',0x8C18)
GL_TEXTURE_2D_ARRAY=_C('GL_TEXTURE_2D_ARRAY',0x8C1A)
GL_TEXTURE_ALPHA_TYPE=_C('GL_TEXTURE_ALPHA_TYPE',0x8C13)
GL_TEXTURE_BINDING_1D_ARRAY=_C('GL_TEXTURE_BINDING_1D_ARRAY',0x8C1C)
GL_TEXTURE_BINDING_2D_ARRAY=_C('GL_TEXTURE_BINDING_2D_ARRAY',0x8C1D)
GL_TEXTURE_BLUE_TYPE=_C('GL_TEXTURE_BLUE_TYPE',0x8C12)
GL_TEXTURE_DEPTH_TYPE=_C('GL_TEXTURE_DEPTH_TYPE',0x8C16)
GL_TEXTURE_GREEN_TYPE=_C('GL_TEXTURE_GREEN_TYPE',0x8C11)
GL_TEXTURE_INTENSITY_TYPE=_C('GL_TEXTURE_INTENSITY_TYPE',0x8C15)
GL_TEXTURE_LUMINANCE_TYPE=_C('GL_TEXTURE_LUMINANCE_TYPE',0x8C14)
GL_TEXTURE_RED_TYPE=_C('GL_TEXTURE_RED_TYPE',0x8C10)
GL_TEXTURE_SHARED_SIZE=_C('GL_TEXTURE_SHARED_SIZE',0x8C3F)
GL_TEXTURE_STENCIL_SIZE=_C('GL_TEXTURE_STENCIL_SIZE',0x88F1)
GL_TRANSFORM_FEEDBACK_BUFFER=_C('GL_TRANSFORM_FEEDBACK_BUFFER',0x8C8E)
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING=_C('GL_TRANSFORM_FEEDBACK_BUFFER_BINDING',0x8C8F)
GL_TRANSFORM_FEEDBACK_BUFFER_MODE=_C('GL_TRANSFORM_FEEDBACK_BUFFER_MODE',0x8C7F)
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE=_C('GL_TRANSFORM_FEEDBACK_BUFFER_SIZE',0x8C85)
GL_TRANSFORM_FEEDBACK_BUFFER_START=_C('GL_TRANSFORM_FEEDBACK_BUFFER_START',0x8C84)
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN=_C('GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN',0x8C88)
GL_TRANSFORM_FEEDBACK_VARYINGS=_C('GL_TRANSFORM_FEEDBACK_VARYINGS',0x8C83)
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH=_C('GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH',0x8C76)
GL_UNSIGNED_INT_10F_11F_11F_REV=_C('GL_UNSIGNED_INT_10F_11F_11F_REV',0x8C3B)
GL_UNSIGNED_INT_24_8=_C('GL_UNSIGNED_INT_24_8',0x84FA)
GL_UNSIGNED_INT_5_9_9_9_REV=_C('GL_UNSIGNED_INT_5_9_9_9_REV',0x8C3E)
GL_UNSIGNED_INT_SAMPLER_1D=_C('GL_UNSIGNED_INT_SAMPLER_1D',0x8DD1)
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY=_C('GL_UNSIGNED_INT_SAMPLER_1D_ARRAY',0x8DD6)
GL_UNSIGNED_INT_SAMPLER_2D=_C('GL_UNSIGNED_INT_SAMPLER_2D',0x8DD2)
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY=_C('GL_UNSIGNED_INT_SAMPLER_2D_ARRAY',0x8DD7)
GL_UNSIGNED_INT_SAMPLER_3D=_C('GL_UNSIGNED_INT_SAMPLER_3D',0x8DD3)
GL_UNSIGNED_INT_SAMPLER_CUBE=_C('GL_UNSIGNED_INT_SAMPLER_CUBE',0x8DD4)
GL_UNSIGNED_INT_VEC2=_C('GL_UNSIGNED_INT_VEC2',0x8DC6)
GL_UNSIGNED_INT_VEC3=_C('GL_UNSIGNED_INT_VEC3',0x8DC7)
GL_UNSIGNED_INT_VEC4=_C('GL_UNSIGNED_INT_VEC4',0x8DC8)
GL_UNSIGNED_NORMALIZED=_C('GL_UNSIGNED_NORMALIZED',0x8C17)
GL_VERTEX_ARRAY_BINDING=_C('GL_VERTEX_ARRAY_BINDING',0x85B5)
GL_VERTEX_ATTRIB_ARRAY_INTEGER=_C('GL_VERTEX_ATTRIB_ARRAY_INTEGER',0x88FD)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glBeginConditionalRender(id,mode):pass
@_f
@_p.types(None,_cs.GLenum)
def glBeginTransformFeedback(primitiveMode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBindBufferBase(target,index,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glBindBufferRange(target,index,buffer,offset,size):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,arrays.GLcharArray)
def glBindFragDataLocation(program,color,name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindFramebuffer(target,framebuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindRenderbuffer(target,renderbuffer):pass
@_f
@_p.types(None,_cs.GLuint)
def glBindVertexArray(array):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLbitfield,_cs.GLenum)
def glBlitFramebuffer(srcX0,srcY0,srcX1,srcY1,dstX0,dstY0,dstX1,dstY1,mask,filter):pass
@_f
@_p.types(_cs.GLenum,_cs.GLenum)
def glCheckFramebufferStatus(target):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glClampColor(target,clamp):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLfloat,_cs.GLint)
def glClearBufferfi(buffer,drawbuffer,depth,stencil):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLfloatArray)
def glClearBufferfv(buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLintArray)
def glClearBufferiv(buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLuintArray)
def glClearBufferuiv(buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMaski(index,r,g,b,a):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteFramebuffers(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteRenderbuffers(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteVertexArrays(n,arrays):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDisablei(target,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEnablei(target,index):pass
@_f
@_p.types(None,)
def glEndConditionalRender():pass
@_f
@_p.types(None,)
def glEndTransformFeedback():pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr)
def glFlushMappedBufferRange(target,offset,length):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glFramebufferRenderbuffer(target,attachment,renderbuffertarget,renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTexture1D(target,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTexture2D(target,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTexture3D(target,attachment,textarget,texture,level,zoffset):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTextureLayer(target,attachment,texture,level,layer):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenFramebuffers(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenRenderbuffers(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenVertexArrays(n,arrays):pass
@_f
@_p.types(None,_cs.GLenum)
def glGenerateMipmap(target):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLbooleanArray)
def glGetBooleani_v(target,index,data):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetFragDataLocation(program,name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFramebufferAttachmentParameteriv(target,attachment,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glGetIntegeri_v(target,index,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetRenderbufferParameteriv(target,pname,params):pass
@_f
@_p.types(arrays.GLubyteArray,_cs.GLenum,_cs.GLuint)
def glGetStringi(name,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameterIiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glGetTexParameterIuiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLcharArray)
def glGetTransformFeedbackVarying(program,index,bufSize,length,size,type,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLuintArray)
def glGetUniformuiv(program,location,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexAttribIiv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetVertexAttribIuiv(index,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum,_cs.GLuint)
def glIsEnabledi(target,index):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsFramebuffer(framebuffer):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsRenderbuffer(renderbuffer):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsVertexArray(array):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr,_cs.GLbitfield)
def glMapBufferRange(target,offset,length,access):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorage(target,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageMultisample(target,samples,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameterIiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glTexParameterIuiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER( ctypes.POINTER( _cs.GLchar )),_cs.GLenum)
def glTransformFeedbackVaryings(program,count,varyings,bufferMode):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint)
def glUniform1ui(location,v0):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform1uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint)
def glUniform2ui(location,v0,v1):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform2uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniform3ui(location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform3uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniform4ui(location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform4uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint)
def glVertexAttribI1i(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI1iv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribI1ui(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI1uiv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint)
def glVertexAttribI2i(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI2iv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI2ui(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI2uiv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexAttribI3i(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI3iv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI3ui(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI3uiv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLbyteArray)
def glVertexAttribI4bv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexAttribI4i(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI4iv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttribI4sv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLubyteArray)
def glVertexAttribI4ubv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI4ui(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI4uiv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttribI4usv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribIPointer(index,size,type,stride,pointer):pass
