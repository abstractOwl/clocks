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


## See also

* [Lamport timestamps](https://en.wikipedia.org/wiki/Lamport_timestamps)
* [Vector clock](https://en.wikipedia.org/wiki/Vector_clock)
