# QShader Language. V1.1.0-ALPHA.
QShader (QTS) language is a mix of Python and new fancy syntax.

<h2>Keywords.</h2>

* `#begin_shader` - Marks main shader beggining.
* `#end_shader` - Marks main shader ending.
* `#input` - Require outer variable.
* `#import` - Import Python module.
* `#optimization` - Specify optimization level.
* `#pre_define` - Pre define variable.
* `#thread` - Specify shader threading.<br><br>

`#begin_shader` & `#end_shader` example:
```python
#begin_shader
# Your shader code here.
#end_shader
```
<br>

`#input` example:
```python
#input VARIABLE_NAME
```
<br>

`#import` example:
```python
#import MODULE ITEM
```
<br>

`#optimization` example:
```python
#optimization OPTIMIZATION
```
Optimization level can be `Quality` (default) or `Performance`.<br>

`#pre_define` example:
```python
#pre_define VARIABLE_NAME VARIABLE_VALUE
```
Variable value supports builtin types.<br>

`#thread` example:
```python
#thread THREAD ?DELAY
```
There are 3 threads:
* `NonThreaded` (executes shader one time in non threaded mode).
* `Thread` (executes shader one time in threaded mode).
* `QTimer` (executes shader infinitely with specified delay).
<br><BR>`DELAY` parameter is important if you're using `QTimer`.

<h2>Builtin functions.</h2>

* `%%create` - Create temporary Qt widget.
* `%%create+` - Create Qt widget.
* `%%rect` - Create temporary rectangle.
* `%%rect+` - Create rectangle.<br><br>

`%%create`/`%%create+` example:
```python
widget = %%create(WIDGET, *ARGS)

widget = %%create+(WIDGET, *ARGS)
```
Temporary widgets will be deleted instantly (will be deleted every QTimer.timeout if thread is `QTimer`).<br>

`%%rect`/`%%rect+` example:
```python
rect = %%rect((X, Y, WIDTH, HEIGHT), COLOR)

rect = %%rect+((X, Y, WIDTH, HEIGHT), COLOR)
```
Temporary rectangles will be deleted instantly (will be deleted every QTimer.timeout if thread is `QTimer`). `COLOR` argument is optional.<br>

<h2>Parent operations.</h2>

* `$$parent` - Shader parent (field).
* `$$effect` - Set parent effect.
* `$$style` - Set parent style (QStyleSheet).

`$$effect` example:
```python
$$effect(EFFECT, *ARGS)
```
Current supported effects: `BloomEffect`, `BlurEffect`, `ShadowsEffect`, `ColorizerEffect`.<br>

`$$style` example:
```python
$$style(STYLE)
```

<h2>Constants.</h2>

* `MOUSE_POSITION` = Calculated in runtime.
* `MOUSE_POSITION_WIDGET` = Calculated in runtime.

* `UNDER_MOUSE` = Calculated in runtime.

* `RGBA_MAX_LIST` = `[255, 255, 255, 255]`
* `RGBA_MIN_LIST` = `[0, 0, 0, 0]`

* `HUE_MAX` = `360`
* `HUE_MIN` = `0`

* `RGB_MAX` = `255`
* `RGB_MIN` = `0`

* `RGB_MIN_MAX` = `[0, 255]`

* `RGB_MAX_LIST` = `RGBA_MAX_LIST[:-1]`
* `RGB_MIN_LIST` = `RGBA_MIN_LIST[:-1]`

* `RGB_RANGE` = `range(*RGB_MIN_MAX)`

* `RGB_RANGE_REVERSED` = `reversed(RGB_RANGE)`

<h2>Random functions.</h2>

* `kill_shader_thread()` - Kill shader thread (QTimer).
* `printf(*values: object, sep: str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False)` - Alternative to `print`.
* `randint(X, Y)` - Random integer from x to y.
* `uniform(X, Y)` - Random float from x to y.

<h2>Overall example.</h2>

```python
#thread QTimer 10

#pre_define hue 0

#import PyQt5.QtGui QColor

#begin_shader
color = QColor.fromHsv(hue, @@RGB_MAX, @@RGB_MAX)

$$style(f'background-color: {color.name()}; color: black; border: 0px; font-size: 20px; padding: 30px;')

$$effect(BloomEffect, 250, color)

$$parent.setText(color.name())

hue = (hue + (2 if @@UNDER_MOUSE else 1)) % @@HUE_MAX
#end_shader
```
Rainbow glowing widget shader.<br>

<img src="shaders.gif">
<p align="center">⬆</p>
