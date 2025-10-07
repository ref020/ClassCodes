public class ArraysExample {
	public static void main(String[] args) {
		// To declare an array, use square brackets after the variable data type
		String[] names;
		
		// We can initialize the array with an array literal (comma separated values in {})
		String[] colors = {"red", "green", "blue"};

		// We can access an array element with its index number
		System.out.println(colors[0] + "\n");

		// We can also change an array element with its index number
		System.out.println(colors[2]);
		colors[2] = "cyan";
		System.out.println(colors[2]);

		// The length of an array can be found using its length property
		System.out.println("the list has " + colors.length + " elements");

		// The for-each loop iterates through all the elements in an array
		for (String color : colors){
			System.out.println(color + ", ");
		}
		// Multi-dimensional arrays can be created with nested {}
		String[][] colors2D = {{"red", "pink", "maroon"},{"blue","cyan","green"}};

		for (String[] colorArray : colors2D){
			for (String color : colorArray){
			System.out.print(color + ", ");
		} 
		System.out.println();
		}

		// The first index points to the color arrays inside colors2D,
		// and the second index points to a color in the array pointed
		// to by the first index
		System.out.println(colors2D[0][2]);
	}
}