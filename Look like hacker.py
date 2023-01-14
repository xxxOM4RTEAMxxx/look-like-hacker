import colorama
from colorama import Fore
while True:
	print(Fore.RED+"Hello user wanna look like a hacker?>:)")
	print(Fore.BLUE+"1)YEES!!:)")
	print(Fore.RED+"2)NO(lol)")
	choice = input(Fore.CYAN+"enter choice: ")
	
	choice = choice.strip()
	if (choice == "1"):
		while True:
			print(Fore.GREEN+"s^:U7I{=USb.M]j7dI6aQ1l+w1pC<'!{;jj\Ss^:U7I{=USb.M]j7dI6aQ1l+w1pC<'!{;jj")
	elif (choice == "2"):
		name = input(Fore.YELLOW+"well okay whats ur name?")	
		print(Fore.GREEN+"okay then rate that "+name)
		break
	else:
		print(Fore.RED+"you not dumb right?")		