class Knapsack: # define a class to better visualize/generalize

    def __init__(self, num_items, capacity): # constructor

        self.num_items = num_items
        self.capacity = capacity
        self.items = [(0, 0)] * (num_items + 1) # to keep numbering of items consistent 
        self.matrix = [[0] * (capacity + 1) for _ in range(num_items + 1)]
        # print(self.matrix), check if correctly initialized


    def add_item(self, weight, value):

        for i in range(1, len(self.items)):

            if self.items[i] == (0, 0):
                self.items[i] = (weight, value)
                break


    def get_max_value(self):

        dp = [row[:] for row in self.matrix]  # copy over the entire matrix to populate/memo

        for i in range(1, self.num_items + 1):
            
            for w in range(1, self.capacity + 1):
                
                if self.items[i][0] > w:
                    dp[i][w] = dp[i - 1][w] # Bellman equation p 1
                else:
                    dp[i][w] = max(dp[i - 1][w], self.items[i][1] + dp[i - 1][w - self.items[i][0]]) # Bellman equation p 2
        
        return dp[self.num_items][self.capacity]


def main():

    num_instances = int(input())
    instances = []

    for _ in range(num_instances):

        num_items, capacity = map(int, input().split())
        # create a new knapsack object
        ks = Knapsack(num_items, capacity)

        for _ in range(num_items):

            weight, value = map(int, input().split())
            ks.add_item(weight, value) # add each item and properties
       
        instances.append(ks)
    
    for instance in instances:
       
        print(instance.get_max_value())


if __name__ == "__main__":
    main()
