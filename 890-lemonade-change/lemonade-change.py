class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fives = 0
        tens = 0
        # Dont need to keep track of 20s bc we can't give 20s in change

        for bill in bills:
            # print(bills[i])
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            elif bill == 20:
                if tens < 1:
                    fives -= 3
                    # tens -= 0
                    # change[20] += 1 
                else:
                    fives -= 1
                    tens -= 1
                    # change[20] += 1
            
            # print(change.items())

            if fives < 0 or tens < 0:
                return False
            
        return True
