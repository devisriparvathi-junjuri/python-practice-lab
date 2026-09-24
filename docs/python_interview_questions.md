# Python Interview Questions

## Basics

**What is the difference between `==` and `is`?** `==` compares values; `is` checks object identity. Use `is None` for a `None` check.

**What is mutability?** A mutable object can change in place, such as a list. An immutable object, such as a string or tuple, must be replaced to represent a change.

## Data structures

**When would you use a set?** When uniqueness and fast membership checks matter, and ordering is not the primary requirement.

**How is a dictionary different from a list?** A list is an ordered sequence accessed by position; a dictionary maps unique keys to values.

## Functions

**What are `*args` and `**kwargs`?** They collect extra positional and keyword arguments, respectively. They are useful for flexible forwarding APIs.

**What is a closure?** A nested function that retains access to variables from its enclosing scope after the outer function returns.

## OOP

**What is composition?** Building an object from other objects, such as a library containing a collection of books. It often keeps responsibilities more focused than deep inheritance.

**What is polymorphism?** Different object types can provide the same operation, allowing calling code to depend on behavior rather than a concrete class.

## Exceptions and files

**Why use `with open(...)`?** A context manager closes the file even when an exception occurs.

**When should you create a custom exception?** When a domain-specific failure needs a clear name that callers can catch separately.

## Iterators and generators

**What is an iterator?** An object implementing `__iter__` and `__next__`, producing one item at a time.

**Why use a generator?** `yield` produces values lazily, reducing memory use for large or streaming inputs.

## Testing

**What makes a test useful?** It is deterministic, focused on one behavior, readable, and fails for a meaningful regression.

**Why test invalid input?** Validation and error paths are part of the public behavior, not optional details.
