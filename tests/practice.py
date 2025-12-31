from toolsed import StringTools
from toolsed import Functions

# Init 
fc = Functions()
st = StringTools()

array = [1, 2, 3]
empty = []
string = "file"

print(fc.first(array))                  # return 1.
print(fc.first(empty, "Return answer")) # return Retrun answer

fc.is_iterable(array)   # True

print(st.pluralize(3, string))
