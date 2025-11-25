
import java.util.Scanner;
public class nextRound {

   
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int [] arr = new int[n];
        for(int j=0;j<n;j++){
            arr[j] = sc.nextInt();
        }
        int i=0;
         int ans = 0;
        while(i<n){
          
            if(arr[i]>=arr[k-1] && arr[i]>0){
                ans++;
            }
           
            i++;
        }
        System.out.println(ans);
    }
    
}
