'''Оценка массива определяется как произведение его суммы
 и его длины .

Например, оценка [1, 2, 3, 4, 5]равна (1 + 2 + 3 + 4 + 5) * 5 = 75.
Дан положительный целочисленный массив numsи целое число k,
вернуть количество непустых подмассивов,
nums оценка которых строго меньше k'''


class Solution(object):
    def countSubarrays(self, nums, k):
        res = 0
        left = 0
        total_sum = 0

        for right in range(len(nums)):
            total_sum += nums[right]

            while left <= right and total_sum * (right - left + 1) >= k:
                total_sum -= nums[left]
                left += 1

            res += right - left + 1

        return res
