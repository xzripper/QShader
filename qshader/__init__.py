"""Shaders for PyQt."""

from ._parser import parse_shader, Any

from ._utils import ParsedShader, NON_THREADED, THREAD_, QTIMER, PERFORMANCE_OPTIMIZATION

from ._shader_builtins import _S_C, _S_B

from ._effects import BloomEffect, BlurEffect, ShadowsEffect, ColorizeEffect, set_optimization

from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import QPoint, QTimer

from PyQt5.QtGui import QCursor

from random import randint, uniform

from threading import Thread

from importlib import import_module

from python_minifier import minify


QSHADER_VERSION: str = '1.0.0'

class QShader:
    """QShader class."""

    def __init__(self, shader: str) -> None:
        """Initialize shader."""
        self.shader_file = None

        if shader.endswith('.qts'):
            self.shader_file = shader

            with open(shader, 'r') as _shader:
                self.shader: str = _shader.read()

        else:
            self.shader: str = shader

        self.compiled_shader: ParsedShader = None

        self.main_shader: str = None

        self.inputs = {}

        self.id = randint(1, 9999)

        self.shader_builtins = {}

        self.__current_pre_defs = {}

        self._shader_globals = {}

    def compile_shader(self) -> bool:
        """Compile shader."""
        self.compiled_shader = parse_shader(self.shader)

        if self.compiled_shader.pre_defs:
            self.__current_pre_defs = self.compiled_shader.pre_defs

        if self.compiled_shader.shader_content:
            self.compiled_shader.shader_content.append('_SHADER._shader_globals = globals()')

        set_optimization(self.compiled_shader.optimization == PERFORMANCE_OPTIMIZATION)

        return not self.compiled_shader.failed

    def apply(self, widget: QWidget, parent: QWidget) -> bool:
        """Apply shader to a widget."""
        if not self.compiled_shader and not self.compiled_shader.failed:
            return False

        def run_shader():
            if self.compiled_shader.optimization == PERFORMANCE_OPTIMIZATION:
                if (widget.x() > parent.width() \
                    or (widget.x() + widget.width()) < 0) \
                        or (widget.y() > parent.height() \
                            or (widget.y() + widget.height()) < 0):
                    return

            for temp_widget in _S_B.temp_widgets:
                temp_widget.deleteLater()

            _S_B.temp_widgets = []

            class _S_P:
                parent = widget

                @staticmethod
                def effect(_effect, *args):
                    _effect.apply(widget, *args)

                @staticmethod
                def style(css):
                    widget.setStyleSheet(css)

            _S_C.MOUSE_POSITION = QCursor.pos()

            if _S_C.UNDER_MOUSE:
                _S_C.MOUSE_POSITION_WIDGET = widget.mapFromGlobal(_S_C.MOUSE_POSITION)

            else:
                _S_C.MOUSE_POSITION_WIDGET = QPoint(0, 0)

            _S_C.UNDER_MOUSE = widget.underMouse()

            _S_B.parent = parent

            shader = '\n'.join(self.compiled_shader.shader_content)

            shader = shader \
                .replace('@@', '_S_C.') \
                    .replace('%%', '_S_B.') \
                        .replace('$$', '_S_P.') \
                            .replace('_S_B.create+', '_S_B.create_nt') \
                                .replace('_S_B.rect+', '_S_B.rect_nt') \

            shader = minify(shader)

            _globals = {
                '_S_C': _S_C, '_S_B': _S_B, '_S_P': _S_P,

                'randint': randint, 'uniform': uniform,

                'BloomEffect': BloomEffect, 'BlurEffect': BlurEffect,
                'ShadowsEffect': ShadowsEffect, 'ColorizeEffect': ColorizeEffect,

                '_SHADER': self
            } | self.inputs | self.__current_pre_defs | self.shader_builtins

            imported = {}

            for _import in self.compiled_shader.imports:
                imported[_import[1]] = getattr(import_module(_import[0]), _import[1])

            _globals = _globals | imported

            self.main_shader = shader

            exec(shader, _globals, _globals)

            for pre_def_name in self.compiled_shader.pre_defs.keys():
                if pre_def_name in self._shader_globals:
                    self.__current_pre_defs[pre_def_name] = self._shader_globals[pre_def_name]

        if self.compiled_shader.thread == NON_THREADED:
            run_shader()

        elif self.compiled_shader.thread == THREAD_:
            Thread(target=run_shader).start()

        elif self.compiled_shader.thread == QTIMER:
            delay = self.compiled_shader.delay

            if self.compiled_shader.optimization == PERFORMANCE_OPTIMIZATION:
                delay += 10

            timer = QTimer(parent)

            timer.timeout.connect(run_shader)

            timer.start(delay)

        return True

    def compile_and_apply(self, widget: QWidget, parent: QWidget) -> bool:
        """Compile shader and apply."""
        return self.compile_shader() and self.apply(widget, parent)

    def add_shader_input(self, name: str, value: Any) -> None:
        """Add shader input."""
        self.inputs[name] = value

    def add_shader_builtin(self, name: str, value: Any) -> None:
        """Add shader builtin."""
        self.shader_builtins[name] = value

    def get_shader_error(self) -> str:
        """Get shader error."""
        if self.compiled_shader:
            return self.compiled_shader.error

    def shader_id(self) -> int:
        """Get shader ID."""
        return self.id

    def get_shader_file(self) -> str:
        """Get shader file."""
        return self.shader_file

    def get_main_shader(self) -> str:
        """Get main shader."""
        return self.main_shader

    def get_shader(self) -> str:
        """Get shader."""
        return self.shader
