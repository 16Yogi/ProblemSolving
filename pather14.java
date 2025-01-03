public class pather14 {
    public static void main(String[] args){
        for(char i = 'a'; i<='e';i++){  // Outer loop: i runs from 'a' to 'e'
            for(char j = 'e'; j; j++){  // Inner loop with incorrect decrement
                System.out.print(j);
            }
            System.out.println();
        }
    }
}
