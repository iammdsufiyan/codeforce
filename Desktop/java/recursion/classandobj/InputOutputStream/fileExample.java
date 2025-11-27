package classandobj.InputOutputStream;
import java.io.*;
public class fileExample {
    public static void main(String[] args) {
        
       

        try{
             FileOutputStream f = new FileOutputStream("Test.txt");

        String str = "Learn Java Programing";


        f.write(str.getBytes());

            f.close();
        }
        catch(FileNotFoundException e){
            System.out.println(e);
        }

        catch(IOException e){
                System.out.println(e);
        }

        
        
    }
    
}
