# 📚 Library Data
library = [
    {"sr": 201, "title": "Bitcoin & Crypto Guide", "available": True},
    {"sr": 202, "title": "Blockchain.dev Handbook", "available": False},
    {"sr": 203, "title": "Solidity for Smart Contracts", "available": True},
    {"sr": 204, "title": "NFTs Explained", "available": True},
    {"sr": 205, "title": "DeFi & Web3 Basics", "available": False},
]

borrowed_books = []  # to store borrowed book titles

# 🔍 Search + Borrow Function
def search_book(query):
    found = False
    for book in library:
        if str(book["sr"]) == str(query) or book["title"].lower() == query.lower():
            found = True
            status = "✅ Available" if book["available"] else "❌ Not Available"
            print(f"\n📘 Book Found:")
            print(f"   SR No: {book['sr']}")
            print(f"   Title: {book['title']}")
            print(f"   Status: {status}")
            
            # Borrow logic
            if book["available"]:
                book["available"] = False
                borrowed_books.append(book["title"])
                print("📦 Book has been borrowed. (Now marked Not Available)")
            else:
                print("❗This book is already borrowed (Not Available).")
            break
    if not found:
        print("\n⚠️ Book not found.")

# 🔁 Main Loop for Multiple Searches
while True:
    user_input = input("\n🔎 Enter Book Title or Serial Number (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("\n👋 Exiting... Thank you!")
        break
    search_book(user_input)

# 📋 Show Borrowed Book Summary
if borrowed_books:
    print("\n🧾 You borrowed the following books:")
    for i, book in enumerate(borrowed_books, 1):
        print(f"  {i}. {book}")
else:
    print("\n📭 You didn't borrow any books.")
