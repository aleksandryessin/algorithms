// O(N) - по времени и O(1) по памяти 
// Дан отсортированный массив целых чисел от меньшего к большему.
// Нужно вернуть массив, состоящий из массивов всех пар индексов элементов, которые в сумме дадут число N.
// Индексы в каждой паре должны быть уникальными.

// Для того, чтобы определить массивы индексов - необходимо взять каждые пары чисел, их сложить и сравнить с N.

import java.util.ArrayList;
import java.util.List;

public class App_5_5_pairsNSUM {

    public static List<int[]> pairsNSum(int[] arr, int n) {
        List<int[]> result = new ArrayList<>();
        // алгоритм с двумя указателями:
        int start = 0;
        int end = arr.length - 1;
        while (start < end){

            int sum = arr[start] + arr[end];
            if(sum == n){result.add(new int[]{start, end});
                start++;
                end--;
            }
            else if(sum<n) start++;
            else end--;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 3, 4, 5, 6, 7};
        int n = 8;
        List<int[]> pairs = pairsNSum(arr, n);
        for (int[] pair : pairs) {
            System.out.println("[" + pair[0] + ", " + pair[1] + "]");
        }
        // ожидаемый вывод:
        // [0, 6]  (1+7=8)
        // [1, 5]  (2+6=8)
        // [2, 4]  (3+5=8)
    }
}
