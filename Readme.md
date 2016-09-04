# clocks
Simulates various clock algorithms. Currently supports Lamport timestamps and 
vector clocks.


## Usage:

        python clocks.py [lamport|vector]


## Commands

| Commands          | Description                                             |
|-------------------|---------------------------------------------------------|
| `add [<a> ...]`   | Adds node(s)                                            |
| `list`            | Lists nodes                                             |
| `send <a> <b>`    | Sends a message from a to b                             |
| `?`               | Prints a help message                                   |
| `quit`            |  Exits the simulator                                    |


## Example

```
$ python clocks.py vector
[?] Enter command (add/list/send/quit/?): add a b c

[*] Added node a
[*] Added node b
[*] Added node c

[?] Enter command (add/list/send/quit/?): send c b

[*] Node c: Sending clock message <{'c': 1}>
[*] Node b: Receiving clock message <{'b': 0}> -> <{'c': 1, 'b': 1}>

[?] Enter command (add/list/send/quit/?): send b a

[*] Node b: Sending clock message <{'c': 1, 'b': 2}>
[*] Node a: Receiving clock message <{'a': 0}> -> <{'a': 1, 'c': 1, 'b': 2}>

[?] Enter command (add/list/send/quit/?): send b c

[*] Node b: Sending clock message <{'c': 1, 'b': 3}>
[*] Node c: Receiving clock message <{'c': 1}> -> <{'c': 2, 'b': 3}>

[?] Enter command (add/list/send/quit/?): send a b

[*] Node a: Sending clock message <{'a': 2, 'c': 1, 'b': 2}>
[*] Node b: Receiving clock message <{'c': 1, 'b': 3}> -> <{'a': 2, 'c': 1, 'b': 4}>

[?] Enter command (add/list/send/quit/?): send c a

[*] Node c: Sending clock message <{'c': 3, 'b': 3}>
[*] Node a: Receiving clock message <{'a': 2, 'c': 1, 'b': 2}> -> <{'a': 3, 'c': 3, 'b': 3}>

[?] Enter command (add/list/send/quit/?): send b c

[*] Node b: Sending clock message <{'a': 2, 'c': 1, 'b': 5}>
[*] Node c: Receiving clock message <{'c': 3, 'b': 3}> -> <{'a': 2, 'c': 4, 'b': 5}>

[?] Enter command (add/list/send/quit/?): send c a

[*] Node c: Sending clock message <{'a': 2, 'c': 5, 'b': 5}>
[*] Node a: Receiving clock message <{'a': 3, 'c': 3, 'b': 3}> -> <{'a': 4, 'c': 5, 'b': 5}>

[?] Enter command (add/list/send/quit/?): list

[*] Listing 3 nodes...
[*] Node a <{'a': 4, 'c': 5, 'b': 5}>
[*] Node c <{'a': 2, 'c': 5, 'b': 5}>
[*] Node b <{'a': 2, 'c': 1, 'b': 5}>

[?] Enter command (add/list/send/quit/?): quit
```


## See also

* [Lamport timestamps](https://en.wikipedia.org/wiki/Lamport_timestamps)
* [Vector clock](https://en.wikipedia.org/wiki/Vector_clock)
