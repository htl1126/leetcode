# ref: https://leetcode.com/problems/lemonade-change/solutions/143719/c-java-python-straight-forward

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            elif ten > 0:  # get 20 and give back 10 and 5
                five -= 1
                ten -= 1
            else:  # get 20 and give back three 5's
                five -= 3

            if five < 0:
                return False

        return True

