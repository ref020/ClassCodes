/*
Name:		[Your Name Here]
Date:		[Current Date Here]
Course:		CSC 220 - Data Structures
*/
public class Queue<Type> extends LinkedList<Type> {
	/**
	 * Adds an element to the back of the queue (the end of the linked list)
	 * @param 		element - the element to be enqueued
	 */
	public void enqueue(Type element) {
		add(element);
	}

	/**
	 * Removes and returns the element at the front of the queue (the beginning of the linked list)
	 * @return 		the element at the front of the queue
	 */
	public Type dequeue() {
		Type popped = getFirst();
		remove(0);
		return popped;
	}

	/**
	 * Returns the element at the front of the queue WITHOUT removing it
	 * @return 		the element on top of the stack
	 */
	public Type peek() {
		return getFirst();
	}
}