# quikskript - 2022
# written by eclipsedotspace@gmail.com
# hosted under the MIT license
# eclips-e.space | https://github.com/Just-a-Unity-Dev/quikskript

class Interpreter():
    def __init__(self):
        self.commands = {}
        self.funcs = {}
        self.vars = {}
    
    def add_command(self, name, func):
        self.commands.__setitem__(name, func)

    def set_var(self, name, val, vtype):
        if vtype == "s":
            self.vars.__setitem__(name, val)
        elif vtype == "i":
            self.vars.__setitem__(name, int(val))
        elif vtype == "f":
            self.vars.__setitem__(name, float(val))
        elif vtype == "b":
            self.vars.__setitem__(name, val == 'true')
    
    def get_var(self, name):
        try:
            return self.vars.__getitem__(name)
        except KeyError:
            return None
    
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
                raise Exception()

test = """
* quik is an assembly/sql-like language, following a (command) (arg) syntax
* this is a comment lol
* these are global variables, always declared at a top of a file
* global i 0

* below is a function declared by starting and ending an identifier with /
/func/
    * order of functions is important
    * you cant access a func declared below you
    set i i 0
    out *i
    call /func/ > i 10
    done

/main/
    * the main function is recommended to be put last of all other funcs so that /main/ has full access to all other funcs
    call /func/ ?
    out the function FINALLY finished
    out hello world!
"""

interpreter = Interpreter()

def call_command(args, itr: Interpreter):
    func = itr.funcs[args[0][1:]]
    params = args[1]
    
    evaluated = False
    inverted = False
    var = None
    cmp = None
    if not params == "?":
        var = itr.get_var(args[2])
        cmp = args[3]
        if args[3].startswith("*"):
            cmp = itr.get_var(args[3][1:])
    else:
        evaluated = True

    if params == "!":
        # inverse
        inverted = not inverted
    elif params == ">":
        print(var, cmp, var > cmp)
        if var > cmp:
            evaluated = True
    elif params == "<":
        if var < cmp:
            evaluated = True
    elif params == "=":
        if var == cmp:
            evaluated = True

    if inverted:
        evaluated = not evaluated

    if evaluated:
        for command in func:
            itr.commands[func[0]](func[1], itr)
            del func[:2]

def out_command(args, ir: Interpreter):
    if args[0].startswith("*"):
        print(ir.get_var(args[0][1:]))
    else:
        print(' '.join(args))

def set_command(args, ir: Interpreter):
    var_name = args.pop(0)
    var_type = args.pop(0)
    ir.set_var(var_name, ' '.join(args), var_type)

interpreter.add_command("call", call_command)
interpreter.add_command("out", out_command)
interpreter.add_command("set", set_command)

interpreter.interpret(test)
