# C++ Syntactic Peculiarities
After using a fairly large, matured language for a reasonable period of time, find peculiarities in the language or the libraries is guaranteed to happen. However, given it’s history, I have to say C++ definitely allows for some of the strangest peculiarities in it’s syntax. Below I list three that are my favorite.

## Ternaries Returning lvalues
You might be familiar with ternaries as `condition ? do something : do something else`, and they become quite useful in comparison to the standard if-else. However, if you’ve dealt with ternaries a lot, you might have noticed that ternaries also return [lvalues/rvalues](http://stackoverflow.com/questions/3601602/what-are-rvalues-lvalues-xvalues-glvalues-and-prvalues). Now, as the name suggests suggests, you can assign to lvalues (lvalues are often referred to as locator values). So something like so is possible:

```
std::string x = "foo", y = "bar";

std::cout << "Before Ternary! ";
// prints x: foo, y: bar
std::cout << "x: " << x << ", y: " << y << "\n"; 

// Use the lvalue from ternary for assignment
(1 == 1 ? x : y) = "I changed";
(1 != 1 ? x : y) = "I also changed";

std::cout << "After Ternary! ";
// prints x: I changed, y: I also changed
std::cout << "x: " << x << ", y: " << y << "\n"; 
```

Although it makes sense, it’s really daunting; I can attest to never seeing it in the wild.

## Commutative Bracket Operator
An interesting fact about C++ bracket operator, it’s simply pointer arithmetic. Writing `array[42]()` is actually the same as writing `*(array + 42)`, and thinking in terms of x86/64 assembly, this makes sense! It’s simply an indexed addressing mode, a base (the beginning location of array) followed by an offset (42). If this doesn’t make sense, that’s okay. We will discuss the implications without any need for assembly programming.

So we can do something like `*(array + 42)`, which is interesting; but we can do better. We know addition to be commutative, so wouldn’t saying `*(42 + array)` be the same? Indeed it is, and by transitivity, `array[42]()` is exactly the same as `42[array]()`. The following is a more concrete example.

```cpp
std::string array[50];
42[array] = "answer";

// prints 42 is the answer
std::cout << "42 is the " << array[42] << ".";
```

## Zero Width Space Identifiers
This one has the least to say, and could cause the most damage. The C++ standard allows for [hidden white space](https://en.wikipedia.org/wiki/Whitespace\_character) in identifiers (i.e. variable names, method/property names, class names, etc.). So this makes the following possible.

```
int n​umber = 1;
int nu​mber = 2;
int num​ber = 3;

std::cout << n​umber << std::endl; // prints 1
std::cout << nu​mber << std::endl; // prints 2
std::cout << num​ber << std::endl; // prints 3
```

Using `\u` as a proxy for hidden whitespace character, the above code can be re-written as such:

```
int n\uumber = 1;
int nu\umber = 2;
int num\uber = 3;

std::cout << n\uumber << std::endl; // prints 1
std::cout << nu\umber << std::endl; // prints 2
std::cout << num\uber << std::endl; // prints 3
```

So if you’re feeling like watching the world burn, this would be the way to go.
