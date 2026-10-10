class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        fleet_count = 0
        last_time = 0

        for pos, spd in cars:
            t = (target - pos) / spd
            if last_time < t:
                last_time = t
                fleet_count += 1


        return fleet_count

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

sol = Solution()
print(sol.carFleet(target, position, speed))