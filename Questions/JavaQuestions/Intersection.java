package JavaQuestions;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Intersection {
	public static void main(String[] args) {

		int[] nums1 = {1,2,3,2,3,0};
		int[] nums2 = {5,0,8,4,3,2};
		System.out.println(Arrays.toString(intersection(nums2, nums1)));

	}

	public static int[] intersection(int[] nums1, int[] nums2) {
		HashSet<Integer> set = new HashSet<>();
		List<Integer> list = new ArrayList<>();

		for (int num : nums1) 	set.add(num);
		for (int num : nums2) {
			if (set.contains(num)) {
				list.add(num);
				set.remove(num);
			}
		}

		int[] ans = new int[list.size()];
		for (int i=0; i<list.size(); i++) ans[i] = list.get(i);
		return ans;
	}
}
