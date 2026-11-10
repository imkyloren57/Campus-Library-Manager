
1. Why LibraryItem is Abstract & What Happens if DVD Forgets late_fee()

Abstract classes act as architectural blueprints to prevent invalid object creation. By defining LibraryItem as abstract, Python blocks developers from instantiating generic, incomplete items. 

Marking late_fee() with the @abstractmethod decorator enforces a strict contractual rule: any child class must implement its own version of that method. If a child class fails to do so, Python will immediately crash with a TypeError instead of allowing broken code to run.

2. Reading item.__available Outside the Class vs. is_available()

Attempting to access item.__available directly from outside the class results in a Python AttributeError due to name mangling, which enforces private encapsulation, whereas the is_available() method acts as a safe, read-only window that prevents outside classes from bypassing business rules to alter the value directly.

3. LibraryItem.total_items vs. self.title

The difference between LibraryItem.total_items and self.title lies in class scope versus instance scope. LibraryItem.total_items is a class attribute owned by the entire class blueprint, meaning only a single copy exists in memory and any change to it immediately affects all objects globally. In contrast, self.title is an instance attribute owned by a single specific object, meaning each new item gets its own independent copy and modifying it only alters that individual object without impacting others.