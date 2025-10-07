class inputcase {
    public static void main (String[] args){
        int [] nums = {2,4,7,8,10};
        int j = 0;
        for (int i : nums){
            j += i - 1;
        }
        System.out.println(j);
    }
}