class exponent { 

    public static int recursivePower(int b, int p){
        if (p == 0){
            return 1;
        } 
        return b * recursivePower(b, p - 1);
    }
    public static void main(String[] args){
        
        int base = input("what is the base?");
        int power = input("What power are you raising to?");

        System.out.println(recursivePower(base, power));
    }
}