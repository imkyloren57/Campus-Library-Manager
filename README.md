
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

The difference between LibraryItem.total_items and self.title lies in class scope versus instance scope. LibraryItem.total_items is a class attribute owned by the entire class blueprint, meaning only a single copy exists in memory and any change to it immediately affects all objects globally. In contrast, self.title is an instance attribute owned by a single specific object, meaning each new item gets its own independent copy and modifying it only alters that individual object without impacting others.