from collections import deque, defaultdict
import bisect
class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packets = set()
        self.queue = deque()
        self.destination_counts = defaultdict(list) # destination -> sorted list of timestamps

        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.packets: return False
        if len(self.packets) >= self.memoryLimit:
            self.forwardPacket()

        self.packets.add(packet)
        self.queue.append(packet)
        self.destination_counts[destination].append(timestamp)

        return True

        

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []
        for_packet = self.queue.popleft()
        self.packets.remove(for_packet)
        destination = for_packet[1]
        self.destination_counts[destination].pop(0)
        return list(for_packet)
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps_list = self.destination_counts.get(destination, [])
        if not timestamps_list:
            return 0
        
        left = bisect.bisect_left(timestamps_list, startTime)
        right = bisect.bisect_right(timestamps_list, endTime)
        return right - left
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)