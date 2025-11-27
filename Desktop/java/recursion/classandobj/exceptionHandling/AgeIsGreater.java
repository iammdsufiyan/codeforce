package classandobj.exceptionHandling;
import java.util.Scanner;

class  InvalidAgeException extends Exception {

    public  InvalidAgeException(String masg){
        super (masg);
    }
    
}

public class AgeIsGreater {
 static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        try {

          
            System.out.println("Enter your age");
            int age = sc.nextInt();


            if(age>18){
                System.out.println("you are eligible ");
            }
            else{
                throw new InvalidAgeException("age is below 18");
            }

        }
          catch(InvalidAgeException e){
                           System.out.println("nvalid input you are below 18");

          }  
         catch (Exception e) {
           System.out.println(e);
        }

    }
    
}
