class LogSystem:

    def __init__(self):
        self.storage = []
        self.dicti = {"Hour": "3", "Month":"1", "Year":"0", "Minute":"4", "Day":"2", "Second":"5"}

    def put(self, id: int, timestamp: str) -> None:
        st = ""
        timestamp = timestamp.split(":")
        stamp = []
        for time in timestamp:
            st = st + time           
            stamp.append(st)
        self.storage.append([id, stamp])
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        index = int(self.dicti[granularity])
        times = sorted(self.storage, key=lambda x:x[1][index])
        start = start.split(":")
        end = end.split(":")
        st = ""
        ed = ""
        for i in range(index+1):
            st += start[i]
            ed += end[i]
            
        result = []
        for id, time in times:
            if time[index] >= st and time[index] <= ed:
                result.append(id)
        
        return result
        

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
