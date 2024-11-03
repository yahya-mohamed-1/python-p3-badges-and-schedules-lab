def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    return [f"Hello, {names[i]}! You'll be assigned to room {i + 1}!" for i in range(len(names))]

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    # Print room assignments
    for assignment in assign_rooms(names):
        print(assignment)
