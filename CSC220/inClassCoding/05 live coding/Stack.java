/*
Name:		[Your Name Here]
Date:		[Current Date Here]
Course:		CSC 220 - Data Structures
*/
public class Stack<Type> extends LinkedList<Type> {
	/**
	 * Default Constructor
	 * if a constructor is not provided, Java calls the default constructor instead (no parameters)
	 * the constructor below can be commented out or removed without changing the behavior of this class
	 */
	public Stack() {
		super();
	}

	/**
	 * adds an element on top of the stack (at the beginning of the linked list)
	 * @param 		element - the element to be pushed
	 */
	public void push(Type element) {
		add(0, element);
	}

	/**
	 * returns the element on top of the stack and removes it
	 * @return 		the element on top of the stack
	 */
	public Type pop() {
		Type popped = getFirst();
		remove(0);
		return popped;
	}

	/**
	 * returns the element on top of the stack WITHOUT removing it
	 * @return 		the element on top of the stack
	 */
	public Type peek() {
		return getFirst();
	}
}