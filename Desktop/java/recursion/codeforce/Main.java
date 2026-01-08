

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // number of test cases

        while (t-- > 0) {
            int size = sc.nextInt();
            int[] arr = new int[size];

            for (int i = 0; i < size; i++) {
                arr[i] = sc.nextInt();
            }

            int[] ans = Arrays.copyOf(arr, size);

            // Step 1: Fix first and last element
            if (size == 1) {
                if (ans[0] == -1) ans[0] = 0;
            } else {
                if (ans[0] == -1 && ans[size - 1] == -1) {
                    ans[0] = 0;
                    ans[size - 1] = 0;
                } else if (ans[0] == -1) {
                    ans[0] = ans[size - 1];
                } else if (ans[size - 1] == -1) {
                    ans[size - 1] = ans[0];
                }
            }

            // Step 2: Fill remaining -1 with 0
            for (int i = 1; i < size - 1; i++) {
                if (ans[i] == -1) {
                    ans[i] = 0;
                }
            }

            // Step 3: Calculate minimum absolute value
            int minValue = Math.abs(ans[size - 1] - ans[0]);

            // Output
            System.out.println(minValue);
            // Optional: print filled array
            // System.out.println(Arrays.toString(ans));
        }

        sc.close();
    }
}