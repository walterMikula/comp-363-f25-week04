class museum:
    def __init__(self, value, weight, Cmax):
        self.value = value
        self.weight = weight
        self.cmax = Cmax
        self.n = len(value) - 1

    def __optimal_subset_value(self, value, weight, cmax):
        n = len(value) - 1
        S = []
        i = 0
        while i <= n:
            row =[]
            r=0
            while r <= cmax:
                row.append(0)
                r = r + 1
            S.append(row)
            i = i + 1

            #filling in teh table
        i = 1
        while i <= n:
            v_i = value[i]
            w_i = weight[i]
            r = 1
            while r <= cmax:
                if w_i > r:
                    S[i][r] = S[i - 1][r]
                else:
                    S[i][r] = max(S[i - 1][r], S[i - 1][r - w_i] + v_i)
                r = r + 1
            i = i + 1
        self.S = S
        return S
    

    def build_subset(self, S, value, weight, cmax):
        subset = []
        i = len(value) - 1
        r = cmax
        while i > 0 and r > 0:
            v_i = value[i]
            w_i = weight[i]
            if w_i <= r and S[i][r] == S[i - 1][r - w_i] + v_i:
                subset.append(i)
                r = r - w_i
            i = i - 1

        left = 0
        right = len(subset) - 1
        while left < right:
            tmp = subset[left]
            subset[left] = subset[right]
            subset[right] = tmp
            left = left + 1
            right = right - 1
        return subset
    
    def sum_weights(self, indices):
        total_weight = 0
        j = 0
        while j < len(indices):
            total_weight = total_weight + self.weight[indices[j]]
            j = j + 1
        return total_weight
    
    def sum_values(self, indices):
        total_value = 0
        j = 0
        while j < len(indices):
            total_value = total_value + self.value[indices[j]]
            j = j + 1
        return total_value
    
    def power_set_size(self):
        return 2 ** self.n
    
    def solve(self):
        S = self.__optimal_subset_value(self.value, self.weight, self.cmax)
        subset = self.build_subset(S, self.value, self.weight, self.cmax)
        total_weight = self.sum_weights(subset)
        total_value = self.sum_values(subset)

        rows = self
        cols = self.cmax + 1
        total_subsets = self.power_set_size()
        optimal_value = S[self.n][self.cmax]

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