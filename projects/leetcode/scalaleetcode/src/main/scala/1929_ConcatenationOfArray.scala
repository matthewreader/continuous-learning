package leetcode.scalaleetcode

object ConcatenationOfArray {
    def getConcatenation(nums: Array[Int]): Array[Int] = {
        return Array.concat(nums, nums)
    }
}