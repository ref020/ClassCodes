/*
Name:       [Your Name Here]
Date:       [Current Date Here]
Course:     CSC 220 - Data Structures
*/

public class Heap extends AbstractHeap {
   /* /**
     * Default constructor - initializes data to have a size equal to maxi_SIZE
     */
    public Heap() {
        data = new int[MAX_SIZE];
    }
    
    // Methods for getting the index of a node's left child, right child, or parent
    protected int getLeftIndex(int index){
        return 2 * index + 1;
    }

    protected int getRightIndex(int index){
        return 2 * index + 2;
    }

    protected int getParentIndex(int index){
        return (index-1)/2;
    }
    
    // Methods for getting the data stored at some index in the heap
    protected int getLeftData(int index){
        return data[getLeftIndex(index)];
    }

    protected int getRightData(int index){
        return data[getRightIndex(index)];
    }
    protected int getParentData(int index){
        return data[getParentIndex(index)];
    }

    // Methods for checking if a node has a left child, right child, or parent
    protected boolean hasLeft(int index){
        return getLeftIndex(index) < size;
    }

    protected boolean hasRight(int index){
        return getRightIndex(index) < size;
    }

    protected boolean hasParent(int index){
        return getParentIndex(index) >= size;
    }
    // Checks if the heap is empty/full
    public boolean isEmpty(){
        return size == 0;
    }

    public boolean isFull(){
        return size == MAX_SIZE;
    }
    /**
     * Returns the String representation of the heap
     * @return          the heap as a String
     */
    public String toString() {
        String s = "";
        for (int i = 0; i < size; i++){
            s += data[i] + " ";
        }
        return s.trim();
    }
    
    /**
     * Swap the data stored at two different indices in the heap
     * @param           index0 - the index whose data will be swapped with the data at index1
     * @param           index1 - the index whose data will be swapped with the data at index0
     */
    public void swap(int index0, int index1) {
        int temp = data[index0];
        data[index0] = data[index1];
        data[index1] = temp;
    }
    
    /**
     * Adds a new node to the heap
     * @param           element - the data to add to the heap
     */
    public void add(int element) {
        if(!isFull()){
            data[size] = element;
            size++;
            maxHeapifyUp();   
        }
        return;
    }

    /**
     * Removes and returns the data stored at the root (index 0)
     * @return          the data stored at the root
     */
    public int getMax() {
        if(!isEmpty()){
            int maxi = data[0];

            swap(0, size-1);

            size--;

            maxHeapifyDown();

            return maxi;
        }
        return -1;
    }
    
    /**
     * Restores the heap property by repeatedly swapping the last leaf node up the heap until properly positioned
     */
    public void maxHeapifyUp() {
        int current = size - 1;

        while (current > 0 && data[current] > data[getParentIndex(current)]){
            swap(current, getParentIndex(current));
            current = getParentIndex(current);
        }
    
    }
    
    /**
     * Restores the heap property by repeatedly swapping the root node down the heap until properly positioned
     */
    public void maxHeapifyDown() {
        int index = 0;
        while(true){
            int maxi = index;
            int right = getRightIndex(index);
            int left = getLeftIndex(index);

            if (left < size && data[left] > data[maxi]){
                maxi = left;
            }

            if (right < size && data[right] > data[maxi]){

                maxi = right;
            }

            if (index == maxi){
                break;
            }

            swap(index, maxi);

            index = maxi;
        }
    }
}
