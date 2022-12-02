from typing import List

from pydantic import validator, root_validator

from lazy_model.main import LazyModel


class Simple(LazyModel):
    i: int
    s: str

    @validator("s")
    def s_upper(cls, v):
        return v.upper()

    @root_validator(pre=True)
    def check_card_number_omitted(cls, values):
        "i" in values
        return values


class Nested(LazyModel):
    s: Simple
    lst: List[Simple]


class Inherited(Simple):
    f: float
