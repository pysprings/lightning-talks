from robot.libraries.BuiltIn import BuiltIn


class TestLibrary:
    def test_equivalency_in_python(self, var1, var2) -> bool:
        BuiltIn().log(f"Checking if {var1} == {var1}", level="INFO")
        return var1 == var2

    def this_will_always_return_false(self) -> bool:
        BuiltIn().log("Writting log messages from Python", level="WARN")
        return False
