# 📦 Local Data Store (alpha-0.0.1 Edition)
This package is distributed by [Mochigoz](https://github.com/Mochigoz)\
Local Data Store is a Python librairy to save and manage `.json` files locally.\
Basically it can store, simple values such as `str`, `int`, `list` and `dict`

## Installation
The librairy is only available on GitHub.
```
pip git+https://github.com/Mochigoz/local_data_store.git
```

## Usage
```python
import local_data_store as lds

path = r"PATH\TO\A\FILE"

# Create a new .json file or rewrite it and save "Hello" in it
lds.write(path, "Hello")

# Read the file
print(lds.read(path))

# Append a data in the file
lds.append(path, "Bye")
print(lds.read(path))

# Delete the file
lds.remove(path)
```
```raw
>>> "Hello"
>>> ["Hello", "Bye"]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
