# 19.Using Databases With TKinter - Python Tkinter GUI Tutorial #19

from tkinter import *
from PIL import  ImageTk, Image
import sqlite3
root = Tk()
root.title("Using Databases")
root.iconbitmap("stark-wolf.ico")
root.geometry("400x500")

# Databases
# Create a database or connect to onne
conn = sqlite3.connect('address_book.db')
# creating cursor to send command
cursor = conn.cursor()
# Commit Changes
conn.commit()
'''
#Creating a table
cursor.execute("""CREATE TABLE addresses(
first_name text,
last_name text,
address text,
city text,
state text,
zipcode integer
)
""")
'''


# Create edit function to update a record
def edit():
    editor = Tk()
    editor.title("Update a Record")
    editor.iconbitmap("stark-wolf.ico")
    editor.geometry("400x200")

    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create cursor
    cursor = conn.cursor()

    record_id = delete_box.get()
    # query the databse
    cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cursor.fetchall()

    # create update function to update a record
    def update():
        conn = sqlite3.connect("address_book.db")
        cursor = conn.cursor()
        record_id = delete_box.get()
        cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
                       {
                        'first': f_name_editor.get(),
                        'last': l_name_editor.get(),
                        'address': address_editor.get(),
                        'city': city_editor.get(),
                        'state': state_editor.get(),
                        'zipcode': zipcode_editor.get(),

                        'oid': record_id
                       })
        conn.commit()
        conn.close()
        editor.destroy()
    #  # create global variable for text box names
    # global f_name_editor
    # global l_name_editor
    # global address_editor
    # global city_editor
    # global state_editor
    # global zipcode_editor
    # # create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    # Create a save button to save edited record
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=11, columnspan=2, column=0, padx=10, pady=10, ipadx=130)

# Create function to delete a record
def delete():
    # Create a database or connect to onne
    conn = sqlite3.connect('address_book.db')
    # creating cursor to send command
    cursor = conn.cursor()

    # Delete a Record
    cursor.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# Create Submit function for database
def submit():
    # Create a database or connect to onne
    conn = sqlite3.connect('address_book.db')
    # creating cursor to send command
    cursor = conn.cursor()

    # Insert into Table
    cursor.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
                   {'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                    })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function
def query():
    # Create a database or connect to onne
    conn = sqlite3.connect('address_book.db')
    # creating cursor to send command
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    # print(records)

    # Loop through results
    print_rec = ""
    for i in records:
        print_rec += str(i[-1]) + "\t" + str(i[0]) + " " + str(i[1]) + "; " + str(i[2]) + "; " + str(i[3]) + "; " + str(i[4]) + "; " + str(i[5]) + "\n"

    query_label = Label(root, text=print_rec)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width= 30)
delete_box.grid(row=9, column=1, pady=5)

# create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)
# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, columnspan=2, column=0, padx=10, pady=10, ipadx=137)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, columnspan=2, column=0, padx=10, pady=10, ipadx=135)

# Create an Update button
update_btn = Button(root, text="Update Record", command=edit)
update_btn.grid(row=11, columnspan=2, column=0, padx=10, pady=10, ipadx=130)
# Close Connection
conn.close()
root.mainloop()