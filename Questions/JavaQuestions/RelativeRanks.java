package JavaQuestions;

import java.util.Arrays;

public class RelativeRanks {
	public static void main(String[] args) {

		int[] score = {5,4,3,2,1};
		System.out.println(Arrays.toString(findRelativeRanks(score)));


	}

	public static String[] findRelativeRanks(int[] score) {

		int n = score.length;
		int[][] sortedPairs = new int[n][2];
		for (int i = 0; i < n; i++) sortedPairs[i] = new int[] {i, score[i]};

		Arrays.sort(sortedPairs, (x, y) -> (y[1] - x[1]));

		String[] ans = new String[n];

		for (int i =0; i < score.length; i++) {
			if (i == 0) {
				ans[sortedPairs[i][0]] = "Gold Medal";
			} else if(i == 1) {
				ans[sortedPairs[i][0]] = "Silver Medal";
			}else if (i == 2) {
				ans[sortedPairs[i][0]] = "Bronze Medal";
			} else {
				ans[sortedPairs[i][0]] = String.valueOf(i + 1);
			}
		}
		return ans;
	}
}
