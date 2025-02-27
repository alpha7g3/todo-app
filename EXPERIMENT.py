date = input("enter today's date: ")
mood = input("rate ur mood on a scale 1--10: ")
thought = input("write on ur thoughts" + "\n")

with open(f"../PythonProject1/{date}.txt" , "w") as file:
    file.write(mood + 2* "\n")
    file.write(thought)

