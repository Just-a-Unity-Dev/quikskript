# quikskript - 2022
# written by eclipsedotspace@gmail.com
# hosted under the MIT license
# written under 100 lines in Python
# https://github.com/Just-a-Unity-Dev/quikskript
# eclips-e.space

class Interpreter():
    def __init__(self):
        self.commands = {}
        self.funcs = {}
    
    def add_command(self, name, func):
        self.commands.__setitem__(name, func)

    def feed(self, rstring: str):
        strings = rstring.split("\n")
        for string in strings:
            strip = string.strip()
            if strip == "":
                strings.remove(string);
                continue
            strings.__setitem__(strings.index(string), strip)
        
        return strings
            
    
    def interpret(self, data, autofeed: bool = True):
        if autofeed:
            data = self.feed(data);
        
        header = None

        for line in data:
            if line.startswith("*"):
                # skip this, it's a comment
                continue
            elif line.startswith("/") and line.endswith("/"):
                # function header
                header = line[1:].lower()
                self.funcs.__setitem__(header, [])
            elif line == "done":
                # we're done with this header
                header = None
            elif line.split(" ")[0] in self.commands:
                args = line.split(" ")
                command = args.pop(0)

                # append command to header if there is one
                if header == "main/":
                    # if it's the main func then just run it
                    self.commands[command](args, self)
                elif header is not None:
                    # otherwise append it to funcs
                    self.funcs.__setitem__(
                        header,
                        self.funcs.__getitem__(header) +
                        [command,args]
                    )
                else:
                    raise Exception()
            else:
                # not a thing
                # raise Exception()
                pass

test = """
* ooooohh look at me so spooky comment
/setup/
    out test1 test2 test3
    done

*laugh
/main/
    call /setup/
    done
"""

itr = Interpreter()

def call_command(args, itr: Interpreter):
    func = itr.funcs[args[0][1:]]
    itr.commands[func[0]](func[1])

def out_command(args):
    print(' '.join(args))

itr.add_command("call", call_command)
itr.add_command("out", out_command)

itr.interpret(test)
