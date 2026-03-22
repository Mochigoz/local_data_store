# 📦 Local Data Store (alpha-0.0.5 Edition)
This package is distributed by [Mochigoz](https://github.com/Mochigoz)\
Local Data Store is a Python librairy to save and manage `.json` files locally.\
Basically it can store, simple values such as `str`, `int`, `list` and `dict`

## Installation and update
The librairy is only available on GitHub.
```
pip install git+https://github.com/Mochigoz/local_data_store.git
```
Some modifications will be made so if you want to have the latest version of the library, don't forget to update it!
```
pip install --upgrade git+https://github.com/Mochigoz/local_data_store.git
```

## Usage
```python
import local_data_store as lds

lds.edit_custom_path(r"MY_VARIABLE_PATH", r"ABSOLUTE\PATH\TO\A\FILE") # Set a variable saved in Local\local_data_store\paths.json
path = r"ABSOLUTE\PATH\TO\ANOTHER\FILE" # Function also works with a given string

# Create a new .json file or rewrite it and save "Hello" in it
lds.write("MY_VARIABLE_PATH", "Hello")
lds.write(path, "Bye!")

# Read the file
print("--- With variable:")
print(lds.read("MY_VARIABLE_PATH"))
print("--- With 'path':")
print(lds.read(path))
print(lds.read("Bye!"))

# Append a data in the file
lds.append("MY_VARIABLE_PATH", "Hey")
print("--- After appending value:")
print(lds.read("MY_VARIABLE_PATH"))

# Delete the file
lds.remove("MY_VARIABLE_PATH")
```
```raw
>>> --- With variable:
>>> "Hello"
>>> --- With 'path':
>>> Bye!
>>> None
>>> --- After appending value:
>>> ["Hello", "Hey"]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
