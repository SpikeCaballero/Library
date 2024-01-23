"""Library program to control lending and returning books from the titles available.
This library is the Disc World Library, dedicated to the late, great author Terry Pratchett! """

# This function is to check that we have the title in library, this with be called on multiple times through out the program.
def get_book():
      title = input("What is the Title of the book? " ).capitalize()
      if title in books_inventory:
            return title
      else:
            print("we don't have that title in our inventory.")
            return 
      

# This function is to check that we have the member registered in library, this with be called on multiple times through out the program.
def get_user():
      user = input("Please enter the name of the member. " ).capitalize()
      if user in users_info:
            return user
      else:
            answer = input("Member does not exist. Would you like to register a new member? Y/N  " ).upper()
            if answer == "Y":
                  new_user() # the call to a function dedicated to adding a new member.
                  get_user() # once a new member is added, we recall the function so we don't break the process flow.
            else:
                print("Ok, we've returned to the main menu.")
                return 
            
      
""" This function allows for the book to be borrowed, checking we have the book and the member is registered.
Then updating the necessary perameters of book and member."""

def borrow_book():
      existing_title = get_book() # call to check we have the book
      existing_user = get_user() # call to check the member is registered
      if not existing_title or not existing_user:
            print("Sorry, either we don't have your title or the member is not registered. Try again.")
            return
      else:
        if books_inventory[existing_title]['copies'] > 0 and len(users_info[existing_user]['borrowed_books']) < 3:
           books_inventory[existing_title]['copies'] -= 1 
           books_inventory[existing_title]['current_borrowers'].append(existing_user) 
           users_info[existing_user]['borrowed_books'].append(existing_title) 
           print(f"Book '{existing_title}' checked out successfully.")
        else:
           print("Error: Book not available or user has reached the maximum borrow limit.")
              
      return


""" This function allows for the book to be returned, once again checking the book exists and the member is registered.
Then updating the necessary perameters of book and member."""

def return_book():
      existing_title = get_book() # call to check we have the book
      existing_user = get_user() # call to check the member is registered
      fine = fines(existing_user)
      if not existing_title or not existing_user:
            print("Sorry, either we don't have your title or the member is not registered. Try again.")
            return
      else:
        if existing_title in users_info[existing_user]['borrowed_books']:
            books_inventory[existing_title]['copies'] += 1
            books_inventory[existing_title]['current_borrowers'].remove(existing_user)
            users_info[existing_user]['borrowed_books'].remove(existing_title)
            print(f"Book {existing_title} returned successfully. ")
        else:
            print("User has not borrowed this book. ")
      
      return


# This function will show which books the member is currently borrowing or if they have had any fines in the past.
def user_history(): 
      user = input("Please type member's name:  ").capitalize()
      if user in users_info:
           print(f"Here is {user}'s details : \n {users_info[user]} \n ")
           return
      else:
           print("Sorry, we don't have record of that user.")
      return


# This function adds a new member, also checking if that member already exists.
def new_user():
      new_member = input("Please enter the name of our new member : ").capitalize()
      if new_member in users_info:
           print(f" {new_member} is already registered.")
           return
      else:
           users_info[new_member] = {'borrowed_books': [], 'fines': 0}
           print(f"Welcome, {new_member}! ")
      
      return

# This function will update the ammount of copies fo a title. We recieve the title on the function call. 
def change_copies(title):
     copy_qty = int(input("How many copies would you like to add?   "))
     books_inventory[title] = {'copies': copy_qty, 'current_borrowers':[]}
     return

"""This funtion will add a title to the library, checking to see if we already have it. 
Then calling change_copies give said funtion the title entered."""

def add_title():
     title = input("Please enter the title of the book you wish to add to the library. \n")
     if title in books_inventory:
          dession = input("This title already exists in the library, would you like to change the ammount of copies? Y/N :  ").upper()
          if dession == "Y":
               change_copies(title) # This will allow you to modify the ammount of copies for an existing title
          else:
               return
     else: 
          change_copies(title) # this will add a new title directly.
          return
     
# This fuction will remove a title from the library.
def remove_title():
     title = input("Please enter the title of the book you wish to remove from the library. \n").capitalize() 
     if title in books_inventory:
          books_inventory.pop(title)
          return
     else:
          print("That book isn't in the library.")
          return


# This function will show a list of all books in the library.
def show_library():
     list = books_inventory.keys()
     for i in list:
          print(f"{i} \n")
     return

""" Option 5 in the main menu has multiple option so we go through those options here seperatly, for better work flow.
The display list for all titles is here because you might want to check a book title first to confirm it's name before adding or removing it."""

def book_titles():
      choise = int(input("""What would you like to do? 
                     
                     1. Add a book to the library
                     2. Remove a book from the library
                     3. Display a list of current titles
                     
                     Please choose :  """))
      if choise == 1:
           add_title()

      elif choise == 2:
           remove_title() 

      elif choise == 3:
           show_library()
      else:
           print("That wasn't on of the choises, Please try again. ")              
      
      return
# This function will see if the member has had the book too long and fine accordingly. Adding a mark to their permanent record.
def fines(user):
     late = input("Has the borrowed book been out for more than 7 days? (Y/N) ").upper()

     if late == "Y":
          days = int(input("How many days more than 7? "))
          fine = days * .5
          users_info[user]['fines'] += 1
          print(f"A fine of £{fine} has been issued and a record has been made. ")
          return
     else:
          print("Well done, no need to pay a fine and your record need not be permanently tarnished. ")
            

     return
# These are the dictionaries for books in stock and members. Future itterations, this will be a seperate txt file.
books_inventory = {'The Colour of Magic':{'copies': 5, 'current_borrowers':[]}, 
                   'The Light Fantastic':{'copies': 3, 'current_borrowers':[]},
                   'Equal Rites':{'copies': 4, 'current_borrowers':[]},
                   'Mort':{'copies': 5, 'current_borrowers':[]},
                   'Sourcery' :{'copies': 3, 'current_borrowers':[]},
                   'Wyrd Sisters' :{'copies': 6, 'current_borrowers':[]},
                   'Pyramids' :{'copies': 4, 'current_borrowers':[]},
                   'Guards! Guards!' :{'copies': 4, 'current_borrowers':[]},
                   'Eric' :{'copies': 3, 'current_borrowers':[]},
                   }

users_info = {'Spike': {'borrowed_books': [], 'fines': 0},
              'Nizzam':{'borrowed_books':[], 'fines': 0},
              'John':{'borrowed_books':[], 'fines': 0},
              'Steve':{'borrowed_books':[], 'fines': 0},
              'Dave':{'borrowed_books':[], 'fines': 0},
              }


# Main program. Here is where we begin our jouney. 
while True:
        
        try:
            menu_choice = int(input(""" Welcome to Disc World Library please choose one of the options below :
                    
                    1. Borrow a book
                    2. Return a book
                    3. User history
                    4. New Member
                    5. Add/Remove Title
                    6. Exit

                    Please make your choice :  """))
        
 
            if menu_choice == 1:
                  borrow_book()

            elif menu_choice == 2:
                  return_book()

            elif menu_choice == 3:
                  user_history()        
            
            elif menu_choice == 4:
                  new_user()

            elif menu_choice == 5:
                  book_titles()      

            elif menu_choice == 6:
                  break
            else:
                  print("Sorry but that's not one of the options, please try again.") 
                  continue
            

        except ValueError:
            print("Sorry but that's not a number, please try again.")    
            continue         