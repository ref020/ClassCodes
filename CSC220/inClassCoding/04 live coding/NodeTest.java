/*
Name:		[Your Name Here]
Date:		[Current Date Here]
Course:		CSC 220 - Data Structures
*/

public class NodeTest {
	public static void main(String[] args) {
                testAdd();
	}

	public static void testNode() {
                //Create nodes
                Node<String> n1 = new Node<String>();
                Node<String> n2 = new Node<String>();
                Node<String> n3 = new Node<String>();
                Node<String> n4 = new Node<String>(); //can build or set data, build or set a link

                //Put some data into the nodes
                n1.setData("one");
                n2.setData("two");
                n3.setData("three");
                n4.setData("four");

                //Access data stored in a node
                System.out.println("Node 1 contains" + n1.getData());

                // Link two nodes together
                n1.setLink(n2);
                
                //Access the data stored in one node using another node
                System.out.println("Node 2 contains" + n1.getLink().getData());

                //Link the remaining nodes together
                n2.setLink(n3);
                n3.setLink(n4);

                // Iterate through a chain of nodes
                Node<String> currentNode = n1;  //shallow copy of node because there is a reference to the same object
                /* 
                for(int i =0; i<= 4; i++)
                {
                        System.out.println("Node" + i + "contains" + currentNode.getData());
                        currentNode = currentNode.getLink();
                        if(currentNode == null)
                        {
                                break;
                        }
                }
                */
                int i =1;
                while(currentNode.getLink() != null)
                {
                        System.out.println("Node" + i + "contains" + currentNode.getData());
                        currentNode = currentNode.getLink();
                        i ++;
                }
                System.out.println("Node" + i + "contains" + currentNode.getData());
	}

	public static void testAdd() {
                System.out.println("Testing the add() method");
                LinkedList<String> list = new LinkedList<String>();

                //Test printing an empty list
                        System.out.println(list);
                
                //Test adding a single element to the list
                list.add("One");
                System.out.println(list);

                //Test that the method won't add more nodes when the list is full
                for(int i = 0; i < 20; i++)list.add("more");
                System.out.println(list);
        
        }


	public static void testGet() {

	}

	public static void testGetFirst() {

	}

	public static void testGetLast() {

	}

	public static void testIteration() {

	}
}