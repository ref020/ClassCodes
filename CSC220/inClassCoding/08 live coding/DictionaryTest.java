import java.util.ArrayList;
import java.util.Random;

public class DictionaryTest {
    public static void main(String[] args){
        AbstractDictionary prof = new Dictionary();
        AbstractDictionary student = new Dictionary();
        Random r = new Random();
        ArrayList<String> keyBank = new ArrayList<String>();
        keyBank.add("aa"); keyBank.add("ab"); keyBank.add("ac"); keyBank.add("ad");
        keyBank.add("ba"); keyBank.add("bb"); keyBank.add("bc"); keyBank.add("bd");
        keyBank.add("ca"); keyBank.add("cb"); keyBank.add("cc"); keyBank.add("cd");
        keyBank.add("da"); keyBank.add("db"); keyBank.add("dc"); keyBank.add("dd");
        // Test adding when empty
        System.out.println("--- subtest: adding when empty ---");
        String key = keyBank.remove(r.nextInt(keyBank.size()));
        double value = (double)r.nextInt(100);
        prof.add(key, value);
        System.out.println("Expected:\n" + prof);
        student.add(key, value);
        System.out.println("Your Answer:\n" + student);
        // Test adding until full
        System.out.println("--- subtest: adding until full ---");
        for (int i = 1; i < prof.MAX_SIZE; i++) {
        key = keyBank.remove(r.nextInt(keyBank.size()));
        value = (double)r.nextInt(100);
        prof.add(key, value);
        student.add(key, value);
        }
        System.out.println("Expected:\n" + prof);
        System.out.println("Your Answer:\n" + student);
        /*// Test adding when full
        System.out.println("--- subtest: adding when full ---");
        key = keyBank.remove(r.nextInt(keyBank.size()));
        value = (double)r.nextInt(100);
        prof.add(key, value);
        System.out.println("Expected:\n" + prof);
        student.add(key, value);
        System.out.println("Your Answer:\n" + student);*/
    }
}
