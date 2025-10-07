/*
Name:	 	[Ray Favaza]
Date:		[10/10/2023]
Course:		CSC 220 - Data Structures
*/

public class LinkedList<Type> extends AbstractLinkedList<Type> {
	/**
	 * Default Constructor - Newly constructed lists have no nodes,
	 * so head and tail point to null.
	 */
	public LinkedList() {
		head = null;
		current = null;
		tail = null;
		numElements = 0;
	}

	/**
	 * Copy constructor - copies each element from the given linked list
	 * into the one being constructed.
	 * @param 			l - the linked list being copied from
	 */
	public LinkedList(LinkedList<Type> l) {
		this.head = l.head;
		this.current = l.current;
		this.tail = l.tail;
		this.numElements = l.numElements;
        }
        
	/**
	 * Returns a String representation of the list ("NULL" if empty)
	 * @return 			String representation of the linked list
	 */
	public String toString() {
		if(head == null)
		{
			return "NULL";
		}
		else
		{
			String s = "";

			Node<Type> temp = head;
			while(temp != null)
			{
				s += temp.getData() + " ";
				temp = temp.getLink();
			}
			return s;

		}

	}

	/**
	 * Returns the number of elements in the list (not the max capacity)
	 * @return 			number of elements in the linked list
	 */
	public int size() {
		return numElements;
	}

	/**
	 * Returns true if there are no elements in the list
	 * @return 			true if list is empty, false otherwise
	 */
	public boolean isEmpty() {
		return (numElements == 0);
	}

	/**
	 * Returns true if the number of elements in the list is equal to MAX_SIZE
	 * @return 			true if list is full, false otherwise
	 */
	public boolean isFull() {
		return (numElements == MAX_SIZE);
	}

	/**
	 * Set the current Node reference to the head node
	 */
	public void first() {
		current = head;
	}

	/**
	 * Set current to the next node in the list
	 */
	public void next() {
		//Question mark with the colon means that current != null, then current.getLink is what current set equal to, 
		//while if it is not, current is set equal to current
		current = (current != null) ? current.getLink() : current;
	}

	/**
	 * Return the element at the current node
	 * @return 			element stored at the current node
	 */
	public Type getCurrent() {
		return (current != null) ? current.getData() : null;
	}

	/**
	 * Adds the specified element to the end of the list.
	 * Not possible for a full list.
	 * @param 			element - element to add to the linked list
	 */
	public void add(Type element) {
		if(isFull())
		{
			return;
		}
		else if(isEmpty())
		{
			head = new Node<Type>();
			head.setData(element);
			tail = head;
			current = head;
		}
		else
		{
			tail.setLink(new Node<Type>());
			tail = tail.getLink();
			tail.setData(element);
		}
		numElements ++;
		return;
	}

	/**
	 * Returns the value in the node at the given index
	 * @param 			index - the position in the list to get the element from
	 * @return 			the element at index
	 */
	public Type get(int index) {
		if(!(index <0 || index >= numElements))
		{
			Node<Type> temp = head;
			int i = 0;

			while(i<index)
			{
				temp = temp.getLink();
				i++;
			}
			return temp.getData();
		}
		return null;

	}

	/**
	 * Returns the value in the head node
	 * @return 			the value in the head node
	 */
	public Type getFirst() {
		return (head != null ? head.getData() : null);
	}

	/**
	 * Returns the value in the tail node
	 * @return 			the value in the tail node
	 */
	public Type getLast() {
		return (tail != null ? tail.getData() : null);
	}

	/**
	 * Removes the element at the specified index.
	 * Not possible for an empty list
	 * @param			index - the position in the list of the element to be removed
	 */
	public void remove(int index) {
		if(size() <= MAX_SIZE && index >= 0 && index <= size()){
			if (index == 0 && head != null){
				head = head.getLink();
			} else{
				current = head;
				int position = 0;

				while(current != null && position < index - 1){
					current = current.getLink();
					position++;

				}
				if (current == null || current.getLink() == null){
					return;
				}
				current.setLink(current.getLink().getLink());
				numElements++;
			}

		}
	}

	/**
	 * Replaces the element at the specified index with the given element
	 * @param			index - the position in the list of the element to replace
	 * @param			element - the element to replace the current element at index
	 */
	public void set(int index, Type element) {
		if (head == null) {
            return;
        }

        Node<Type> current = head;
        int position = 0;

        while (current != null && position < index) {
            current = current.getLink();
            position++;
        }
        if (current == null) {
            return;
        }

        current.setData(element);
	}

	/**
	 * Returns the index of the first occurrence of the specified element.
	 * Returns -1 if the list does not contain the element.
	 * @param			element - the element whose index is being searched for
	 * @return 			the index of element, or -1 if it doesn't exist
	 */
	public int indexOf(Type element) {

        Node<Type> current = head;
        int position = 0;

        while (current != null && position < numElements) {

			if (current.getData() == element){
				return position;
			} else{
				current = current.getLink();
        	    position++;
				
			}

            
        }
		return -1;
	}
	/**
	 * Adds the specified element to the list at the given index
	 * Not possible for a full list
	 * @param			index - the position in the list to add the element
	 * @param			element - the element to be added to the list
	 */
	@Override
	public void add(int index, Type element){
		if (!isFull()){
			Node<Type> temp = head;
			int i = 0;

			while (i < index - 1 && temp != null){
				if (temp.getLink() ==null){
					break;
				}
				temp = (temp.getLink());
				i++;
			}

			if (isEmpty()){
				head = new Node<Type>();
				head.setData(element);
				current = head;
				tail = head;
				numElements++;
			}

			else if (!isEmpty()){
				if (index > numElements){
					return;
				} else if (index == 0){
					temp = head;
					head = new Node<Type>();
					head.setLink(temp);
					head.setData(element);
				} else {
					Node<Type> oldLink = temp.getLink();
					temp.setLink(new Node<Type>());
					temp = temp.getLink();
					temp.setLink(oldLink);
					temp.setData(element);
				}
			}
			numElements++;
		}
		}
	}
