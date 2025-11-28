package classandobj.InputOutputStream;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class SimpleFileStats {
    public static void main(String[] args) {
        String fileName = "Test.txt";

        int charCount = 0;
        int wordCount = 0;
        int lineCount = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {

            String line;

            while ((line = br.readLine()) != null) {
                lineCount++;                         // Count lines
                charCount += line.length();          // Count characters (without newline)

                // Count words (split by spaces)
                if (!line.trim().isEmpty()) {
                    String[] words = line.trim().split("\\s+");
                    wordCount += words.length;
                }
            }

            // Print results
            System.out.println("\n--- File Statistics ---");
            System.out.println("Characters: " + charCount);
            System.out.println("Words: " + wordCount);
            System.out.println("Lines: " + lineCount);

        } catch (IOException e) {
            System.out.println("Error while reading file: " + e.getMessage());
        }
    }
}
