package classandobj;
import java.util.Scanner;

public class SimpleCalculator {

    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static double divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero!");
        }
        return (double) a / b;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter first number: ");
            int num1 = sc.nextInt();

            System.out.print("Enter second number: ");
            int num2 = sc.nextInt();

            System.out.println("Choose Operation: ");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");

            int choice = sc.nextInt();

        try {
            switch (choice) {
                case 1:
                    System.out.println("Result = " + add(num1, num2));
                    break;

                case 2:
                    System.out.println("Result = " + subtract(num1, num2));
                    break;

                case 3:
                    System.out.println("Result = " + multiply(num1, num2));
                    break;

                case 4:
                    System.out.println("Result = " + divide(num1, num2));
                    break;

                default:
                    System.out.println("Invalid choice!");
            }
            } catch (ArithmeticException e) {
                System.out.println("Error: " + e.getMessage());
            }
        } catch (java.util.InputMismatchException e) {
            System.out.println("Error: Invalid input. Please enter integers only.");
        }

        sc.close();
    }
}