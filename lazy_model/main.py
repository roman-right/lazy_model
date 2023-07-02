import pydantic

# check pydantic version
if pydantic.version.VERSION.split(".")[0] == 1:
    from lazy_model.parser.old import LazyModel  # noqa: F401
else:
    from lazy_model.parser.new import LazyModel  # noqa: F401
