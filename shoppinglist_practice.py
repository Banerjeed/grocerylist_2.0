groceries = [ ]

def addone_shopping(item):
	global groceries

	if item in groceries: 
		print "Error: that item is already on your grocery list"
	
	else: 
		item.lower()
		groceries.append(item)
		groceries.sort()
		return groceries

def delete_shopping(R_item):
	R_item.lower()
	if R_item not in groceries:
		print "Error: that item is not on your list. You cannot remove items that are not on your list"

	else: 
		return groceries.remove(R_item)
		

def main():
	answer = raw_input("Hello! Enter 1- if you want to add something to your shopping list; Enter 2 if you want to delete something from your shopping list; Enter 3 if you want to see your shopping list")
	
	if answer == "1":
		answer2 = raw_input("Enter the item you want to add")
		addone_shopping(answer2)
		return main()
	
	elif answer == "2":
		answer3 = raw_input("Enter the item you want to delete")
		delete_shopping(answer3)
		print answer3, " has now been deleted from your shopping list"
		
		answer4 = raw_input("Would you like to go back to the main menu? Enter 1 if yes; Enter 2 if no") 
		if answer4 == "1":
			return main()
		else: 
			print "OK, happy shopping!"

	else:
		print groceries
		return main()

if __name__ == '__main__':
	main()







