package classandobj.exceptionHandling;

import java.util.Scanner;
import java.util.*;;
public class exception {

    public static void main(String[] args) {

        try {
            Scanner sc = new Scanner(System.in);

            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = a / b;
            System.out.println(c);
        } catch (ArithmeticException e) {

            System.out.println("Denominatore cannot be 0");


       
        }
         System.out.println("Bye");

    }

}
