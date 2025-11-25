package codeforce;
import java.util.*;
public class YetAnotherArrayProblem {
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        for(int i=0;i<num;i++){
            int n = sc.nextInt();
            int [] arr = new int [n];
            for(int j=0;j<n;j++){
                arr[j] = sc.nextInt();
            }
            Arrays.sort(arr);

            for(int k=2;k<arr[arr.length-1];k++){
             
                if(arr[0]%k!=0){
                    System.out.println(k);
                    break;
                }
            }
        }
    }
}
