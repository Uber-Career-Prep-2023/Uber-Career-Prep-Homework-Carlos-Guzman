"""An animal shelter that houses cats and dogs wants to ensure no pet has to wait too long for a forever home. Therefore, anyone who comes to adopt a pet can pick the species (cat or dog) but not the specific animal; they are assigned the animal of that species that has been in the shelter longest. If there are no animals available of the desired species, they must take the other species. You are given a list of pets in the shelter with their names, species, and time in the shelter at the start of a week. You receive a sequence of incoming people (to adopt pets) and animals (new additions to the shelter) one at a time. Print the names and species of the pets as they are adopted out.

Example (input and output forms one sequence of sample input):
Initial Input:
Sadie, dog, 4 days
Woof, cat, 7 days
Chirpy, dog, 2 days
Lola, dog, 1 day

Input: Bob, person, dog
Output: Sadie, dog

Input: Floofy, cat
Output:

Input: Sally, person, cat
Output: Woof, cat

Input: Ji, person, cat
Output: Floofy, cat

Input: Ali, person, cat
Output: Chirpy, dog
"""

"""
This problem uses two priority queues, one to maintain dogs and another for cats.

1) Create two priority queues, one for dogs and one for cats
2) Receive the initial values of the animals that are already in the animal shelter and classify them as dogs or cats. Depending on their species, put them in their respective queue. Their priority will be the time they have spent in the shelter. The queue will store the names of the animals and the priority they will receive will be the time they have been in the shelter.
3) Process incoming requests and classify whether they are people who want to adopt or animals entering the shelter.
4) If they are people who want to adopt, check what species they want to adopt and take out the animal with the highest priority from the respective queue of the species they wish to adopt.
5) If there are no animals of the species that the adopter wants, then look for the animal with the highest priority in the queue of the other species and assign it to the adopter. If there are no more animals in any queue, return False.
6) If there is an animal of the species that they want to adopt, extract the animal with the highest priority from the queue of the species they want and print the name and species of the animal.
7) If there are animals that enter in the input, verify the species of that animal and put it in its respective queue with a priority of 1.
8) Repeat all the steps from step 3) until there are no more requests.
"""


from queue import PriorityQueue

# Function to initialize the queues of cats and dogs
def initialPets(initial_input):
    cats = PriorityQueue()
    dogs = PriorityQueue()

    # Sorting animals to respective queues
    for pet in initial_input:
        if pet[1] == 'dog':
            dogs.put((-pet[2], pet[0]))   
        else:
            cats.put((-pet[2], pet[0]))
    return cats, dogs

# Function to process adoption or arrival of new pets
def AdoptAPet(dogs, cats, current_input):
    # If it's a person
    if current_input[1] == 'person':
        # Check for adoption preference
        if current_input[2] == 'dog':
            if not dogs.empty(): 
                return dogs.get()
            elif not cats.empty():
                return cats.get()
            else:
                return False
        else:
            if not cats.empty(): 
                return cats.get()
            elif not dogs.empty():
                return dogs.get()
            else:
                return False
    else:
        # If it's an animal
        if current_input[1] == 'dog':
            dogs.put((1, current_input[0]))
        else:
            cats.put((1, current_input[0]))
        return

initial_input = [('Sadie', 'dog', 4), ('Woof', 'cat', 7), ('Chirpy', 'dog', 2), ('Lola', 'dog', 1)]
cats, dogs = initialPets(initial_input)

# Test case: Bob adopts a dog
current_input = ('Bob', 'person', 'dog')
output = AdoptAPet(dogs, cats, current_input)
print(output[1] if output else 'No animals available for adoption.')

# Test case: Sally adopts a cat
current_input = ('Sally', 'person', 'cat')
output = AdoptAPet(dogs, cats, current_input)
print(output[1] if output else 'No animals available for adoption.')

# Test case: New dog (Spot) arrives at the shelter
current_input = ('Spot', 'dog')
output = AdoptAPet(dogs, cats, current_input)
print(output[1] if output else 'No animals available for adoption.')

