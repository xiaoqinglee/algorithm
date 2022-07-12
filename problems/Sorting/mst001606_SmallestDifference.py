class Solution:
    def smallestDifference(self, a: list[int], b: list[int]) -> int:
        if len(a) == 0 or len(b) == 0:
            raise "Invalid Input"
        # element: tuple[value, value_from_a_list]
        a_and_b: list[tuple[int, bool]] = ([(val, True) for val in a] +
                                           [(val, False) for val in b])
        a_and_b.sort()
        min_distance: int | float = float("inf")
        for i in range(1, len(a_and_b)):
            if a_and_b[i][1] == a_and_b[i-1][1]:
                continue
            else:
                distance = a_and_b[i][0] - a_and_b[i-1][0]
                min_distance = min(min_distance, distance)

        return min_distance
