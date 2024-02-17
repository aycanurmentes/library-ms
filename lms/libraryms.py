import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.file_name = "books.txt"

        try:
            file = open(self.file_name, "r")
        except FileNotFoundError:
            file = open(self.file_name, "w")
        finally:
            file.close()

    def list_books(self):
        try:
            with open(self.file_name, "r") as file:
                books = file.read().splitlines()
                if not books:
                    messagebox.showinfo("Information", "No books found. Please add books.")
                else:
                    list_window = tk.Toplevel(self.main_window)
                    list_window.title("Book List")
                    list_window.configure(bg="lightblue") 

                    book_list = "\n".join(books)
                    list_label = tk.Label(list_window, text=book_list, bg="lightblue", padx=20, pady=20)
                    list_label.pack()

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

    def add_book(self, book_title, author, release_year, num_pages):
        with open(self.file_name, "a+") as file:
            file.write(f"{book_title}, {author}, {release_year}, {num_pages}\n")
        messagebox.showinfo("Information", "Book added successfully.")

    def remove_book(self, book_title):
        with open(self.file_name, "r") as file:
            books = file.readlines()

        with open(self.file_name, "w") as file:
            book_removed = False
            for book in books:
                if not book.startswith(book_title + ','):
                    file.write(book)
                else:
                    book_removed = True

        if book_removed:
            messagebox.showinfo("Information", "Book removed successfully.")
        else:
            messagebox.showinfo("Information", "The book you want to delete could not be found.")
    def on_closing(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.main_window.destroy()

    def on_key(self, event):
        if event.char == 'q':
            self.on_closing()

    def create_gui(self):
        self.main_window = tk.Tk()
        self.main_window.title("Library Management System")
        self.main_window.config(bg="pink") 
        self.main_window.bind('<Key>', self.on_key)


        self.label = tk.Label(self.main_window, text="Welcome to Library Management System", font=("Arial", 25))
        self.label.pack(pady=10)
        self.label.config(bg=self.main_window.cget('bg')) 

        self.list_button = tk.Button(self.main_window, text="List Books", command=self.list_books, highlightbackground="pink")
        self.list_button.pack(pady=5)

        self.add_button = tk.Button(self.main_window, text="Add Book", command=self.add_book_window, highlightbackground="pink")
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.main_window, text="Remove Book", command=self.remove_book_window, highlightbackground="pink")
        self.remove_button.pack(pady=5)

        self.labelq = tk.Label(self.main_window, text="Press 'q' to exit", font=("Arial", 15), )
        self.labelq.pack(pady=10)
        self.labelq.config(bg=self.main_window.cget('bg'))

        self.main_window.mainloop()

    def add_book_window(self):
        add_window = tk.Toplevel(self.main_window)
        add_window.title("Add Book")
        add_window.config(bg="pink") 

        tk.Label(add_window, text="Book Title:", bg=self.main_window.cget('bg')).pack()
        title_entry = tk.Entry(add_window, bg="white", fg="black")
        title_entry.pack()

        tk.Label(add_window, text="Author:", bg=self.main_window.cget('bg')).pack()
        author_entry = tk.Entry(add_window, bg="white", fg="black")
        author_entry.pack()

        tk.Label(add_window, text="Release Year:", bg=self.main_window.cget('bg')).pack()
        year_entry = tk.Entry(add_window, bg="white", fg="black")
        year_entry.pack()

        tk.Label(add_window, text="Number of Pages:", bg=self.main_window.cget('bg')).pack()
        pages_entry = tk.Entry(add_window, bg="white", fg="black")
        pages_entry.pack()

        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_book(title_entry.get(), author_entry.get(), year_entry.get(), pages_entry.get()),highlightbackground="pink" )
        add_button.pack()

    def remove_book_window(self):
        remove_window = tk.Toplevel(self.main_window)
        remove_window.title("Remove Book")
        remove_window.config(bg="pink")

        tk.Label(remove_window, text="Enter Book Title:", bg=self.main_window.cget('bg')).pack()
        title_entry = tk.Entry(remove_window, bg="white", fg="black")
        title_entry.pack()

        remove_button = tk.Button(remove_window, text="Remove", command=lambda: self.remove_book(title_entry.get()), highlightbackground="pink")
        remove_button.pack()

if __name__ == "__main__":
    lib = Library()
    lib.create_gui()
