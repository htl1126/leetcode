# Ref: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/discuss/1646584/JavaPython-3-Toplogical-Sort-w-brief-explanation.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        suc, in_deg = collections.defaultdict(set), collections.defaultdict(int)
        for recipe, ingredient_list in zip(recipes, ingredients):
            for item in ingredient_list:
                suc[item].add(recipe)
            in_deg[recipe] = len(ingredient_list)

        available, ans = collections.deque(supplies), []
        while available:
            item = available.popleft()
            for recipe in suc.pop(item, set()):
                in_deg[recipe] -= 1
                if in_deg[recipe] == 0:
                    available.append(recipe)
                    ans.append(recipe)

        return ans
