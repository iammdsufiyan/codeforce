
import java.util.Scanner;

public class WayTooLongsWords {
    
    public static void main(String [] args){
        
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        String [] arr = new String [num];
        int i =0;
        while(num>i){
            String str = sc.next();
            arr[i] = str;
            i++;
        }

       
          

            for(int k=0;k<num;k++){
                  String s = arr[k];
                if(s.length()>10){
                    System.out.println("" + s.charAt(0)+ (s.length()-2)+s.charAt(s.length()-1));
                }
                else{
                    System.out.println(s);
                }
            }
        
    }
}
