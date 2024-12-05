package JavaQuestions;

public class MoveZeroes {
	public static void main(String[] args) {
		int[] nums = {0,1,0,3,12};
		System.out.println(moveZeros(nums));
	}

	public static int[] moveZeros(int[] nums) {

		int left = 0;
		for (int right = 0; right < nums.length; right++) {
			if (nums[right] != 0) {
				int temp = nums[right];
				nums[right] = nums[left];
				nums[left] = temp;
				left++;
			}
		}
		return nums;
	}
}
