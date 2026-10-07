from collections import Counter
import matplotlib.pyplot as plt

# Order of task is as follows {0: 'Sleep', 1: 'Work', 2: 'Exercise', 3: 'Social', 4: 'Leisure'}
Weekly_activities = [0, 1, 1, 3, 4, 0, 1, 1, 3, 4, 0, 1, 1, 3, 4, 0, 1, 1, 3, 4, 0, 1, 1, 3, 4, 
                     0, 2, 2, 3, 4, 0, 2, 2, 3, 4]

# Calculate probabilities
def calculate_probabilities(sequence):
    """ Calculate probability distribution from a sequence.
    Args:
        sequence: List of integers representing activities
    return:
        probabilities in dictionary"""

    counts = Counter (sequence)
    total = len (sequence)
    probability = {k : v /total for k, v in counts.items()}
    return probability

activities_probabilities = calculate_probabilities(Weekly_activities)

#Display Results
activities = {0: 'Sleep', 1:'Work', 2: 'Excercise', 3: 'Social', 4 : 'Leisure'}
print("Activity Probability")
for k, v in sorted(activities_probabilities.items()):
    print (f"   {activities [k]} : {v:.2%}")

# Visualize
plt.figure (figsize=(10, 5))
action = [activities [k] for k in sorted(activities_probabilities.keys())]
percent = [activities_probabilities[k] for k in sorted(activities_probabilities.keys())]
plt.bar(action, percent, color= 'red')
plt.title ('Digital Twin Task')
plt.ylabel ('Percentage')
plt.xlabel ('Tasks')
plt.ylim (0, 0.4)
for i, v in enumerate(percent):
    plt.text(i, v + 0.01, f'{v:.1%}', ha= 'center')
plt.show()