from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QGraphicsBlurEffect, QGraphicsColorizeEffect

from PyQt5.QtGui import QColor


optimize = False

def set_optimization(_optimize: bool) -> None:
    global optimize

    optimize = _optimize

class BloomEffect:
    @staticmethod
    def apply(widget: QWidget, power: int, color: QColor) -> None:
        bloom = QGraphicsDropShadowEffect()

        bloom.setBlurRadius((power / 2) if optimize else power)

        bloom.setOffset(0, 0)

        bloom.setColor(color)

        widget.setGraphicsEffect(bloom)

class BlurEffect:
    @staticmethod
    def apply(widget: QWidget, power: int) -> None:
        blur = QGraphicsBlurEffect()

        blur.setBlurRadius((power / 2) if optimize else power)

        widget.setGraphicsEffect(blur)

class ShadowsEffect:
    @staticmethod
    def apply(widget: QWidget, offset: tuple[int, int], blur: int, color=QColor(0, 0, 0, 255)) -> None:
        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius((blur / 2) if optimize else blur)

        shadow.setOffset(*offset)

        shadow.setColor(color)

        widget.setGraphicsEffect(shadow)

class ColorizeEffect:
    @staticmethod
    def apply(widget: QWidget, color: QColor) -> None:
        colorize = QGraphicsColorizeEffect()

        colorize.setColor(color)

        widget.setGraphicsEffect(colorize)
