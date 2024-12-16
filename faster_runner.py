

# Get names and times from the user
runner1_name = input("Runner 1:\nName: ")
runner1_time = float(input("Time (in seconds): "))
runner2_name = input("Runner 2:\nName: ")
runner2_time = float(input("Time (in seconds): "))

# Compare times and print the result
if runner1_time < runner2_time:
    print(f"The faster runner is {runner1_name}")
elif runner2_time < runner1_time:
    print(f"The faster runner is {runner2_name}")
else:
    print(f"{runner1_name} and {runner2_name} have the same time")
