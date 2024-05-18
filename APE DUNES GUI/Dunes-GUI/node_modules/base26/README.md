```
# Base26

A simple library to perform basic +/- arithmatic on an alphabet-based number system.

a + 1 = b
b + 5 = g
z + 1 = aa
abc - 4 = aay

A practical usecase: spreadsheet column names.


---

## API

### base26.add(alpha: string, num: number): string

Increment alpha num times

add('a', 10) -> 'k'
add('aab', 10) -> 'aal'
add('x', 5), -> 'ac'
add('zc', 26), -> 'aac'



### base26.subtract(alpha: string, num: number): string

Decrement alpha num times.  Function throws if the result is not positive.

subtract('f', 5) -> 'a'
subtract('aag', 5) -> 'aab'
subtract('aag', 26) -> 'zg'
subtract('b', 2) -> throws



### base26.from(alpha: string): number

Convert number comprised of lowercase a-z alphabetical digits to the equivalent base10 number

from('a') -> 1
from('z') -> 26
from('aab') -> 704
from('A') -> throws
from('1') -> throws



### base26.to(decimal: number): string

Convert positive base10 number (> 0) to alphabetical digits

to(1) -> 'a'
to(26) -> 'z'
to(704) -> 'aab'
to(0) -> throws
to(-10) -> throws
```
