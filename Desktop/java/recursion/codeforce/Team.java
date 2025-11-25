
import java.util.Scanner;

public class Team {
    
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int i = 0;
        int count = 0;
        while(i<num){
            int petya = sc.nextInt();
            int vasya = sc.nextInt();
            int tonya = sc.nextInt();

            if(petya + vasya + tonya >=2){
                count++;
            }
            i++;
        }

        System.out.println(count);

    }

}
