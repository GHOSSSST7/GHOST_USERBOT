from . import fonts
from . import memeshelper as jmthonmemes
from .aiohttp_helper import AioHttp
from .utils import *

flag = True
check = 0
while flag:
    try:
        from . import nsfw as useless
        from .chatbot import *
        from .functions import *
        from .memeifyhelpers import *
        from .progress import *
        from .qhelper import *
        from .tools import *
        from .utils import _format, _jmthonutils

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
