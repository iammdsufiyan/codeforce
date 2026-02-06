import java.io.*;
import java.util.*;

public class TestClass {
    public static int findMaxDigitsSum(int n, int arr[]) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int num = arr[i];
            int max = 0;
            if (num == 0) {
                max = 0;
            } else {
                while (num > 0) {
                    int rem = num % 10;
                    if (rem > max) {
                        max = rem;
                    }
                    num /= 10;
                }
            }
            sum += max;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int arr[] = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(findMaxDigitsSum(size, arr));
    }
}