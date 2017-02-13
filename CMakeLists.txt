Project(PyCEGUI)

set( CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake ${PROJECT_SOURCE_DIR}/cegui/cmake ${CMAKE_MODULE_PATH})

include(CEGUIMacros)

find_package(PythonInterp)

## ensure python3 not picked up as default
find_package(PythonVersion)
if (UNIX AND PYTHON_VERSION_FOUND)
  find_package(PythonLibs ${PYTHON_VERSION_STRING} EXACT)
else()
  find_package(PythonLibs)
endif()
find_package(Boost 1.36.0 COMPONENTS python)

find_package(CEGUI REQUIRED)
if ("${CEGUI_VERSION}" VERSION_GREATER "0.8.0")
    set(CEGUI_LIB_SUFFIX "-${CEGUI_VERSION_MAJOR}")
endif ()

execute_process(
    COMMAND ${PYTHON_EXECUTABLE} -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_lib(plat_specific=True, prefix=\"\"))"
    OUTPUT_VARIABLE CEGUI_PYTHON_INSTALL_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

set( CEGUI_PYTHON_INSTALL_DIR "${CEGUI_PYTHON_INSTALL_DIR}/${CMAKE_PROJECT_NAME}-${CEGUI_VERSION_MAJOR}.${CEGUI_VERSION_MINOR}" )

include_directories(${CMAKE_CURRENT_SOURCE_DIR}
                    ${PYTHON_INCLUDE_DIR}
                    ${Boost_INCLUDE_DIR})

cegui_set_library_name( CEGUI_NULL_RENDERER_LIBNAME CEGUINullRenderer )
cegui_set_library_name( CEGUI_OPENGL_RENDERER_LIBNAME CEGUIOpenGLRenderer )
cegui_set_library_name( CEGUI_OGRE_RENDERER_LIBNAME CEGUIOgreRenderer)
set( CEGUI_BASE_LIBNAME "${CEGUI_LIBRARIES}" )
set( CEGUI_PYCEGUI_CORE_LIBNAME PyCEGUI )
set( CEGUI_PYCEGUI_OPENGL_RENDERER_LIBNAME PyCEGUIOpenGLRenderer )
set( CEGUI_PYCEGUI_OGRE_RENDERER_LIBNAME PyCEGUIOgreRenderer )
set( CEGUI_PYCEGUI_NULL_RENDERER_LIBNAME PyCEGUINullRenderer )

include_directories(${CEGUI_INCLUDE_DIR})
include_directories("cegui/cegui/src/ScriptModules/Python/bindings/")

set(CEGUI_PYTHON_INSTALL_DIR ${CMAKE_INSTALL_PREFIX})

cegui_add_python_module( ${CEGUI_PYCEGUI_CORE_LIBNAME} "cegui/cegui/src/ScriptModules/Python/bindings/output/CEGUI" "")

if (CEGUI_BUILD_RENDERER_NULL)
    cegui_add_python_module( ${CEGUI_PYCEGUI_NULL_RENDERER_LIBNAME} "cegui/cegui/src/ScriptModules/Python/bindings/output/CEGUINullRenderer" "")
    target_link_libraries(${CEGUI_PYCEGUI_OPENGL_RENDERER_LIBNAME} ${CEGUI_NULL_RENDERER_LIBRARIES})
endif()

if (CEGUI_BUILD_RENDERER_OGRE)
    cegui_add_python_module( ${CEGUI_PYCEGUI_OGRE_RENDERER_LIBNAME} "cegui/cegui/src/ScriptModules/Python/bindings/output/CEGUIOgreRenderer" "")
    target_link_libraries(${CEGUI_PYCEGUI_OPENGL_RENDERER_LIBNAME} ${CEGUI_OGRE_RENDERER_LIBRARIES})
endif()

if (CEGUI_BUILD_RENDERER_OPENGL)
    find_package(GLEW)
    include_directories(${GLEW_INCLUDE_DIR})
    find_package(OpenGL)
    include_directories(${OPENGL_INCLUDE_DIR})
    find_package(GLFW)
    include_directories(${GLFW_INCLUDE_DIR})
    find_package(GLFW3)
    include_directories(${GLFW3_INCLUDE_DIR})
    find_package(GLFW3)
    include_directories(${GLFW3_INCLUDE_DIR})
    find_package(GLFW3)
    include_directories(${GLM_INCLUDE_DIR})
    cegui_add_python_module( ${CEGUI_PYCEGUI_OPENGL_RENDERER_LIBNAME} "cegui/cegui/src/ScriptModules/Python/bindings/output/CEGUIOpenGLRenderer" "")
    target_link_libraries(${CEGUI_PYCEGUI_OPENGL_RENDERER_LIBNAME} ${CEGUI_OpenGLRenderer_LIBRARIES})
endif()

