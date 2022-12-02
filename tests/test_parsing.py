from lazy_model.main import NAO
from tests.models import Simple, Nested, Inherited


class TestParsing:
    def test_simple_parse(self):
        obj = Simple.lazy_parse({"i": "10", "s": "test"})
        assert obj.__dict__["i"] == NAO
        assert obj.__dict__["s"] == NAO
        assert obj.i == 10
        assert obj.s == "TEST"

    def test_simple_parse_with_fields(self):
        obj = Simple.lazy_parse({"i": "10", "s": "test"}, fields={"s"})
        assert obj.__dict__["i"] == NAO
        assert obj.__dict__["s"] == "TEST"
        assert obj.i == 10
        assert obj.s == "TEST"

    def test_simple_parse_store(self):
        obj = Simple.lazy_parse({"i": "10", "s": "test"})
        obj.parse_store()
        assert obj.__dict__ == {"i": 10, "s": "TEST"}

    def test_nested_parse(self):
        obj = Nested.lazy_parse(
            {
                "s": {"i": "10", "s": "test"},
                "l": [{"i": "10", "s": "test"}, {"i": "10", "s": "test"}],
            }
        )
        assert obj.__dict__ == {"s": NAO, "l": NAO}
        assert obj.s == Simple(i=10, s="TEST")
        assert obj.lst == [Simple(i=10, s="TEST"), Simple(i=10, s="TEST")]

    def test_inheritance(self):
        obj = Inherited.lazy_parse({"i": "10", "s": "test", "f": 1.23})
        assert obj.__dict__ == {"i": NAO, "s": NAO, "f": NAO}
        assert obj.i == 10
        obj.parse_store()
        assert obj.__dict__ == {"f": 1.23, "i": 10, "s": "TEST"}
