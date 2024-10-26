def recaman_sequence(n):

    sequence = [0]  

    for k in range(1, n):
       
        next_value = sequence[-1] - k
        if next_value > 0 and next_value not in sequence:
            sequence.append(next_value)
        else:
            sequence.append(sequence[-1] + k)

    return sequence

n = int(input("Enter the length of the Recamán sequence: "))

print("The Recamán sequence is:", recaman_sequence(n))


