def printArray(arr, n):
    # Iterating and printing the array
    for i in range(n):
        print(arr[i], end=" ")


# Function to implement the
# quadratic probing


class HashTable:
    def __init__(self, size, modulo):
        self.size = size
        self.hash_modulo = modulo
        self.hash_table = [0] * size
        for i in range(size):
            self.hash_table[i] = -1

    def printArray(self):
        # Iterating and printing the array
        for i in range(self.size):
            print(f"{self.hash_table[i]} {i}", end="\n")

    def hash(self, arr):
        print(arr)
        # Iterating through the array
        for i in range(len(arr)):
            # Computing the hash value
            hv = i % self.size
            # Insert in the table if there
            # is no collision
            if self.hash_table[hv] == -1:
                self.hash_table[hv] = arr[i]
            else:
                # If there is a collision
                # iterating through all
                # possible quadratic values
                for j in range(self.size):
                    # Computing the new hash value
                    t = (hv + j * j) % self.size
                    if self.hash_table[t] == -1:
                        # Break the loop after
                        # inserting the value
                        # in the self.hash_table
                        self.hash_table[t] = arr[i]
                        break
                    else:
                        continue
        self.printArray()
