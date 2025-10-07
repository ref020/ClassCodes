/*
Name: 		[Ray Favaza]
Date: 		[9/20/23]
Course: 	CSC 220 - Data Structures
*/

public class ComplexityAnalyzer extends AbstractComplexityAnalyzer {
	//math functions
	static double log2(double in){
		return (Math.log(in)) / (Math.log(2));
	}
	/**
	 * Returns a String containing the names of the functions that could have
	 * possibly generated the output given the input
	 * @param 		input number
	 * @param 		output number
	 * @return 		names of possible functions
	 */
	public String analyzeComplexity(double input, double output) {

		//creates an empty string
		String result = "";
		
		if (output == 1){
			result += "Constant, ";
		}

		if (output == log2(input)){
			result += "Logarithmic, ";
		}

		if (output % input == 0){
			result += "Linear, ";
		}

		if (output == input*(log2(input))){
			result += "Quasi-Linear, ";
		}

		if (Math.pow(input, 2) == output){
			result += "Quadratic, ";
		}

		if (Math.pow(input, 3) == output){
			result += "Cubic, ";
		}

		if (Math.pow(2, input) == output){
			result += "Exponential, ";
		}

		result = result.substring(0, (result.length()-2));


		return result;
	}
}