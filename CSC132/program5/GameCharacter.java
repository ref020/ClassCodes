public class GameCharacter {
    
    public static void main(String[] args){
        GameCharacter c = new GameCharacter();
        System.out.println(c);
    }
    
    
    private String name;
    private int lives;
    private String[] inventory;
    private static final int MAXLIVES = 5;

    //constructor
    public GameCharacter() {
        name = "Sam Sung";
        lives = MAXLIVES;
        inventory = new String[5];
    }
    
    //overload constructor
    public GameCharacter(String n, int l){
        name = n;
        lives = l;
        setLives(l);
        inventory = new String[5];
    }

    //name getter
    public String getName(){
        return name;
    }

    //name setter
    public void setName(String n){
        name = n;
    }

    //lives getter
    public int getLives(){
        setLives(lives);
        return lives;
    }

    //lives setter
    public void setLives(int l){
        if(l > MAXLIVES || l < 0){
            lives = MAXLIVES;
        } else {
            lives = l;
        }
    }

    //inventory getter
    public String[] getInventory(){
        return inventory;
    }

    //inventory setter
    public void setInventory(String[] inv){
        inventory = inv; 
    }

    public Boolean isAlive(){ 
        if (lives > 0){
            return true;
        } else {
            return false;
        }
    }

    public Boolean hasWeapon(){
        for (int i = 0; i < inventory.length; i++){
            if (inventory[i] == "knife" || inventory[i] == "gun"){
                return true;
            } 
        }
        return false;
    }

    public int sizeOfInventory(){
        int counter = 0;
        for (int i = 0; i < inventory.length; i++){
            if (inventory[i] != null){
                counter += 1;
            }
        }
        return counter;
    }

    public void heal(){
        lives = MAXLIVES;
    }

    public void damage(){
        if(lives > 0){
        lives -= 1;
        }
    }

    public void pickUp(String item){
        if (sizeOfInventory() < 5){
            for (int i = 0; i < inventory.length; i++){
                if (inventory[i] == null){
                    inventory[i] = item;
                    break;
                }
            }
        }
    }

    public void drop(String item){
            for (int i = 0; i < 5; i++){
                if (inventory[i] == item){
                    inventory[i] = null;
                    break;
                }
            }
        }
    
    public static String printArray(String[] list){
        String inv = "";
        for (int i = 0; i < list.length; i++){
            if ((list[i]) != null){
                inv = inv + list[i] + ","+ " ";            
            }
        }
        return inv;
    }
        
    public String toString(){
        return "Name:" + name + "\nLives: " + lives+ "\nInventory: " + printArray(inventory)+ "\n";
    }
}
