import math

while True:
 	print("\nChoose operation:")
 	print("1. Add")
 	print("2. Subtract")
 	print("3. Mulitply")
 	print("4. Divide")
 	print( "5. Power")
 	print("6. Square root")
 	print("7. Precentage")
 	print( "8. Exit")
 	
 	choice = input("Enter choice: ")
 	
 	if choice == "1":
 		n1 = float(input("Enter frist number: "))
 		n2 = float(input("Enter second number: "))
 		print("Result:",n1 + n2)
 		
 	elif choice == "2":
 		n1 = float(input("Enter frist number: "))
 		n2 = float(input("Enter second number"))
 		print("Result:",n1 - n2)
 		
 	elif choice == "3":
 		n1 = float(input("Enter frist number: "))
 		n2 = float(input("Enter second number: "))
 		print("Result:",n1 * n2)
 		
 	elif choice == "4":
 		n1 = float(input("Enter frist number: "))
 		n2 = float(input("Enter second number: "))
 		if n2 == 0:
 			print("Error: Cannot divide by zero!")
 		else:
 			print("Result:", n1 / n2)
 			
 	elif choice =="5":
 			base = float(input("Enter base: "))
 			exp = float(input("Enter expoent: "))
 			print("Result:",base ** exp)
 			
 	elif choice == "6":
 		num = float(input("Enter number: "))
 		if num < 0:
 			print("Error: Negative number!")
 		else:
 			print("Square root:", math.sqrt(num))
 			
 	elif choice == "7":
 		total = float(input("Enter total: "))
 		part = float(input("Enter part: "))
 		if total == 0:
 			print("Error: Total cannot be zero!")
 		else:
 			print("Percentage:", (part / total) * 100, "%")
 			
 	elif choice == "8":
 		print("Exiting...")
 		break
 		
 		
 	else:
 		print("Invaild choice! Try again.")
