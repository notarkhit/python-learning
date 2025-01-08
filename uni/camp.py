
def total_chocolates(chocolates):
    """Calculate the total number of chocolates received by all children."""
    return sum(chocolates)

def reward_extra_chocolates(child_ids, chocolates, child_id, extra_chocolates):
    """Reward a child with extra chocolates for good conduct."""
    # Validate extra chocolates
    if extra_chocolates < 1:
        return "Extra chocolates is less than 1"
    
    # Validate child_id
    if child_id not in child_ids:
        return "Child is invalid"
    
    # Add extra chocolates
    index = child_ids.index(child_id)
    chocolates[index] += extra_chocolates
    return chocolates

# Input: child IDs and their chocolates
num_children = int(input("Enter the number of children: "))
child_ids = []
chocolates = []

print("Enter the child IDs and chocolates:")
for _ in range(num_children):
    child_id = int(input("Child ID: "))
    num_chocolates = int(input(f"Number of chocolates for child {child_id}: "))
    child_ids.append(child_id)
    chocolates.append(num_chocolates)

child_ids = tuple(child_ids)

# 1. Calculate total chocolates
print("\nCalculating total chocolates...")
print("Total chocolates received by all children:", total_chocolates(child_ids))

# 2. Reward extra chocolates
print("\nRewarding extra chocolates...")
child_id = int(input("Enter the child ID to reward extra chocolates: "))
extra_chocolates = int(input(f"Enter the number of extra chocolates for child {child_id}: "))

result = reward_extra_chocolates(child_ids, chocolates, child_id, extra_chocolates)
if isinstance(result, list):
    print("Updated chocolates list:", result)
else:
    print(result)
