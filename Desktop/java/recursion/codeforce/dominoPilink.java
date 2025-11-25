
import java.util.Scanner;
public class dominoPilink {
    
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);

        int M = sc.nextInt();
        int N = sc.nextInt();

        int area = M*N;

        int ans = area/2;
        System.out.println(ans);
    }
}
