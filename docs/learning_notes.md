# Learning Notes

## Indexes, keys, and values

A sequence uses integer indexes: `colors[0]` selects the first item. A dictionary uses keys: `marks["Asha"]` selects the value stored under the key `"Asha"`. The value is the data returned by either lookup. Keys must be hashable; values may be any object.

## Mutability

Lists, dictionaries, and sets can be changed after creation. Strings and tuples cannot be changed in place. A function that receives a mutable object can observe changes made to it, so copy data when independent state is needed.

## Exceptions

Use exceptions for unexpected conditions and handle them close to the boundary where you can respond meaningfully. Keep the protected `try` block small. Avoid a bare `except` because it hides programming errors.

## Complexity

Big-O describes how work grows with input size. A dictionary lookup is usually $O(1)$ average time; scanning a list is $O(n)$. Prefer the clearest correct solution first, then measure before optimizing.

## Testing mindset

A good test names one behavior, uses deterministic data, and checks both successful and invalid inputs. Tests are executable documentation and make refactoring safer.
