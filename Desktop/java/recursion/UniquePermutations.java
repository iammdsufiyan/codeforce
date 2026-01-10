// import java.util.*;

// public class UniquePermutations {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int n1 = sc.nextInt();
//         int n2 = sc.nextInt();
//         int n3 = sc.nextInt();
//         sc.close();

//         Map<Character, Integer> freq = new HashMap<>();
//         freq.put('a', n1);
//         freq.put('b', n2);
//         freq.put('c', n3);

//         StringBuilder sb = new StringBuilder();
//         backtrack(sb, freq, n1 + n2 + n3);
//     }

//     public static void backtrack(StringBuilder sb, Map<Character, Integer> freq, int targetLen) {
//         if (sb.length() == targetLen) {
//             System.out.println(sb.toString());
//             return;
//         }

//         for (char ch : freq.keySet()) {
//             int count = freq.get(ch);
//             if (count > 0) {
//                 sb.append(ch);
//                 freq.put(ch, count - 1);

//                 backtrack(sb, freq, targetLen);

//                 // backtrack
//                 sb.deleteCharAt(sb.length() - 1);
//                 freq.put(ch, count);
//             }
//         }
//     }
// }

import java.util.*;

// public class UniquePermutations {

//     public static void main(String [] args){
//         Scanner sc = new Scanner(System.in);
//         int n1 = sc.nextInt();
//         int n2 = sc.nextInt();
//         int n3 = sc.nextInt();
//         sc.close();

//         HashMap <Character, Integer> map = new HashMap<>();

//         map.put('a', n1);
//         map.put('b',n2);
//         map.put('c',n3);

//         StringBuilder sb=  new StringBuilder();

//         backtrack(sb, map , n1+n2+n3);
//     }

//    public static void   backtrack (StringBuilder sb, HashMap <Character, Integer> map,  int len){

//         if(sb.length() == len){
//             System.out.println(sb.toString());
//             return ;
//         }
//     }
     
// }

public class UniquePermutations {
    public static void main(String[] args) {
        int n1 = 2, n2 = 1, n3 = 0;

        char[] chars = {'a', 'b', 'c'};
        int[] count = {n1, n2, n3};

        backtrack(new StringBuilder(), chars, count, n1 + n2 + n3);
    }

    static void backtrack(StringBuilder sb, char[] chars, int[] count, int len) {
        if (sb.length() == len) {
            System.out.println(sb.toString());
            return;
        }

        for (int i = 0; i < 3; i++) {
            if (count[i] > 0) {
                sb.append(chars[i]);
                count[i]--;

                backtrack(sb, chars, count, len);

                sb.deleteCharAt(sb.length() - 1);
                count[i]++;
            }
        }
    }
}