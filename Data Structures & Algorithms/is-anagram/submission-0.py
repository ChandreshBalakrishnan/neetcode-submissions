class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = {}
        for letter in s:
            if letter not in visited:
                visited[letter] = 1
            else:
                visited[letter] += 1

        for l in t:
            if l in visited:
                visited[l] -= 1
            else:
                return False

        for value in visited.values():
            if value != 0:
                return False
        return True
