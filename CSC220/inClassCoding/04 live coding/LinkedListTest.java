import java.util.ArrayList;
import java.util.Random;

public class LinkedListTest{
   
    
    public static void main(String[] args){
    AbstractLinkedList<Character> test = new LinkedList<Character>();
    Random r = new Random();
    // Create array list of letters from A to Z
    ArrayList<Character> letters = new ArrayList<Character>();
    for (char c = 'A'; c != '['; c++) letters.add(c);
    // Copy the test list into the student list
    // Test adding letter to empty list
    char c = letters.remove(r.nextInt(letters.size()));
    test.add(0, c);
    System.out.println("--- subtest 1: adding a letter to an empty list ---");
    System.out.println("Correct list = " + test);
    // Test adding letter out of bounds
    c = letters.remove(r.nextInt(letters.size()));
    test.add(2, c);
    System.out.println("--- subest 2: adding a letter at index 2 (out of bounds) ---");
    System.out.println("Correct list = " + test);
    // Test adding letter to beginning
    c = letters.remove(r.nextInt(letters.size()));
    test.add(0, c);
    System.out.println("--- subtest 3: adding a letter to the beginning of the list(index 0) ---");
    System.out.println("Correct list = " + test);
    
    // Test adding letter to middle
    
    c = letters.remove(r.nextInt(letters.size()));
    test.add(1, c);
    System.out.println("--- subtest 4: adding a letter to the middle of the list(index 1) ---");
    System.out.println("Correct list = " + test);
    
    // Test adding letter to end
    c = letters.remove(r.nextInt(letters.size()));
    test.add(3, c); 
    System.out.println("--- subtest 5: adding to the end of the list (index 3) ---");
    System.out.println("Correct list = " + test);
    
    // Test adding letter to full list
    for (int i = 0; i < 6; i++) test.add(letters.remove(r.nextInt(letters.size())));
    c = letters.remove(r.nextInt(letters.size()));
    test.add(9, c);
    System.out.println("--- subtest 6: fill the list with letters, then try to addanother (index 9) ---");
    System.out.println("Correct list = " + test);
    
            
        }
}