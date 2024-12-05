package JavaQuestions;

import java.util.ArrayList;
import java.util.List;

public class DisappearedNumbers {     //Question 448
	public static void main(String[] args) {

		int[] nums = {4,3,2,7,8,2,3,1};
		System.out.println(findDisappearedNumbers(nums));

		int[] nums1 = {1,1};
		System.out.println(findDisappearedNumbers(nums1));
	}

	public static List<Integer> findDisappearedNumbers(int[] nums) {
		int n = nums.length;
		for (int i =0; i<nums.length; i++) {
			int originalValue = Math.abs(nums[i]);
			int idx = originalValue - 1;
			if (nums[idx] > 0) nums[idx] *= -1;
		}

		List<Integer> arraylist = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			if (nums[i] > 0) {
				arraylist.add(i + 1);
			}
		}
		return arraylist;
	}
}
