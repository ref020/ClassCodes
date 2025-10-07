import java.util.Random;
import java.util.Scanner;

public class SortSearch {
static final int MIN = 10;
static final int MAX = 99;

    public static void main(String [] args) {
        int[] values = new int[15];
        Random r = new Random();
        Scanner s = new Scanner(System.in);
        int num;          //value to search for
        int index;        //specified value's index

        for (int i = 0; i < values.length; i++){
            values[i] = r.nextInt(MAX - MIN + 1) + MIN;
        }
        System.out.print("Not Sorted: ");
        printArray(values);

        sortArray(values);
        System.out.print("Sorted: ");
        printArray(values);

        System.out.println("Value to search for? ");
        num = s.nextInt();
        System.out.println("Searching for " + num);
        index = searchArray(values, num);
        System.out.println("Value: ");
        if (index == -1){
            System.out.println("Not found");
        } else {
            System.out.println("Found at index" + index + "!");
        }
    }

    public static void printArray(int[] list){
        for (int i = 0; i < list.length; i++){
            System.out.print(list[i] + " ");
        }
        System.out.println();
    }

    public static void sortArray(int[] list){
        for (int i = 0; i < list.length; i++){
            int minPos = i;
            for (int j = i + 1; j < list.length; j++){
                if (list[j] < list[minPos]){
                    minPos = j;
                }
            }
        int temp = list[i];
        list[i] = list[minPos];
        list[minPos] = temp;
        }
    }

    public static int searchArray(int[] list, int val){
        int first = 0;
        int last = list.length - 1;
        
        while (first <= last){
            int mid = (first + last) / 2;

            if (val == list[mid]){
                return mid;
            } else if (val > list[mid]){
                first = mid + 1;
            } else{
                last = mid - 1;
            }
        }
        return -1;
    }
}
