# QShader V1.0.0-ALPHA.
`QShader` class is used for working with shaders in PyQt.

### Methods
- `__init__(shader: str) -> None`: Initializes the shader.
- `compile_shader() -> bool`: Compiles the shader.
- `apply(widget: QWidget, parent: QWidget) -> bool`: Applies the shader to a widget.
- `compile_and_apply(widget: QWidget, parent: QWidget) -> bool`: Compiles the shader and applies it.
- `add_shader_input(name: str, value: Any) -> None`: Adds a shader input.
- `add_shader_builtin(name: str, value: Any) -> None`: Adds a shader builtin.
- `get_shader_error() -> str`: Retrieves the shader error.
- `shader_id() -> int`: Retrieves the shader ID.
- `get_shader_file() -> str`: Retrieves the shader file.
- `get_main_shader() -> str`: Retrieves the main shader.
- `get_shader() -> str`: Retrieves the shader.

## Constants
- `QSHADER_VERSION`: Version of the QShader module.
