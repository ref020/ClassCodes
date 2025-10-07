public class SelectionExample {
	public static void main (String[] args) {
		// Get integer argument from command line
		int argument = Integer.parseInt(args[0]);

		// if
		if (argument == 0 ){
			System.out.println("if");
		}
		// else if
		else if (argument == 1 ){
			System.out.println("else if");
		}
		// else
		else {
			System.out.println("else");
		}
		// switch
		switch (argument) {
			case 1:
				System.out.println(1);
			case 2:
				System.out.println(2);
			case 3:
				System.out.println(3);
				break;
			case 4:
				System.out.println(4);
			case 5:
				System.out.println(5);
			case 6:
				System.out.println(6);
				break;
			default:
				System.out.println("default");
		}
		}
	}
