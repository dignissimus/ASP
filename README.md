# ASProject

A "simple" Stack-oriented programming language

### Prerequisites

ALl you need is a working version of python3

####Linux
```
sudo apt-get install python3
```

### Installing
First download the version wanted

####Downloading
```
wget https://raw.githubusercontent.com/spammy23/ASProject/master/ASP/<VERSION>/ASP.py
```

####Setting up
#####Linux
```
sudo chmod +x ./ASP.py
```
### Running
```
./ASP.py /path/to/code.asprj
```
To run the code in `code.asprj`
OR
Just
```
./ASP.py
```
For an interactive

## Programming
### Basics
ASProj is stack-oriented so the code `1` would add '1' to the stack and `1 2` would add '1' to the stack then add '2'.
If you want to print these values out then you would need to use either `P`, `p` or `/`. `P` prints the whole stack, then deletes it. `p` takes off the last added stack entry, then prints it, so `1 2 3p` will print '3'(then print '1' and '2' because ASProj prints the stack afterwards). `/` prints the whole stack, but leaves it as it is.
### Arithmatic
To add numbers you place them on the stack and use `A`, so `1 4A` takes off '1' and '4' from the stack and replaces it with 5.
To subtract numbers you do the same as addition but you would use `M`, and `1 4M` takes off the '1' and the '4' and replaces it with -1.
To divide is `D` and to multiply is `T` and to raise x to the power of y ia `^`.
### loops
For a while loop you would do `<Value>W<Code>]` which is while `<Value>` do `<code>`.
`1W1p]` will forever print '1'

For a For loop you would do `<Value><f/F><Code>]`.
which is for `$` in `<Value>` do `<code>`. If you use `f` it uses a 1 based index so `7f$]` will print '1' to '7'. And `7F$]` will print '0' to '6'.
### Other Functions
`C` checks if all numbers on the stack are prime.

`c` checks if the last number on the stack is prime.

`R` reverses the whole stack

`r` swaps the top two stack values

`\` is used to add the next character onto the stack `\a` adds 'a' to the stack

`X` adds '10' to the stack

`G` adds the literal alphabet to the stack

`{` AND `}` are used to define blocks which are defined 'functions' which sit on the stack.

`E` runs the string that was last place on the stack

`b` reverses the item on the top of the stack

`o` prints the stack without using newline. `O` does the same, but it also deletes the stack

`;` deletes the last item on the stack

`:` deletes the whole of the stack
