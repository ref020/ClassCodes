import java.util.ArrayList;
import java.util.Random;

public class HeapTest {
        
    public static void main(String[] args){
        AbstractHeap result = new Heap();
AbstractHeap student = new Heap();
Random r = new Random();
for (int i = 0; i < 5; i++) {
// Prep the solution heap and initialize student heap
ArrayList<Integer> nums = new ArrayList<Integer>();
for (int j = 0; j < 10; j++) nums.add(j);
while (nums.size() > 0) result.add(nums.remove(r.nextInt(nums.size())));
System.out.println("--- subtest " + (i+1) + " ---");
System.out.println("Heap: " + result);
ArrayList<Integer> swapNums = new ArrayList<Integer>();
for (int j = 0; j < 10; j++) swapNums.add(j);
int num1 = swapNums.remove(r.nextInt(swapNums.size()));
int num2 = swapNums.remove(r.nextInt(swapNums.size()));
System.out.println("Swapping indices " + num1 + " and " + num2);
result.swap(num1, num2);
System.out.println("Expected: " + result);
student.swap(num1, num2);
System.out.println("Your Answer: " + student);
}

    }
}
