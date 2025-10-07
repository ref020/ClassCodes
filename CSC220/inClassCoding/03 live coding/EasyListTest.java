import java.util.ArrayList;
import java.util.Random;

public class EasyListTest {
    public static void main (String[] args){ 
        
        EasyList student = new EasyList();
        Random r = new Random();
        ArrayList<Character> letters = new ArrayList<Character>();
        for (char c = 'A'; c != '['; c++) letters.add(c);
        for (int i = 0; i < 10; i++) student.add(letters.remove(r.nextInt(letters.size())));
        
        // Test student copy constructor
        AbstractEasyList studentCopy = new EasyList(student);
        System.out.println("The original list: " + student);
        System.out.println("Your copied list: " + studentCopy);

    }
}

