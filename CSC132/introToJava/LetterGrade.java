public class LetterGrade {
    public static void main(String[] args){
        double score = 87.5;
        char LetterGrade;

        LetterGrade = calcGrade(score);
        System.out.println("Your grade is " + LetterGrade);
    }

    public static char calcGrade(double numericScore){
        if (numericScore >= 90){
            return 'A';    
        }
        else if (numericScore >= 80){
            return 'B';
        }
        else if (numericScore >= 70){
            return 'C';
        }
        else if (numericScore >= 60){
            return 'D';
        }
        else {
            return 'F';
        }
    }
}
