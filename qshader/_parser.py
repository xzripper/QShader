from ._utils import *

from typing import Any


BEGIN_SHADER = '#begin_shader'
END_SHADER = '#end_shader'

INPUT = '#input'

IMPORT = '#import'

OPTIMIZATION = '#optimization'

PRE_DEFINE = '#pre_define'

THREAD = '#thread'

def del_empty_lines(lines: list) -> list:
    return [line for line in lines if line]

def missing_parts(line: str, parts_required: int=2) -> bool:
    return len(line.split()) < parts_required

def cast(element: str) -> Any:
    if element.isdigit():
        return int(element)

    elif element == 'true':
        element = element == 'true'

    elif element == 'null':
        return None

    else:
        try:
            return float(element)
        except ValueError:
            return element

def parse_shader(source: str) -> ParsedShader:
    _shader_content_start_pos = 0

    shader_content = None

    thread = None

    delay = None

    optimization = None

    inputs = []

    imports = []

    pre_defs = {}

    for pos, line in enumerate(source.split('\n')):
        if line.startswith(BEGIN_SHADER):
            _shader_content_start_pos = pos + 1

        elif line.startswith(END_SHADER):
            shader_content = del_empty_lines(source.split('\n')[_shader_content_start_pos:pos])

        elif line.startswith(INPUT):
            if missing_parts(line):
                return ParsedShader(error=f'Missing input name. [L:{pos + 1}].')

            inputs.append(line.split()[1])

        elif line.startswith(IMPORT):
            if missing_parts(line, 3):
                return ParsedShader(error=f'Missing module/item to import. [L:{pos + 1}].')

            _import = line.split()

            imports.append((_import[1], _import[2]))

        elif line.startswith(OPTIMIZATION):
            if missing_parts(line):
                return ParsedShader(error=f'Missing optimization type. [L:{pos + 1}].')

            _optimization = line.split()[1]

            if _optimization not in [QUALITY_OPTIMIZATION, PERFORMANCE_OPTIMIZATION]:
                return ParsedShader(error=f'Invalid optimization type: `{_optimization}`; Possible optimizations: Quality, Performance. [L:{pos + 1}].')

            optimization = _optimization

        elif line.startswith(PRE_DEFINE):
            if missing_parts(line, 3):
                return ParsedShader(error=f'Missing pre definition name/value. [L:{pos + 1}].')

            pre_def = line.split()

            pre_defs[pre_def[1]] = cast(pre_def[2])

        elif line.startswith(THREAD):
            if missing_parts(line, 2):
                return ParsedShader(error=f'Missing thread. [L:{pos + 1}].')

            _thread = line.split()

            if _thread[1] not in [NON_THREADED, THREAD_, QTIMER]:
                return ParsedShader(error=f'Invalid thread type: `{_thread[1]}`; Possible threads: NonThreaded, Thread, QTimer. [L:{pos + 1}].')

            else:
                thread = _thread[1]

            if thread == QTIMER:
                if len(_thread) < 3:
                    return ParsedShader(error=f'Missing QTimer delay. [L:{pos + 1}].')

                _delay = cast(_thread[2])

                if not isinstance(_delay, int) and not isinstance(_delay, float):
                    return ParsedShader(error=f'Delay should be int/float. [L:{pos + 1}].')

                else:
                    delay = _delay

    return ParsedShader(shader_content, thread, delay, optimization, inputs, imports, pre_defs)
