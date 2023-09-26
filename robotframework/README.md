# Robotframework Introduction

[Robot Framework](https://robotframework.org/) is a widely used testing library with many features.

RF really excels and creating test suites and test cases.  It's a fairly simple
process to define many different testing scenarios.  This would be difficult if
you created a long "test suite" inside a single script.

The basic features can be broken down to `keyword`s and `libraries`.

## Keywords

Think of `keyword`s as _functions_.  They are defined by a unique name, they might take arguments, and they might return something.

You make a Test Case out of Keywords, which can be provided through [Robot Framework](https://robotframework.org/robotframework/#standard-libraries) or your custom code.

No matter where you define your keyword, RF will always refer to them as capitalized, space-separated, things.

For example, let say you defined a Keyword in Python like this:
```python
def log_in_to_the_website(): ...
```

You refer to that "keyword" in RF code as:
```
Log In To The Website
```

## Libraries

Think of `libraries` as a collection of keywords.


## Takeaways

I only have a few weeks of experience with Robot Framework, so take this with much scepticism.

* Pros:
    - Been around for a while (lots of useful info online)
    - Very generic
    - "Easy" to write suites/cases (once you get used to the format)
    - Too many examples use "single file" setups (e.g. having test cases/suites, library, etc, all defined in an RST file)
    - Extensive documentation
    - You can inline basic Python code

* Cons:
    - Language is not very Pythonic
    - Even the Python API isn't very Pythonic
    - Very generic
    - I find the syntax awkward
    - Difficult to apply documentation to real world example
    - Awkward use of strings "everwhere, except there"
