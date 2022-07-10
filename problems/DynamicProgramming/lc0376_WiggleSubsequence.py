class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:

        # nums[i]作为子序列的最后一个元素且身份为山谷时最长的那个子序列[foo...i]的信息

        # as_valley_is_nth_elem_in_seq[i]是这个子序列的长度
        as_valley_is_nth_elem_in_seq: list[int] = [-1] * len(nums)
        # as_valley_prev_elem_idx[i]是这个子序列中倒第二个元素的索引
        as_valley_prev_elem_idx: list[int] = [-1] * len(nums)

        # nums[i]作为子序列的最后一个元素且身份为山峰时最长的那个子序列[foo...i]的信息

        # as_peak_is_nth_elem_in_seq[i]是这个子序列的长度
        as_peak_is_nth_elem_in_seq: list[int] = [-1] * len(nums)
        # as_peak_prev_elem_idx[i]是这个子序列中到第二个元素的索引
        as_peak_prev_elem_idx: list[int] = [-1] * len(nums)

        as_valley_is_nth_elem_in_seq[0] = 1
        as_peak_is_nth_elem_in_seq[0] = 1

        for j in range(1, len(nums)):

            # j 作为子序列最后一个元素且 j 是山峰, 满足这样条件的子序列中最大的子序列长度
            max_seq_len = 0
            for i in range(0, j):
                if nums[i] < nums[j]:
                    seq_len = as_valley_is_nth_elem_in_seq[i] + 1
                    if seq_len > max_seq_len:
                        max_seq_len = seq_len
                        as_peak_is_nth_elem_in_seq[j] = seq_len
                        as_peak_prev_elem_idx[j] = i

            # j 作为子序列最后一个元素且 j 是山谷, 满足这样条件的子序列中最大的子序列长度
            max_seq_len = 0
            for i in range(0, j):
                if nums[i] > nums[j]:
                    seq_len = as_peak_is_nth_elem_in_seq[i] + 1
                    if seq_len > max_seq_len:
                        max_seq_len = seq_len
                        as_valley_is_nth_elem_in_seq[j] = max_seq_len
                        as_valley_prev_elem_idx[j] = i

        last_elem_is_peak: bool = True
        longest_subsequence_len = as_peak_is_nth_elem_in_seq[len(nums) - 1]
        if as_valley_is_nth_elem_in_seq[len(nums) - 1] > as_peak_is_nth_elem_in_seq[len(nums) - 1]:
            last_elem_is_peak: bool = False
            longest_subsequence_len = as_valley_is_nth_elem_in_seq[len(nums) - 1]

        return max(max(as_valley_is_nth_elem_in_seq), max(as_peak_is_nth_elem_in_seq))
