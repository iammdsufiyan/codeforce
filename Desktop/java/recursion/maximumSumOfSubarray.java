// import java.util.*;

// public class maximumSumOfSubarray {

//     public static void main(String[] args) {

//         Scanner sc = new Scanner(System.in);

//         int n = sc.nextInt();
//         int[] arr = new int[n];

//         for (int i = 0; i < n; i++) {
//             arr[i] = sc.nextInt();
//         }

//         // prefix sum
//         int[] prefix = new int[n + 1];
//         for (int i = 0; i < n; i++) {
//             prefix[i + 1] = prefix[i] + arr[i];
//         }

//         // map to count subarray sums
//         HashMap<Integer, Integer> map = new HashMap<>();

//         int max = 0;

//         // generate all subarrays
//         for (int i = 0; i < n; i++) {
//             for (int j = i; j < n; j++) {

//                 int sum = prefix[j + 1] - prefix[i];

//                 // increase count of this sum
//                 map.put(sum, map.getOrDefault(sum, 0) + 1);

//                 // if same sum appears at least twice
//                 if (map.get(sum) >= 2) {
//                     max = Math.max(max, sum);
//                 }
//             }
//         }

//         System.out.println(max);
//     }
// }

// import java.util.*;

// public class maximumSumOfSubarray{
//     public static void main(String [] args){
//         Scanner sc = new Scanner(System.in);
//             int n = sc.nextInt();

//             int [] arr = new int [n];

//             for(int i=0;i<n;i++){
//                 arr[i] = sc.nextInt();
//             }
//             HashMap <List<Integer>,Integer> map = new HashMap<>();

// int sum =0;
// int max = 0;
//             for(int i=0;i<n;i++){
//                List<Integer> sub = new ArrayList<>();
//                 sum =0;
//                 for(int j=i;j<n;j++){
//                     sum = sum+arr[j];
//                     sub.add(arr[j]);
//                     boolean found = false;
//                     for(int val: map.values()){
//                         if(val==sum){
//                             found = true;
//                             break;
//                         }
//                     }
//                     if(found){
//                         max = Math.max(max,sum);
//                     }


//                     map.put(new ArrayList<>(sub),sum);
//                 }
//             }
//             System.out.println(max);
//     }
// }


import java.util.*;

public class maximumSumOfSubarray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        HashMap<List<Integer>, Integer> freqMap = new HashMap<>();
        int max = 0;

        for (int i = 0; i < n; i++) {
            List<Integer> sub = new ArrayList<>();
            int sum = 0;

            for (int j = i; j < n; j++) {
                sub.add(arr[j]);
                sum += arr[j];

                // 🔑 normalize (order independent)
                List<Integer> key = new ArrayList<>(sub);
                Collections.sort(key);

                freqMap.put(key, freqMap.getOrDefault(key, 0) + 1);

                if (freqMap.get(key) == 2) {
                    max = Math.max(max, sum);
                }
            }
        }

        System.out.println(max);
    }
}