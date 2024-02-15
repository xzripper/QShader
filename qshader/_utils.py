QUALITY_OPTIMIZATION = 'Quality'
PERFORMANCE_OPTIMIZATION = 'Performance'

NON_THREADED = 'NonThreaded'
THREAD_ = 'Thread'
QTIMER = 'QTimer'

DEFAULT_OPTIMIZATION = QUALITY_OPTIMIZATION
DEFAULT_THREAD = NON_THREADED

class ParsedShader:
    def __init__(self, shader_content: list=None, thread: str=DEFAULT_THREAD, delay: int=None, optimization: str=DEFAULT_OPTIMIZATION, inputs: list=None, imports: list=None, pre_defs: dict=None, error: str='') -> None:
        self.shader_content = shader_content

        self.thread = thread

        self.delay = delay

        self.optimization = optimization

        self.inputs = inputs

        self.imports = imports

        self.pre_defs = pre_defs

        self.error = error

    def __repr__(self) -> str:
        return f'Shader SZ:{len(self.shader_content)} Thread:{self.thread} Delay:{self.delay} Optimization:{self.optimization} Inputs:{self.inputs} Imports:{self.imports} PreDefs:{self.pre_defs} Failed:{self.failed}'

    @property
    def failed(self):
        return bool(self.error)
