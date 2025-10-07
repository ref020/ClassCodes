public class RepetitionExample {
	public static void main(String[] args) {

		// while

		System.out.println("The While Loop");
		int counter = 0;

		while (counter < 10){
			System.out.print(counter);
			counter++;
		}

		while (counter < 10){
			System.out.println("This sentence will never print!");
			counter++;
		}

		System.out.println("\n");
		
		// do-while

		System.out.println("The While Loop");

		do{
			System.out.print(counter);
			counter--;
		} while (counter > 0);

		do{
			System.out.println("\nThis sentence will only print once");
			counter--;
		} while (counter > 0);

		System.out.println("\n");

		// for

		System.out.println("The For Loop");

		for (int i = 0; i < 5; i++){
			System.out.println("This will print 5 times exactly");
		}

		for (; counter > -5; counter -= 2){
			System.out.println("Now counter is " + counter);
		}
	}
}