/*
Name: 		Ray Favaza
Date: 		10/1/23
Course: 	CSC 220 - Data Structures
*/

public class EasyList extends AbstractEasyList {
	/**
	 * Default constructor - constructs an empty list of initial capacity MAX_SIZE.
	 * end is set to -1 to indicate the list is empty.
	 */
	public EasyList() {
        list = new char[MAX_SIZE];
        end = -1;
	}

	/**
	 * Copy constructor - constructs an EasyList whose elements are copied from
	 * the given EasyList
	 * @param		el - EasyList to copy from
	 */
	public EasyList(EasyList el) {
		list = new char[MAX_SIZE];
        end = -1;
		for (int i = 0; i < MAX_SIZE; i++){
			list[i] = el.list[i];
			end++;
		}
	}

	/**
	 * Returns the number of elements in the list (not the max capacity)
	 * @return 		number of elements in list (use the end option to find wher ethe most recent element is)
	 */
	public int size() {
		return end + 1;
	}

	/**
	 * Returns a String representation of the list ("NULL" if empty)
	 * @return 		String representation of list
	 */
	public String toString() {
		//Return NULL if empty
        if(size() == 0)
        {
            return "Null";
        }

        //Otherwise, list each element seperated by a space
        else
        {
            String s = "";

            for(int i = 0; i < size(); i++)
            {
                s += list[i] + " ";
            }
            return s;
        }
    }

	/**
	 * Adds the specified element to the end of the list.
	 * Not possible for a full list.
	 * @param 		element - the element to be added to the list
	 */
	public void add(char element) {
        //only add the element if there is room
        if(size() < MAX_SIZE)
        {
            end++;
            list[end] = element;
        }
	}

	/**
	 * Adds the specified element at the specified position in the list.
	 * Elements are shifted to the right to make room.
	 * Not possible for a full list.
	 * @param 		index - the position in the list where the element will be added
	 * @param 		element - the element to be added to the list
	 */
	public void add(int index, char element) {
        if(size() < MAX_SIZE && index <= size())
        { 
        for(int i =end; i >= index; i --)
            {
                list[i + 1] = list[i]; 
            }
            list[index] = element;
            end ++;
        }
	}

	/**
	 * Returns the element at the specified index
	 * @param 		index - the position in the list of the element we are getting
	 * @return 		the element at index
	 */
	public char get(int index) {
		// if the index is in range, return the element
		if(index >= 0 && index < size())
		{
		return list[index];
		}
		//otherwise, return some default value
		//in reality, for a more robust implementation, throw an error
		else
		{
			return '6';
		}
	}

	/**
	 * Removes the element at the specified index.
	 * Elements are shifted to the left to fill in the space.
	 * Not possible for an empty list.
	 * @param 		index - the position in the list of the element we are removing
	 */
	public void remove(int index) {
		//Only remove if list is not empty and index is in bounds
		if(size()> 0 && index >= 0 && index< size())
		{
			for(int i = index; i<end; i++)
			{
				list[i] = list[i+1];
			}
			end --;
		}
	}
 
	/**
	 * Replaces the element at the specified index with the element.
	 * Not possible for an empty list.
	 * @param 		index - the position in the list of the element we are replacing
	 * @param 		element - the element replacing the existing element at index
	 */
	public void set(int index, char element) {
		if(size() >0 && index >= 0 && index < size())
		{
			list[index] = element;
		}
	}

	/**
	 * Returns the index of the first occurrence of the specified element.
	 * Returns -1 if the list does not contain the element.
	 * @param 		element - the element being searched for
	 * @return 		the index of element, or -1 if it doesn't exist
	 */
	public int indexOf(char element) {
		for(int i =0; i<size(); i++)
		{
			if(list[i] == element)
			{
				return i;
			}
		}

		return -1;
	}

	/**
	 * Sorts the list in ascending order using insertion sort.
	 */
	public void sort() {
		int n = size();
		int i;
		char key;
        for (i = 1; i < n; i++) {
            key = list[i];
            int j = i - 1;
 
            /* Move elements of list[0..i-1], that are
               greater than key, to one position ahead
               of their current position */
            while (j >= 0 && list[j] > key) {
                list[j + 1] = list[j];
                j = j - 1;
            }
            list[j + 1] = key;
    }
	}
	public boolean isFull(){
		if (size() == MAX_SIZE){
			return true;
		} else{
			return false;
		}
	}
	public boolean isEmpty(){
		if (size() == 0){
			return true;
		} else{
			return false;
		}
	}
	
}