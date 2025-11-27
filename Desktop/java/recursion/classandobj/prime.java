package classandobj;
import java.util.Scanner;
public class prime {

  

    public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    for(int i=2;i<n; i++){
        if(n/i==0){
            System.out.println("if is not a prime ");
        }
    }


    for(int i=2;i<n;i++){
        for(int j=2;j<i;j++){
            if(i%j==0){
                System.out.println(i+"it is not a prime ");
                break;
            }
            else{
                System.out.println(i+"it is a prime number ");
            }
        }
    }
    }
}
