/*
Name:     	[Your Name Here]
Date:       [Current Date Here]
Course:     CSC 220 - Data Structures
*/

public class Dictionary extends AbstractDictionary {
	/**
	 * Default Constructor
	 */
	public Dictionary() {
		hashTable = new KVPair[MAX_SIZE];
		DELETED = new KVPair("Deleted", 0.0);
		numKVPairs = 0;
	}

	// Returns true if the Dictionary is empty or full, respectively
	public boolean isFull(){
		return (numKVPairs == MAX_SIZE);
	}

	public boolean isEmpty(){
		return (numKVPairs == 0);
	}

	/**
	 * Returns the number of key-value pairs in the dictionary
	 * @return 			the number of key-value pairs
	 */
	public int getSize() {
		return numKVPairs;
	}

	/**
	 * Returns a vertical string representation of the dictionary's hash table
	 * This includes null and deleted KVPairs
	 * @return 			String representation of the dictionary's hash table
	 */
	public String toString() {
		String s = "";
		for (KVPair kvp : hashTable){
			if (kvp == null){
				s += "-NULL-\n";
			} else if (kvp == DELETED){
				s += "-DELETED-\n";
			} else {
				s += kvp + "\n";
			}
		}
		
		return s;
	}

	/**
	 * Adds the key and value given to the dictionary as a KVPair by storing it in its proper position
	 * in the backend hash table.  Uses open addressing with linear probing to handle collisions.
	 * @param			key - the key of the KVPair to be added to the dictionary
	 * @param			value - the value of the KVPair to be added to the dictionary
	 */
	public void add(String key, double value) {
		if(isFull()){
			return;
		}
		
		int preHashValue = preHash(key);
		int hashValue = hashFunction(preHashValue);

		//System.out.println("e");
		if((hashTable[hashValue] == DELETED) || (hashTable[hashValue] == null)){
			hashTable[hashValue] = new KVPair(key, value);
			numKVPairs++;
			//System.out.println("d");		
		}
		else{
			int current = (hashValue + 1) % MAX_SIZE;
			//System.out.println("a");
			while(current != hashValue){
				//System.out.println("b");
				if(hashTable[current] == null || hashTable[current] == DELETED){
					//System.out.println("c");
					hashTable[current] = new KVPair(key, value);
					numKVPairs++;
					break;
				}
		
			current = (current + 1) % MAX_SIZE;
			}
		}
	}

	/**
	 * Returns the value stored in the Dictionary for the given key
	 * @param			key - the key of the KVPair to lookup in the dictionary
	 * @return 			the value of the KVPair containing key
	 */
	public double get(String key) {
		int preHashValue = preHash(key);
		int hashValue = hashFunction(preHashValue); 

		int current = hashValue;
		
		for(int i = 0; (i < MAX_SIZE && hashTable[current] != null); i++){
			if (hashTable[current] != DELETED && hashTable[current].getKey().equals(key)) {
				return hashTable[current].getValue();	
			}

			current = (current + 1) % MAX_SIZE;
		}
		return 0.0;
	}

	/**
	 * Removes the KVPair associated with the given key
	 * @param			key - the key of the KVPair to remove from the dictionary
	 */
	public void remove(String key) {
		int preHashValue = preHash(key);
		int hashValue = hashFunction(preHashValue); 
	
		int current = hashValue;

		for(int i = 0; (i < MAX_SIZE && hashTable[current] != null); i++){
			if (hashTable[current] != DELETED && hashTable[current].getKey().equals(key)) {
				hashTable[current] = DELETED;
				numKVPairs--;
				return;	
			}
			current = (current + 1) % MAX_SIZE;
		}
	}

	public int preHash(String word){
		int sum = 0;
		int index = 0;
		char[] ch = word.toCharArray();
		for(int i = 0; i < ch.length; i++){
			index = (int) ch[i];
			sum += index;
		}
		return sum;
	}

	public int hashFunction(int preHashValue){
		return preHashValue % MAX_SIZE;
	}
}