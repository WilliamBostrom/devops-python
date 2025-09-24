def print_menu(option, text):
  check = option in [1,2,3,4]
  if not check:
    print("Invalid choice")
    return
  print(f"You selected option {option}. {text}")


menu_is_running = True

while menu_is_running:
  menu_choice = input("Enter a choice (1-3. 4 to quit): ")


  if menu_choice == '1':
    print_menu(1, "Lågt val")
  elif menu_choice == '2':
    print_menu(2, "Medel val")
  elif menu_choice == '3':
    print_menu(3, "Högt val")
  elif menu_choice == '4':
    print_menu(4, "Ogiltigt val")
    break
  else:
    print('invalid choice')
  menu_choice = input("Enter a choice (1-3. 4 to quit)")
  

print("program exited.")
