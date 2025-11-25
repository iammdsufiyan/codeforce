
import java.util.Scanner;
public class Bit {
    
    public static void main (String[] args){
 Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();

    int i = 0;
     int X = 0;
    while(i<num){ 
        String s = sc.next();
            if(s.equals("++X") || s.equals("X++") ){
                X++;
            }
            else{
                X--;
            }
                i++;
    }
    
       System.out.println(X);
    }
   
}
