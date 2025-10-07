/*
Name:     	Ray Favaza
Date:       11/1/23
Course:     CSC 220 - Data Structures
*/

import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;

public class Sort extends AbstractSort {

	public static void main(String[] args) {
/*		
		Sort s = new Sort();
		int[] quickArray = s.generateRandomArray(10, 1);
		int[] quizArray = {17, 48, 44, 93, 19, 85, 99, 87};

		//quick Sort
		System.out.println("### Testing Quick Sort");
		System.out.println("Initial Array" + Arrays.toString(quizArray));
		s.quickSort(quizArray);
		System.out.println("Sorted Array" + Arrays.toString(quizArray));


		Sort s2 = new Sort();
		//int[] shellArray = s2.generateRandomArray(10, 1);
		int[] quizShellArray = {79, 48, 67, 1, 43, 0, 77, 26};

		//quick Sort
		System.out.println("### Testing Shell Sort");
		System.out.println("Initial Array" + Arrays.toString(quizShellArray));
		s2.shellSort(quizShellArray, 3);
		System.out.println("Sorted Array" + Arrays.toString(quizShellArray));
*/
		Heap h = new Heap();
		int[] heapArray = {22, 19};
		for (int i : heapArray){
			h.add(i);
			System.out.println("" + h.toString());
		}
		h.maxHeapifyUp();
		System.out.println("" + h.toString());

	}

	/**
	 * Returns an array of random integers between 0-99 given a size and seed
	 * @param 			size - the desired size of the array being generated
	 * @param 			seed - the seed used to initialize the random number generator
	 * @return 			an array of random integers between 0-99 (without duplicates)
	 */
	public int[] generateRandomArray(int size, int seed) {
		Random r = new Random(seed);
		
		//create choices bank
		ArrayList<Integer> bank = new ArrayList<Integer>();
		for (int i = 0; i < 100; i++){
			bank.add(i);
		}

		//fill an array with random selections from choices bank
		int[] array = new int[size];
		for (int i = 0; i < size; i++){
			array[i] = bank.remove(r.nextInt(bank.size()));
		}

		return array;
	}

	/**
	 * Public interface to the quick sort algorithm. 
	 * @param 			array - the array of integers to sort
	 */
	public void quickSort(int[] array) {
		quickSort(array, 0, array.length - 1);
	}

	/**
	 * Recursive quickSort algorithm.  This version always chooses the first element as the pivot,
	 * but this is not the only or best method for choosing a pivot!
	 * Uses the private quickSort method to do the sorting.
	 * @param 			array - the array of integers to sort
	 * @param			first - the index of the first element in the current subarray being sorted
	 * @param			last - the index of the last element in the current subarray being sorted
	 */
	private void quickSort(int[] array, int first, int last) {
		//chose a pivot number and a position for the left and right cursors
		int pivot = array[first];
		int leftCursor = first + 1;
		int rightCursor = last + 1;

		//search for swaps until cursors meet
		while (leftCursor != rightCursor){
			//search for a value larger than the pivot with the left cursor
			while (leftCursor != rightCursor){
				if (array[leftCursor] > pivot){
					break;
				}
				leftCursor++;
			}

			//search for a value smaller than the pivot with the right cursor
			while (leftCursor != rightCursor){
				rightCursor--;
				if (array[rightCursor] < pivot){
					break;
				}
			}

			//swap values if cursors haven't met
			if (leftCursor != rightCursor){
				int temp = array[leftCursor];
				array[leftCursor] = array[rightCursor];
				array[rightCursor] = temp;
			}
		}

		//swap pivot with the value at the cursors
		array[first] = array[leftCursor - 1];
		array[leftCursor - 1] = pivot;
System.out.println("" + Arrays.toString(array));
		//recursively sort the subarray to the left of the cursors
		if ((leftCursor - 2) - first > 0){
			
			quickSort(array, first, leftCursor - 2);
		}

		//recursively sort the subarray to the left of the cursors
		if (last - rightCursor > 0){
			quickSort(array, rightCursor, last);
		}
		
	}

	/**
	 * The shell sort algorithm.
	 * @param			array - the array of integers to sort
	 * @param			k - the spacing counter used by shell sort
	 */
	public void shellSort(int[] array, int k) {
		while (k > 0){
			for (int i = 0; i < k; i++){
				insertionSort(array, k, i);
				System.out.println("" + Arrays.toString(array));
		}
		k--;
		  }
		  
		  
	}

	public static void insertionSort(int[] array, int k, int startIndex){
		for (int i = startIndex + k; i < array.length; i += k){
			int key = array[i];
			int j = i - k;

			while (j >= startIndex && array[j] > key){
				array[j + k] =array[j];
				j -= k;
			}

			array[j+k] = key;
		}
	}

	/**
	 * The heap sort algorithm.
	 * @param			array - the array of integers to sort
	 */
	public void heapSort(int[] array) {
		int len = array.length;
		Heap heap = new Heap();

		for (int value : array){
			heap.add(value);
		}

		for (int i = 0; i <len; i++){
			int max = heap.getMax();
			System.out.println("" + Arrays.toString(array));
			array[i] = max;
		}
		
		int[] temp = new int[len];
		int j = len;
		for (int i = 0; i < len; i++){
			temp[j - 1] = array[i];
			j = j - 1;
			
		}

		for (int i = 0; i < len; i++){
			array[i] = temp[i];
		}
	}
}