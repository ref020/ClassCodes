public class FractionFun{
    public static void main(String[] args){
        Fraction f = new Fraction();
        System.out.println(f);
        f.setNumerator(5);
        f.setDenominator(10);
        System.out.println(f);

        Fraction f2 = new Fraction(8, 88);
        Fraction f3 = f.add(f2);
        System.out.println(f3); 
    }
}

class Fraction {
    private int numerator;
    private int denominator;
    
    //constructor
    public Fraction() {
        numerator = 0;
        denominator = 1;
    }

    //another constructor
    public Fraction(int n, int d){
        numerator = n;
        if (d != 0){
            denominator = d;
        } else{
            denominator = 1;
        }
        reduce();
    }

    //accessor
    public int getNumerator(){
        return numerator;
    }

    //mutator
    public void setNumerator(int val){
        numerator = val;
    }

    //accessor
    public int getDenominator(){
        return denominator;
    }

    //mutator
    public void setDenominator(int val){
        if (val != 0){
            denominator = val;
        }
    }

    public Fraction add(Fraction f){
        Fraction sum = new Fraction();

        sum.numerator = (numerator * f.denominator) + (f.numerator * denominator);
        sum.denominator = (denominator * f.denominator) + (f.denominator * denominator);
        sum.reduce();
        return sum;
    }

    private void reduce(){
        int gcd = 1;
        int min = Math.min(Math.abs(numerator), Math.abs(denominator));

        for (int i = 2; i <= min; i++){
            if (numerator % i ==0 && denominator % i == 0){
                gcd = i;
            }
        }

        numerator /= gcd;
        denominator /= gcd;

        if (numerator == 0) denominator = 1;
    }

    public String toString(){
        return numerator + "/" + denominator;
    }
}
