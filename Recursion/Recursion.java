public class Recursion {


	public static void main(String[] args) {

	int var = iterativeFactorial(3);
	System.out.println("Factorial with iteratiion: " + var);

	System.out.println();

	int var1 = recursiveFactorial(3);
	System.out.println("Factorial with recursion: " + var1);
	}

	// 1! = 0! * 1;
	// 2! = 1! * 2;
	// 3! = 2! * 3;
	// 4! = 3! * 4;
	// 5! = 4! * 5;
	// n! = (n-1)! * n
	public static int iterativeFactorial(int num) {

		if (num == 0) {
			return 1;
		}

		int factorial = 1;
		for (int i = 1; i <= num; i++) {
			factorial *= i;
		}
		return factorial;
	}

	public static int recursiveFactorial(int num) {

		if (num == 0) {
			return 1;
		}
		return num * recursiveFactorial(num - 1);
	}
}