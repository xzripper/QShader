<h1 align="center">📦 QShaderV1-ALPHA. 💫</h1>
<p align="center">Powerful shading support for PyQt5. [<code>pip install qshader</code>].</p>
<p align="center"><img src="shaders.gif"></p>

```python
#thread QTimer 10

#pre_define hue 0

#import PyQt5.QtGui QColor

#begin_shader
Color1 = QColor.fromHsv(hue, 50, 200)
Color2 = QColor.fromHsv((hue + 30) % 360, 50, 220)
Color3 = QColor.fromHsv((hue + 60) % 360, 50, 240)

if @@UNDER_MOUSE:
    Gradient = f"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {Color1.name()}, stop:{@@MOUSE_POSITION_WIDGET.x() / $$parent.width()} {Color2.name()}, stop:1 {Color3.name()})"

else:
    Gradient = f"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {Color1.name()}, stop:0.5 {Color2.name()}, stop:1 {Color3.name()})"

$$style(f"background: {Gradient}; color: white; border: 0px solid; border-radius: 1px; font-size: 18px; padding: 15px;")

$$effect(BloomEffect, 100, QColor.fromRgb(Color1.red(), Color2.green(), Color3.blue(), @@RGB_MAX))

hue = (hue + 1) % 360
#end_shader
```

```python
#thread QTimer 10

#pre_define hue 0

#import PyQt5.QtGui QColor

#begin_shader
color = QColor.fromHsv(hue, @@RGB_MAX, @@RGB_MAX)

$$style(f'background-color: {color.name()}; color: black; border: 0px; font-size: 20px; padding: 30px;')

$$effect(BloomEffect, 250, color)

$$parent.setText(color.name())

hue = (hue + (2 if @@UNDER_MOUSE else 1)) % 360
#end_shader
```

<b>WARNING</b>: QShader is in ALPHA state, please be patient and report for all bugs.<br>

[QShader Documentation.](https://github.com/xzripper/QShader/blob/main/qshader.md)
[QTS Documentation.](https://github.com/xzripper/QShader/blob/main/qtsdocs.md)

<hr><p align="center"><b>QShader V1.0.0-ALPHA.</b></p>
