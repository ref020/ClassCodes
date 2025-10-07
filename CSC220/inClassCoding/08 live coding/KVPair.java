/*
Name:     	[Your Name Here]
Date:       [Current Date Here]
Course:     CSC 220 - Data Structures
*/

public class KVPair {
	private String key;
	private double value;
	/**
	 * Constructor
	 * @param			k - the key to store in the KVPair
	 * @param			v - the value to store in the KVPair
	 */
	public KVPair(String k, double v) {
		key = k;
		value = v;
	}

	// Getter and setter methods
	public String getKey(){
		return key;
	}

	public double getValue(){
		return value;
	}

	public void setValue(double v){
		value = v;
	}

	/**
	 * Returns the string representation of the key/value pair
	 * @return 			the String representation of the KVPair
	 */
	public String toString() {
		return key + " | " + value;
	}
}