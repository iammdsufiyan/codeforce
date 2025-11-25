import java.util.Scanner;

public class scanner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number:");
        String line = sc.nextLine();
        String[] numbers = line.split(",");
        int tc = Integer.parseInt(numbers[0].trim());
        System.out.println("You entered: " + tc);

        System.out.println("Enter the numbers for the array, separated by commas:");
        String arrayLine = sc.nextLine();
        String[] arrayNumbersStr = arrayLine.split(",");
        int n = arrayNumbersStr.length;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(arrayNumbersStr[i].trim());
        }
        System.out.println("Array created with the following " + n + " elements:");
        for (int i = 0; i < n; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
        sc.close();
    }
}
