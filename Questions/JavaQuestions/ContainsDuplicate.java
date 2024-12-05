package JavaQuestions;

import java.util.Arrays;

public class ContainsDuplicate {
	public static void main(String[] args) {
		int[] nums = {1,2,3,1};
		System.out.println(containsDuplicate(nums));
		System.out.println(containsDuplicates(nums));

	}

	public static boolean containsDuplicate(int[] nums) {   // Approach 1: Brute Force

		for (int i = 0; i < nums.length - 1; i++) {
			for (int j = i + 1; j < nums.length; j++) {
				if (nums[i] == nums[j]) {
					return true;
				}
			}
		}
		return false;
	}

	public static boolean containsDuplicates(int[] nums) { 		// Approach 2: Sorting

		Arrays.sort(nums);
		int n = nums.length;
		for (int i = 1; i < n; i++) {
			if (nums[i] == nums[i-1]) {
				return true;
			}
		}
		return false;
	}
}
