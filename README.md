# Lazy parsing for Pydantic models

This library provides a lazy interface for parsing objects from dictionaries. During the parsing, it saves the raw data inside the object and parses each field on demand.

## Install

poetry
```shell
poetry add lazy-model
```

pip
```shell
pip install lazy-model
```

## Usage

```python
from lazy_model import LazyModel
from pydantic import validator


class Sample(LazyModel):
    i: int
    s: str

    @validator("s")
    def s_upper(cls, v):
        return v.upper()


obj = Sample.lazy_parse({"i": "10", "s": "test"})

# at this point the data is stored in a raw format inside the object

print(obj.__dict__)

# >>> {'i': NAO, 's': NAO}

# NAO - Not An Object. It shows that the field was not parsed yet.

print(obj.s)

# >>> TEST

# Custom validator works during lazy parsing

print(obj.__dict__)

# >>> {'i': NAO, 's': 'TEST'}

# The `s` field  was already parsed by this step

print(obj.i, type(obj.i))

# >>> 10 <class 'int'>

# It converted `10` from string to int based on the annotations

print(obj.__dict__)

# >>> {'i': 10, 's': 'TEST'}

# Everything was parsed
```