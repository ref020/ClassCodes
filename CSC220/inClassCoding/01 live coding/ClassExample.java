// Create a class with the class keyword
class ClassExample {
	String someText = "This string is a fiels of the ClassExample class!";

	public static void main(String[] args) {
		// Create an object from a class using the keyword new
		ClassExample obj = new ClassExample();

		// Access the attributes of an object using a "."
		System.out.println(obj.someText);

		// Multiple objects of the same class have separate attribute values
		ClassExample obj2 = new ClassExample();
		obj2.someText = "This string is different";

		System.out.println(obj.someText);
		System.out.println(obj2.someText);
		// The printSomeText method must be called from an object since it is not static
		obj.printSomeText("Printing some text!");
		// Removing the comment below throws an error since we tried calling it outside an object
		// printSomeText("Throwing an error!");
	}

	// Constructors are called when a new object of this class is created
	// Java creates one automatically if one is not provided
	// Constructors also have no return type
	public ClassExample() {
		someText = "A ClassExample object was just constructed";
	}

	// This method is not static, so it must be called from an object
	public void printSomeText(String textToPrint) {
		System.out.println(textToPrint);
	}
}