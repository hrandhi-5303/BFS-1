from collections import deque,defaultdict
class Solution:
    def canFinish(self,numCourses,prerequisites):
        graph=defaultdict(list)
        in_degree=[0]*numCourses

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course]+=1

        queue=deque([i for i in range(numCourses) if in_degree[i]==0])
        completed=0

        while queue:
            curr=queue.popleft()
            completed+=1
            for neighbor in graph[curr]:
                in_degree[neighbor] -=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        
        return completed == numCourses
    
sol=Solution()
print(sol.canFinish(2,[[1,0]]))
print(sol.canFinish(2,[[1,0],[0,1]]))