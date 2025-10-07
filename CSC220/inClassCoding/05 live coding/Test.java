/*
Name:		[Your Name Here]
Date:		[Current Date Here]
Course:		CSC 220 - Data Structures
*/

import java.util.Random;

public class Test {
	public static void main(String[] args) {
		AbstractInfixToPostfix test = new InfixToPostfix();
		AbstractInfixToPostfix student = new InfixToPostfix();
		Random r = new Random();
		String[] expressions = new String[] {(r.nextInt(9)+1) + " + " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " * " + (r.nextInt(9)+1) + " + " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " ^ " + (r.nextInt(9)+1) + " - " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " * " + (r.nextInt(9)+1) + " - ( " + (r.nextInt(9)+1) + " - " + (r.nextInt(9)+1) + " / " + (r.nextInt(9)+1) + " )",(r.nextInt(9)+1) + " ^ " + r.nextInt(4) + " ^ " + r.nextInt(3),"( " + (r.nextInt(9)+1) + " + ( " + (r.nextInt(9)+1) + " - " +(r.nextInt(9)+1) + " ) * ( " +(r.nextInt(9)+1) + " - " + (r.nextInt(9)+1) + " ) * " + (r.nextInt(9)+1) + ")"};
		for (int i = 0; i < expressions.length; i++) {
			String infixStr = expressions[i];
			String[] infixExp = test.parseExpression(infixStr);
			String[] postfixExp = test.infixToPostfix(infixExp);
			String postfixStr = test.expressionToString(postfixExp);
			System.out.println("--- subtest " + (i+1) + " ---");
			System.out.println("Infix: " + infixStr);
			System.out.println("Postfix: " + postfixStr);
			String[] resultExp = student.infixToPostfix(infixExp);
			String result = test.expressionToString(resultExp);
			System.out.println("Your Answer: " + result);
		}


	}

/*
	public static void testEvaluate() {
		AbstractInfixToPostfix student = new InfixToPostfix();
		Random r = new Random();
		String[] expressions = new String[] {
		(r.nextInt(9)+1) + " + " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " - " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " * " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " / " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " ^ " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " * " + (r.nextInt(9)+1) + " + " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " ^ " + (r.nextInt(9)+1) + " - " + (r.nextInt(9)+1),(r.nextInt(9)+1) + " * " + (r.nextInt(9)+1) + " - ( " + (r.nextInt(9)+1) + "- " + (r.nextInt(9)+1) + " / " + (r.nextInt(9)+1) + " )",(r.nextInt(9)+1) + " ^ " + r.nextInt(4) + " ^ " + r.nextInt(3)};
		for (int i = 0; i < expressions.length; i++) {
			String infixStr = expressions[i];
			System.out.println("--- subtest " + (i+1) + " ---");
			System.out.println("Postfix: " + postfixStr);
			System.out.println("Expected: " + solution);
			String result = student.evaluatePostfix(postfixExp);
			System.out.println("Your Answer: " + result);
		}
	}*/
}