from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        
        graph = defaultdict(list)
        indegree = {}

        for recipe in recipes:
            indegree[recipe] = 0
        for recipe, ingre_list in zip(recipes, ingredients):

            for ingredient in ingre_list:
                graph[ingredient].append(recipe)
                indegree[recipe] += 1

        queue = deque(supplies)
        result = []

        while queue:
            have = queue.popleft()
            for recipe in graph[have]:
                indegree[recipe] -= 1
                
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
        return result
        
Solution = Solution()
print(Solution.findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]))