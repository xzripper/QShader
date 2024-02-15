from PyQt5.QtWidgets import QWidget, QLabel


class _S_C:
    MOUSE_POSITION = None
    MOUSE_POSITION_WIDGET = None

    UNDER_MOUSE = None

    RGBA_MAX_LIST = [255, 255, 255, 255]
    RGBA_MIN_LIST = [0, 0, 0, 0]

    RGB_MAX = 255
    RGB_MIN = 0

    RGB_MIN_MAX = [0, 255]

    RGB_MAX_LIST = RGBA_MAX_LIST[:-1]
    RGB_MIN_LIST = RGBA_MIN_LIST[:-1]

    RGB_RANGE = range(*RGB_MIN_MAX)

    RGB_RANGE_REVERSED = reversed(RGB_RANGE)

class _S_B:
    parent = None

    temp_widgets = []

    def create(widget: QWidget, *args) -> QWidget:
        _widget = widget(*args, parent=_S_B.parent)

        _widget.show()

        _S_B.temp_widgets.append(_widget)

        return _widget

    def create_nt(widget: QWidget, *args) -> None:
        _widget = widget(*args, parent=_S_B.parent)

        _widget.show()

        return _widget

    def rect(geometry: tuple, bg='black') -> None:
        _rect = QLabel(_S_B.parent)

        _rect.setStyleSheet(f'background-color: {bg};')

        _rect.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])

        _rect.show()

        _S_B.temp_widgets.append(_rect)

        return _rect

    def rect_nt(geometry: tuple, bg='black') -> None:
        _rect = QLabel(_S_B.parent)

        _rect.setStyleSheet(f'background-color: {bg};')

        _rect.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])

        _rect.show()

        return _rect
