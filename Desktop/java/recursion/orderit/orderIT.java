import java.util.*;

public class OrderItBFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        
        // Read input (similar to your parsing logic)
        // ... parsing code ...
        
        List<String> shuffled = Arrays.asList(shuffledArr);
        List<String> original = Arrays.asList(originalArr);
        
        int moves = minMovesBFS(shuffled, original);
        System.out.println(moves);
    }
    
    static int minMovesBFS(List<String> shuffled, List<String> original) {
        if (shuffled.equals(original)) return 0;
        
        Queue<List<String>> queue = new LinkedList<>();
        Set<List<String>> visited = new HashSet<>();
        
        queue.offer(shuffled);
        visited.add(shuffled);
        int moves = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                List<String> current = queue.poll();
                if (current.equals(original)) return moves;
                
                for (List<String> neighbor : getNeighbors(current)) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);
                        queue.offer(neighbor);
                    }
                }
            }
            moves++;
        }
        return -1;
    }
    
    static List<List<String>> getNeighbors(List<String> arr) {
        List<List<String>> neighbors = new ArrayList<>();
        int n = arr.size();
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                List<String> block = arr.subList(i, j + 1);
                List<String> remaining = new ArrayList<>();
                remaining.addAll(arr.subList(0, i));
                remaining.addAll(arr.subList(j + 1, n));
                
                for (int k = 0; k <= remaining.size(); k++) {
                    if (k == i) continue;
                    List<String> newArr = new ArrayList<>();
                    newArr.addAll(remaining.subList(0, k));
                    newArr.addAll(block);
                    newArr.addAll(remaining.subList(k, remaining.size()));
                    neighbors.add(newArr);
                }
            }
        }
        return neighbors;
    }
}