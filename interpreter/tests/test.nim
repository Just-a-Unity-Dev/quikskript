import unittest
import Quikskript/interpreter

## This test tests if ``Interpreter.feed()`` is working.
test "feed test":
  var itr: Interpreter = initInterpreter()
  
  # probably cant see it but this string is full of yucky whitespace
  let test_string: string = """
    Hello world!
    The itr.feed() method converts a string full of
        whitespace and cleans it up by     

stripping the string and checking if it's pure empty.   
  """

  var feed: seq[string] = itr.feed(test_string)

  check feed == @[
    "Hello world!",
    "The itr.feed() method converts a string full of",
    "whitespace and cleans it up by",
    "stripping the string and checking if it\'s pure empty."
  ]
