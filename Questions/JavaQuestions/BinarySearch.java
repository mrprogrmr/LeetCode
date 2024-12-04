package JavaQuestions;

public class BinarySearch {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] > target) {
                end = mid - 1;
            }
            else if (nums[mid] < target) {
                start = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        // int[] nums = {2, 5, 6, 0, 0, 1, 2};
        // Solution sol = new Solution();
        // int target = 0;
        // int result = sol.search(nums, target);
        // System.out.println("Index of target: " + result);

    }

}


// 1. The method search takes two parameters:
// nums: A sorted integer array to search in
// target: The value we're looking for
// 2.
// We initialize two pointers:
// start: Points to the beginning of the array (index 0)
// end: Points to the end of the array (index nums.length - 1)
// 3.
// The main search logic is inside a while loop that continues as long as start is less than or equal to end:
// while (start <= end) {
//     // ... search logic ...
// }
// 4.
// In each iteration, we calculate the middle index:
// int mid = (start + end) / 2;
// 5.
// We then compare the value at the middle index with the target:

// a. If nums[mid] equals the target, we've found the value and return its index:
// if (nums[mid] == target) {
//     return mid;
// }

// b. If nums[mid] is greater than the target, the target must be in the left half of the array, so we update end:
// else if (nums[mid] > target) {
//     end = mid - 1;
// }

// c. If nums[mid] is less than the target, the target must be in the right half of the array, so we update start:
// else if (nums[mid] < target) {
//     start = mid + 1;
// }
// 6.
// If the while loop completes without finding the target, it means the target is not in the array, so we return -1:
// return -1;
