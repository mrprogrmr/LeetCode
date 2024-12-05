package JavaQuestions;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

import static java.lang.Math.abs;

public class ContainsDuplicateII {
	public static void main(String[] args) {

		int[] nums = {1, 2, 3, 1};
		int[] nums1 = {1, 2, 3, 1, 2, 3};
		System.out.println(containsNearbyDuplicate(nums, 3));
		System.out.println(containsNearbyDuplicate(nums1, 2));

		System.out.println(containsDuplicateHashSet(nums, 3));
		System.out.println(containsDuplicateHashSet(nums1, 2));
	}

	public static boolean containsNearbyDuplicate(int[] nums, int k) {     // Approach 1: Using Two Pointers

		int n = nums.length;

		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1; j < n; j++) {
				if (nums[i] == nums[j] && abs(i - j) <= k) {
					return true;
				}
			}
		}
		return false;
	}

	public static boolean containsDuplicateHashSet(int[] nums, int k) {     // Approach 1: Using HashSet

		// Base case...
		if(nums == null || nums.length < 2 || k == 0)
			return false;
		int i = 0;
		// Create a Hash Set for storing previous of k elements...
		HashSet<Integer> hset = new HashSet<Integer>();
		// Traverse for all elements of the given array in a for loop...
		for(int j = 0; j < nums.length; j++) {
			// If duplicate element is present at distance less than equal to k, return true...
			if(!hset.add(nums[j])){
				return true;
			}
			// If size of the Hash Set becomes greater than k...
			if(hset.size() >= k+1){
				// Remove the last visited element from the set...
				hset.remove(nums[i++]);
			}
		}
		// If no duplicate element is found then return false...
		return false;
	}

	public static boolean containsNearbyDuplicates(int[] nums, int k) {
		Map<Integer, Integer> seen = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {
			int val = nums[i];
			if (seen.containsKey(val) && i - seen.get(val) <= k) {
				return true;
			}
			seen.put(val, i);
		}

		return false;
	}
}