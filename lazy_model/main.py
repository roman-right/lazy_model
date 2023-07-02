import pydantic
from lazy_model.nao import NAO

# check pydantic version
if pydantic.version.VERSION.split(".")[0] == 1:
    from lazy_model.parser.old import LazyModel
else:
    from lazy_model.parser.new import LazyModel
