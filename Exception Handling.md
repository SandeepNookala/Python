
#Error /Exception handling:
***************************
Interupting Normal Excecution of a code


try:
  risky code
except:
  print('Error')
else:
  print('No Error')
finally:
  print('always prints message')

#Example:
********
balance = 550.90

try:
    deposit = float(input('Enter amount:'))
except ValueError:
    print("please Enter valid amount")
else:
    final_Balance = balance+deposit
    print(final_Balance)
finally:
    print("Thank you")
	
