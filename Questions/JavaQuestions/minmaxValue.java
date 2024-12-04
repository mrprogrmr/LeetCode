package JavaQuestions;

import java.util.Arrays;

class MinMaxValue {
    public int minDifference(int[] A) {
        int n = A.length, res = Integer.MAX_VALUE;
        if (n < 5) return 0;
        Arrays.sort(A);
        // Find the minimum difference between 4 consecutive elements
        for (int i = 0; i < 4; ++i) {
            // Use the absolute difference to avoid negative values
            // to get the smallest possible difference
            // and the maximum possible difference
            // by subtracting the smaller element from the larger one
            // and then adding the smaller element to the larger one
            // in case the difference is negative
            // and then subtracting the smaller element from the larger one
            // to get the smallest possible difference
            //
            res = Math.min(res, A[n - 4 + i] - A[i]);
        }
        return res;
    }
}
