// package classandobj.InputOutputStream;
// import java.io.*;
// public class FileInputExample {

// public static void main(String[] args) {
    

//     try{
//         FileInputStream fis = new FileInputStream("Test.txt");

//         System.out.println(fis.available());

//         byte [] b = new byte[fis.available()];

//         fis.read(b);
       

//         String str = new String(b);

//         System.out.println(str);

        

//     }

//     catch(FileNotFoundException e){
//         System.out.println(e);
//     }
//     catch(IOException   e){
//         System.out.println(e);
//     }
// }
    
// }


package classandobj.InputOutputStream;

import java.io.*;

public class FileInputExample {

    public static void main(String[] args) {

        try {
           FileInputStream  fis = new FileInputStream("Test.txt");

            // Read file into byte array
            byte[] b = new byte[fis.available()];
            fis.read(b);

            // Convert to String
            String str = new String(b);

            // Print the file content
            System.out.println("File Content:\n" + str);

            // --- Count Characters, Words, Lines ---
            int charCount = str.length();

            // Split by whitespace for words
            String[] words = str.trim().isEmpty() ? new String[0] : str.trim().split("\\s+");
            int wordCount = words.length;

            // Split by newline for lines
            String[] lines = str.split("\r?\n");
            int lineCount = lines.length;

            // Print results
            System.out.println("\n--- File Statistics ---");
            System.out.println("Characters: " + charCount);
            System.out.println("Words: " + wordCount);
            System.out.println("Lines: " + lineCount);

            fis.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("File not found: " + e);
        }
        catch (IOException e) {
            System.out.println("IO Error: " + e);
        }
    }
}