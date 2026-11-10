
1. Why LibraryItem is Abstract & What Happens if DVD Forgets late_fee()

LibraryItem is abstract because it represents a conceptual template, not a real-world object. You cannot walk into a library and borrow a generic "item"; you borrow a specific Book, Magazine, or DVD. Making the class abstract protects your architecture by preventing anyone from accidentally creating a blank item using LibraryItem("Generic", 999).
If the DVD class forgets to write its own late_fee() method, Python will completely refuse to let you create a DVD object.
Because LibraryItem marks late_fee with the @abstractmethod decorator, Python enforces a strict contractual rule: any child class must provide a concrete implementation of that method. If you try to run dvd = DVD("Inception", 3, 148) without defining late_fee inside the DVD class, Python will immediately crash with a TypeError: Can't instantiate abstract class DVD with abstract method late_fee.

2. Reading item.__available Outside the Class vs. is_available()

If you try to read item.__available from outside the class, Python will throw an AttributeError claiming the property doesn't exist.
This happens because of a feature called Name Mangling. When you prefix an attribute with a double underscore (__), Python internally renames it to _ClassName__variableName (in this case, _LibraryItem__available) to intentionally hide it and prevent accidental modifications from external code.
We use the is_available() method instead for two major reasons:
• Encapsulation: It acts as a controlled "read-only" window. External classes (like Member) can check the status, but they cannot maliciously or accidentally force the value to change (e.g., writing item.__available = True directly bypasses the business rules).
• Future Flexibility: If you ever change how availability is calculated later (for example, checking if an item is reserved or lost instead of just a simple True/False flag), you only need to change the code inside the is_available() method. Every other class using it will continue to work perfectly without requiring a single rewrite.

3. LibraryItem.total_items vs. self.title

The fundamental difference comes down to Class Scope (Shared) vs. Instance Scope (Individual).

Metric	LibraryItem.total_items (Class Attribute)	self.title (Instance Attribute)
Ownership	Owned by the entire Class blueprint.	Owned by one specific object instance.
Copies	Only one single copy exists in computer memory.	Every new object created gets its own unique copy.
Behavior	If it changes, the change is instantly reflected across every single item globally.	If it changes, it only alters that exact specific item, leaving others untouched.


💡 The Analogy

Think of LibraryItem.total_items like a digital counter mounted on the library ceiling tracking how many total assets are in the building. Every time a new book, magazine, or DVD passes through registration, the counter clicks up by one.
On the other hand, self.title is like the sticker printed on the front cover of a single book. Changing the sticker on one book doesn't alter the text on any other book's cover, nor does it affect the digital counter on the ceiling.
Would you like to explore how property decorators (@property) can make is_available() look like a standard attribute while keeping its protection, or do you want to add a __str__ magic method to clean up how items look when printed?


 python3 -c "import dis, marshal; f=open('main.cpython-312.pyc', 'rb'); f.read(16); print(dis.dis(marshal.load(f)))"