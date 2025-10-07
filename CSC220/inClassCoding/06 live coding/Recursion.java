/*
Name:		[Your Name Here]
Date:		[Current Date Here]
Course:		CSC 220 - Data Structures
*/

public class Recursion {
	public static void main(String[] args) {

	}

	/**
	 * Recursively evaluates and returns base^exp
	 * @param 			base - the exponent's base
	 * @param 			exp - the exponent
	 * @return 			the evaluated result of base^exp
	 */
	public static int pow(int base, int exp) {
		if (exp == 0){
			return 1;
		} else if (exp == 1){
			return base;
		} else {
			return base * pow(base, exp - 1);
		}
	}

	/**
	 * Recursively evaluates and returns num!
	 * @param 			num - the factorial base
	 * @return 			num factorial (num!)
	 */
	public static int factorial(int num) {
		if (num >= 0){
			if (num == 0){
				return 1;
			} else {
				return num * factorial(num - 1);
			}
		}
		return 0;
	}

	/**
	 * Recursively evaluates and returns the Fibonacci number corresponding to the input number
	 * @param 			num - the index of the number to return in the Fibonaci sequence
	 * @return 			the Fibonacci number at index num in the Fibonacci sequence
	 */
	public static int fib(int num) {
		if (num >= 0){
			if (num == 0){
				return 0;
			} else if (num == 1){
				return 1;
			} else {
			return fib(num - 1) + fib(num - 2);
			}
		}
		return 0;
	}
}