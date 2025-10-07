/*
Name:		[Your Name Here]
Date:		[Current Date Here]
Course:		CSC 220 - Data Structures
*/


public class InfixToPostfix extends AbstractInfixToPostfix {
	/**
	 * Evaluate the result of two String operands (a & b) and a String operator and return the result as a String
	 * @param 			a - the first operand
	 * @param 			b - the second operand
	 * @param 			operator - the operator
	 * @return 			The result of "a operator b"
	 */
	public String evaluate(String a, String b, String operator) {
		//parse the opperands
		int numA;
		int numB;
		try{
			numA = Integer.parseInt(a);
			numB = Integer.parseInt(b);
		} catch(NumberFormatException e){
			System.out.println("Invalid operand found during evaluation:");
			System.out.println("\ta=" + a + ", b=" + b);
			return null;
		}
		if (operator.equals("+")){
			return ("" + (int)(numA + numB));
		} else if (operator.equals("-")){
			return ("" + (int)(numA - numB));
		} else if (operator.equals("*")){
			return ("" + (int)(numA * numB));
		} else if (operator.equals("/")){
			return ("" + (int)(numA / numB));
		} else if (operator.equals("^")){
			return ("" + (int)(Math.pow(numA, numB)));
		} else {
			System.out.println("Invalid operator found during evaluation");
			return null;
		}
	}

	/**
	 * Returns true if the given token is an integer
	 * @param 			token - the token to test
	 * @return 			true if token is an integer, false otherwise
	 */
	public boolean isOperand(String token) {
		try{
			Integer.parseInt(token);
			return true;
		} catch(NumberFormatException e){
			return false;
		}
	}

	/**
	 * Returns the infix ranking of the given operator, or 0 by default
	 * @param 			operator - the operator to analyze
	 * @return 			the infix rank of operator
	 */
	public int infixOpRank(String operator) {
		if (operator.equals("(")){
			return 4;
		} else if (operator.equals("^")){
			return 3;
		} else if (operator.equals("*") || (operator.equals("/"))){
			return 2;
		} else if (operator.equals("+") || (operator.equals("-"))){
			return 1;
		} else {
			return 0;
		}
	}

	/**
	 * Returns the operator stack ranking of the given operator, or 0 by default
	 * @param			operator - the operator to analyze
	 * @return 			the operator stack rank of operator
	 */
	public int opStackRank(String operator) {
		if (operator.equals("^")){
			return 2;
		} else if (operator.equals("*") || (operator.equals("/"))){
			return 2;
		} else if (operator.equals("+") || (operator.equals("-"))){
			return 1;
		} else {
			return 0;
		}
	}

	/**
	 * Separates a space separated mathematical expression in String representation
	 * and returns an array of Strings containing the individual elements
	 * @param 			expressionString - the expression in String format to separate
	 * @return 			An array of the operands and operators in expressionString
	 */
	public String[] parseExpression(String expressionString) {
		return expressionString.split(" ");
	}

	/**
	 * Returns the string representation of an expression
	 * @param			expression - an array of operands and operators forming a mathematical expression
	 * @return 			expression as a single, space separated String
	 */
	public String expressionToString(String[] expression) {
		String expString = "";
		if (expression.length > 0){
			for (int i = 0; i < expression.length - 1; i++){
				expString += expression[i] + " ";
			}
			expString += expression[expression.length - 1];
		}
		return expString;
	}

	/**
	 * Evaluate a postfix expression
	 * Integers only, so the division operation is integer division (no remainder from division)
	 * @param 			postfixExpression - the postfix expression to evaluate
	 * @return 			The result from evaluating postfixExpression
	 */
	public String evaluatePostfix(String[] postfixExpression) {
		Stack<String> s = new Stack<String>();

		for(int i = 0; i < postfixExpression.length; i++){
			if (isOperand(postfixExpression[i])){
				s.push(postfixExpression[i]);
			} else if (!isOperand(postfixExpression[i])){
				String num1 = s.pop();
				String num2 = s.pop();
				s.push(evaluate(num2, num1, postfixExpression[i]));
			}
		}
		return s.pop();
	}

	/**
	 * Convert an infix expression to a postfix expression
	 * @param 			infixExpression - the infix expression to convert to postfix
	 * @return 			The postfix expression representation of infixExpression
	 */
	public String[] infixToPostfix(String[] infixExpression) {
		Queue<String> infixQ = new Queue<String>();

		for(String token: infixExpression){
			infixQ.add(token);
		}

		Queue<String> postfixQ = new Queue<String>();
		Stack<String> operatorS = new Stack<String>();

		while(infixQ.peek() != null){
			String token = infixQ.dequeue();
			//testchecker(infixQ, postfixQ, operatorS, 158);
			if (isOperand(token)){
				postfixQ.enqueue(token);
				//testchecker(infixQ, postfixQ, operatorS, 161);
			}else if (token != null && token.equals(")")){
				String op = operatorS.pop();
				//testchecker(infixQ, postfixQ, operatorS, 164);
				while (!op.equals("(")){
					postfixQ.enqueue(op);
					op = operatorS.pop();
				}
				//testchecker(infixQ, postfixQ, operatorS, 169);
			} else {
				String op = operatorS.peek();
				//testchecker(infixQ, postfixQ, operatorS, 172);
				while (op != null && token != null && opStackRank(op) >= infixOpRank(token)){
					op = operatorS.pop();
					postfixQ.enqueue(op);
					op = operatorS.peek();
				}
				//testchecker(infixQ, postfixQ, operatorS, 178);
				operatorS.push(token);
				//testchecker(infixQ, postfixQ, operatorS,180);
			}
		}
		while (operatorS.peek() != null){
			String op = operatorS.pop();
			postfixQ.enqueue(op);
		}
		//testchecker(infixQ, postfixQ, operatorS, 187);
		// Convert the Queue<String> to a String[]
    	String[] postfixArray = new String[postfixQ.size()];
    	int i = 0;
    	while (postfixQ.peek() != null) {
        	postfixArray[i] = postfixQ.dequeue();
        	i++;
    	}
		return postfixArray;
	}
	/*public void testchecker(Queue<String> a, Queue<String> b, Stack<String> c, int ln){
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(ln);
	}*/
}