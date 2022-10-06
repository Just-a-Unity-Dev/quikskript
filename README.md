# quikskript

Quikskript (quik! for short) is a small scripting language designed to be embedded in your applications.

## Sample Syntax

quik! is an assembly-like scripting language, this means most commands follow the basic architecture of:

```
<command> <args>
```

quik! uses functions (funcs) to run code, you define funcs by using a header (`/these/things/are/headers/`). An example hello world program would be:

```
* this is a comment, by the way
/main/
    out "hello world"
```

In order to call another function in quik! you have to use the `call` command. An example script would be:

```
/header/
    out "hello other world!"

/main/
    out "hello world!"
    call /header/
```

## License
MIT
