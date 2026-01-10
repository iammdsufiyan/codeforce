import java.util.Scanner;

public class howToTakeInut {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
      String [] parts=  str.split(",|\\s+");

      for(int i=0;i<parts.length; i++){
    
        int num = Integer.parseInt(parts[i]);
        System.out.println(num);
      }
    }
}
