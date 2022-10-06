# interpreter.nim
import std/tables
import strutils

type GenericTypeEnum = enum
  s, i, b

type Interpreter* = object
  ## The interpreter object contains all the code to feed, convert and run quik! code. Initialize with the ``initializeInterpreter`` func.
  vars*: Table[string, Table[string, GenericTypeEnum]]
method feed*(self: Interpreter, str: string): seq[string]{.base.} =
  var foods: seq[string] = str.split("\n")
  var i: int32 = 0;
  while i < foods.len:
    let food: string = foods[i]
    var strip: string = food.unindent().strip()
    foods[i] = strip
    if strip.isEmptyOrWhitespace():
      foods.del(i)
      i -= 1
    i += 1
  return foods

proc initInterpreter*(): Interpreter =
  Interpreter()
