# Cefpython3 Wrapper
cef_wrapper.py allows autocompleting & methods highlighting for the cefpython3 library.

---

The goal of the `cef_wrapper.py` file is to implement docstrings & auto-completing
for the cefpython3 project.

- `cef` defines the main class that contains multiple other classes.
- In the case of objects, they can be used as type hints, which allows syntax highlighting.
- Don't forget the Zen Of Python, don't use `*` as it would import cefpython3 & some types.

You can find the classes / objects list from cefpython3 here:\
https://github.com/cztomczak/cefpython#classes-and-objects

---
Here's a list of the implemented / supported classes/objects:

| Fully implemented     | Not yet implemented 	|
|---------------------	|---------------------	|
| `cef` python module 	| TextInputContext    	|
| JavascriptBindings    | Frame Object          |
| PaintElementType    	|       	            |
| WindowInfo Class    	|                     	|
| DragData Object     	|                     	|
| cef_alpha_type_t    	|                     	|
| cef_color_type_t    	|                     	|
| Browser Object      	|                     	|
| cef_state_t         	|                     	|
| Image               	|                     	|
