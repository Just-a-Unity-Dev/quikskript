# cli.nim
import std/strformat
import parseopt, os

proc writeHelp() =
  echo """
  usage: <operation> [...]
  operations:
    -h | --help           : show's this message
    -v | --version        : show's the cli version
    -f | --file           : reads from a file and interpret's it
  """

proc writeVersion() =
  echo &"cli v0.0.1\n"

proc cli*() =
  if paramCount() == 0:
    writeHelp()
    quit(0)

  for kind, key, val in getopt():
    case kind
    of cmdLongOption, cmdShortOption:
      case key:
        of "help", "h":
          writeHelp()
          quit(0)
        of "version", "v":
          writeVersion()
          quit(0)
        of "file", "f":
          # TODO: Add functionality to the CLI when the interpreter works
          # Take the CL args, read the file, handle errors
          # Then feed into interpreter or something.
          echo "Not Finished"
          quit(1)
        else:
          discard
    else:
      discard

when isMainModule:
  cli()
