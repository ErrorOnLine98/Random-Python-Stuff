# Given the following array of arrays of numbers representing a list of intervals, merge all overlapping intervals.
# [[6,9],[2,12],[2,4],[13,18],[10,11],[24,32],[10,14],[17,26],[25,30],[15,24],[1,7],[11,16],[5,15],[19,25],[15,23],[24,30]]

# Example: [[1, 3], [8, 10], [2, 6], [10, 16]] would merge into [[1, 6], [8, 16]]. The intervals must be returned in
# ASCENDING order. You can assume that in an interval, the first number will always be smaller than the second.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # This solution should be 0(nLogn)
        intervals.sort(key=lambda i: i[0])  # Sort the intervals by their start values in ascending order
        output = [intervals[0]]  # I'm including the first interval as part of the output

        # Iterate through the intervals starting at the second interval
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]  # The last value of the previous interval

            # Intervals overlap if the start value of an interval is <= the end value of a different interval
            if start <= lastEnd:
                # We take the max of the two end values of the overlapping intervals and set it as the last value of
                # the current interval. We do this to handle cases like [1, 5], [2, 4] where the first one has a
                # larger end value
                output[-1][1] = max(lastEnd, end)
            else:
                # If the intervals don't overlap, it should still be added to the output
                output.append([start, end])

        return output


def main():
    solution = Solution()

    # The example intervals
    intervals = [[6, 9], [2, 12], [2, 4], [13, 18], [10, 11], [24, 32], [10, 14], [17, 26], [25, 30], [15, 24], [1, 7],
                 [11, 16], [5, 15], [19, 25], [15, 23], [24, 30]]
    result = solution.merge(intervals)

    print(result)  # The result should be [[1, 32]] since they all overlap


if __name__ == '__main__':
    main()
