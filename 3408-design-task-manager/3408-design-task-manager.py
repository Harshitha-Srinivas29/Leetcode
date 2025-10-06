class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            # self.task_map[taskId] = [priority, userId]
            # heappush(self.heap, [-priority, -taskId])
            self.add(userId, taskId, priority)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        t, userId = self.task_map[taskId]
        self.task_map[taskId] = (newPriority, userId)
        heapq.heappush(self.heap, (-newPriority, -taskId))
        

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]
        

    def execTop(self) -> int:
        while self.heap:
            p, t = heapq.heappop(self.heap)
            priority = -p
            taskId = -t
            entry = self.task_map[taskId]
            if entry is None:
                continue
            curr_p, curr_user = entry

            if curr_p != priority:
                continue

            del self.task_map[taskId]
            return curr_user
        return -1

        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()