class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for currentPath in paths:
            if currentPath == "..":
                if stack:
                    stack.pop()
            elif currentPath != "" and currentPath != ".":
                stack.append(currentPath)
        
        return "/" + "/".join(stack)