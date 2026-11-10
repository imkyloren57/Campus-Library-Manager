from models import DVD, Book, Magazine, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Sports Illustrated", 2, "March 2024")
dvd = DVD("There Will Be Blood", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: exceeds max_items
except ValueError as e:
    print("Could not borrow:", e)


try:
    bob.return_item(dvd)  # should fail: not borrowed yet
except ValueError as e:
    print("Could not return:", e)


# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)
