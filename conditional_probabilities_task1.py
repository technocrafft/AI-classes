from collections import Counter

# activies = {0:'sleep', 1:'work', 2:'excercise', 3:'leisure', 4:'social'}
week_activities = [0, 1, 4, 0, 1, 3, 0, 1, 3, 0, 1, 4,
                      0, 1, 3, 0, 1, 2, 0, 3, 2]

# Function to find probabilities of every action taken during the week
def activity_probability(sequence):
    a = Counter(sequence) #Returns dictionary containing count for item in sequence
    total = len(sequence) #Returns value of total item in sequence
    probability = {k : v/total for k, v in a.items()} #Return dictionary of item and percentage from 'a'
    return probability
probs = activity_probability(week_activities) #Call the funtion inserting week activities in sequence

#Display results
activities = {0:'sleep', 1:'work', 2:'excercise', 3:'leisure', 4:'social'}
print('Week activity percentage')
for k, v in sorted(probs.items()):#sort out items in probs dictionary an accending order
    print (f" {activities[k]}: {v:.2%}")# assign value of activity to similar key in probs & converts value to percentage

# conditional probability of next activity given current activity

def calculate_conditional_probability(sequence):
    condition = {}#Empty list which would contain current activity an all that comes after
    for i in range(len(sequence) - 1):#Give indicies for 14 out of 15 items
        now = sequence[i]#starts with index 0 and ends at index 14 (records then as present activty)
        after = sequence[i + 1]#Starts at index 1 and ends at index 15 (records them as future activity)

    if now not in condition:#check if entry is in the condition list
        condition[now] = []#Creates a new entry for the dictionary
    condition[now].append(after)#inserts values of after into the newly created entry

#Convert to conditional probabilities