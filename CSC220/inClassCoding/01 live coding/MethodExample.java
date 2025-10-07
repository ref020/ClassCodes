public class MethodExample {
	// This method, named methodOne, has a return type of void and is a static method
	// void means it does not return a value
	// static means the method belongs to the MethodExample class, and not a MethodExample object
	static void methodOne() {
		System.out.println("Your method just got called!");
	}

	// methodTwo has a single parameter, number, of type int
	// when it is called, an int value must be provided as an argument
	static void methodTwo(int number) {
		System.out.println("The parameter now contains the argument " + number);
	}

	// methodThree has two parameters of type double, num1 and num2
	// and it returns a value of type double
	static double methodThree(double num1, double num2) {
		// multiply the two arguments and save the result in a variable
		double result = num1 * num2;
		// return the double value stored in the variable result
		return result;
	}

	public static void main(String[] args) {
		// Call a method by writing its name followed by ()
		methodOne();
		// Pass in an argument that matches the data type of method parameter
		methodTwo(5);
		// save the returned value from methodThree into a variable
		double result3 = methodThree(3.14, 4.13);
		System.out.println("Method Tree returned " + result3);
	}
}