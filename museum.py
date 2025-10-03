class museum:
    def __init__(self, value, weight, Cmax):
        self.value = value
        self.weight = weight # sets the weights to weight
        self.cmax = Cmax # sets max capacity to cmax
        self.n = len(value) - 1 # the number of items in the museum -1 since index 0 is not used

    def __optimal_subset_value(self, value, weight, cmax):
        n = len(value) - 1 
        S = [] #empty list 
        i = 0
        while i <= n:
            row =[]
            r=0
            while r <= cmax:
                row.append(0) # append the row
                r = r + 1
            S.append(row) # append the row ro S
            i = i + 1

            #filling in teh table
        i = 1
        while i <= n:
            v_i = value[i] # gets i's value
            w_i = weight[i] #gets i's weight
            r = 1
            while r <= cmax:
                if w_i > r:
                    S[i][r] = S[i - 1][r] # cannt take the item i at teh capacity r, so take the previus row
                else:
                    S[i][r] = max(S[i - 1][r], S[i - 1][r - w_i] + v_i) # choosing weather to skip i or take i if it maximizes
                r = r + 1
            i = i + 1
        self.S = S
        return S
    

    def build_subset(self, S, value, weight, cmax):
        subset = [] #creates the empty list for the subset
        i = len(value) - 1 #starting from the last item and at full capacity
        r = cmax
        while i > 0 and r > 0: #iterate through the rows the the capacity is the same
            v_i = value[i] 
            w_i = weight[i]
            if w_i <= r and S[i][r] == S[i - 1][r - w_i] + v_i: #if item i meets the requirements than it was taken
                subset.append(i)
                r = r - w_i # reduces the capacity after taking another item
            i = i - 1 # iterates to next itmem

        left = 0 # change the subset indicies to ascenting order
        right = len(subset) - 1
        while left < right:
            tmp = subset[left]
            subset[left] = subset[right] #swapping left and right
            subset[right] = tmp
            left = left + 1
            right = right - 1
        return subset
    
    def sum_weights(self, indices):
        total_weight = 0
        j = 0
        while j < len(indices):
            total_weight = total_weight + self.weight[indices[j]] # add the weight to the total weight so we know how much room is left in cmax
            j = j + 1
        return total_weight
    
    def sum_values(self, indices):
        total_value = 0
        j = 0
        while j < len(indices):
            total_value = total_value + self.value[indices[j]] # as it iterates through each, it will sum the value if it's added so we know the total value
            j = j + 1
        return total_value
    
    def power_set_size(self):
        return 2 ** self.n #2^size of set is the size of the power set 
    
    def solve(self):
        S = self.__optimal_subset_value(self.value, self.weight, self.cmax) # calls optimal subset which will build the table that we biult in class which helps get the max
        subset = self.build_subset(S, self.value, self.weight, self.cmax)# calls build subest to backtrack through S so we nkow the optimal solution
        total_weight = self.sum_weights(subset) #calls sum weights to get the sum of the weights in the optimal subset
        total_value = self.sum_values(subset) #calls the sum value to get the sum of the max values in the optimal set

        rows = self 
        cols = self.cmax + 1
        total_subsets = self.power_set_size()
        optimal_value = S[self.n][self.cmax] # gets teh optimal value from teh table 

        print("Theoretically possible subsets:", total_subsets)
        print("Size of matrix S:", len(S), "rows x", len(S[0]), "columns")
        print("Number of items in the optimal subset:", len(subset))
        print("Total weight of the optimal subset:", total_weight, "(capacity =", self.cmax, ")")
        if total_weight <= self.cmax:
            print("The subset respects the capacity restriction unless i forgot to take out the bag of apples.")
        else:
            print("The subset exceeds the capacity restriction!") 
            
        print("Total value of the items in the optimal subset:", total_value)
        return S, subset


if __name__ == "__main__":
        value = [None, 10, 5, 16, 11]  # value[0] unused
        weight = [None, 3, 2, 4, 4]    # weight[0] unused
        c_max = 10
        small_museum = museum(value, weight, c_max)
        small_museum.solve()
