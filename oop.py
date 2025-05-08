from abc import ABC, abstractmethod

# Abstract class untuk semua item di perpustakaan
class LibraryItem(ABC):
    def __init__(self, item_id, title, year):
        self._item_id = item_id         # Protected attribute
        self._title = title             # Protected attribute
        self._year = year               # Protected attribute

    @abstractmethod
    def display_info(self):
        """Method abstract yang wajib diimplementasikan oleh subclass."""
        pass

    @property
    def title(self):
        """Menggunakan property untuk mengakses title dengan aman."""
        return self._title

    @property
    def item_id(self):
        """Property untuk mendapatkan ID item."""
        return self._item_id


# Subclass Book yang mewarisi dari LibraryItem
class Book(LibraryItem):
    def __init__(self, item_id, title, year, author):
        super().__init__(item_id, title, year)
        self.__author = author          # Private attribute (encapsulation)

    def display_info(self):
        """Implementasi method abstract display_info secara spesifik untuk buku."""
        print(f"[BOOK] ID: {self._item_id}, Title: {self._title}, Author: {self.__author}, Year: {self._year}")


# Subclass Magazine yang mewarisi dari LibraryItem
class Magazine(LibraryItem):
    def __init__(self, item_id, title, year, volume):
        super().__init__(item_id, title, year)
        self.__volume = volume          # Private attribute

    def display_info(self):
        """Implementasi method abstract display_info secara spesifik untuk majalah."""
        print(f"[MAGAZINE] ID: {self._item_id}, Title: {self._title}, Volume: {self.__volume}, Year: {self._year}")


# Kelas Library untuk mengelola koleksi item
class Library:
    def __init__(self):
        self.__items = []               # Private attribute untuk menyimpan koleksi

    def add_item(self, item):
        """Menambahkan item ke koleksi perpustakaan."""
        if isinstance(item, LibraryItem):
            self.__items.append(item)
            print(f"Item '{item.title}' berhasil ditambahkan.")
        else:
            print("Item tidak valid!")

    def show_all_items(self):
        """Menampilkan semua item yang tersedia."""
        print("\n--- Daftar Item Perpustakaan ---")
        for item in self.__items:
            item.display_info()  # Polymorphism: panggil method sesuai jenis item
        print("-------------------------------\n")

    def find_item_by_title(self, title):
        """Mencari item berdasarkan judul."""
        print(f"\nMencari item dengan judul: {title}")
        found = False
        for item in self.__items:
            if item.title.lower() == title.lower():
                item.display_info()
                found = True
        if not found:
            print("Item tidak ditemukan.")

    def find_item_by_id(self, item_id):
        """Mencari item berdasarkan ID."""
        print(f"\nMencari item dengan ID: {item_id}")
        found = False
        for item in self.__items:
            if item.item_id == item_id:
                item.display_info()
                found = True
        if not found:
            print("Item tidak ditemukan.")


# -------------------------
# Contoh penggunaan sistem
# -------------------------
if __name__ == "__main__":
    # Membuat perpustakaan
    library = Library()

    # Menambahkan item ke perpustakaan
    book1 = Book("B001", "Python Programming", 2021, "Guido van Rossum")
    magazine1 = Magazine("M001", "Tech Monthly", 2023, "Vol. 58")

    library.add_item(book1)
    library.add_item(magazine1)

    # Menampilkan semua item
    library.show_all_items()

    # Mencari berdasarkan judul
    library.find_item_by_title("Python Programming")

    # Mencari berdasarkan ID
    library.find_item_by_id("M001")
