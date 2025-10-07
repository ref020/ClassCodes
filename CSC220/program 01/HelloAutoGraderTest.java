class HelloAutoGraderTest{
    public static void main(String [] args){
        AbstractHelloAutograder student = new HelloAutograder();
        System.out.println("Expected: Hello Autograder!");

        System.out.println("Actual: " + student.sayHello());

    }
}