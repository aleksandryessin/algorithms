import java.util.Arrays;

// O(N) - по времени и O(1) по памяти 

// для shiftArray(4):
// Исходный: [1, 1, 5, 3, 6, 9]
// После полного реверса: [9, 6, 3, 5, 1, 1]
// Реверс первых 4: [5, 3, 6, 9, 1, 1]
// Реверс оставшихся 2: [5, 3, 6, 9, 1, 1] 

public class App_5_3_shift_array {
    public static void reverse(int[] arr, int start, int end) {
        
        while (start<end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    public static void shiftArray(int n) {
        int[] arr = new int[]{1, 1, 5, 3, 6, 9};
        System.out.println(Arrays.toString(arr));
        
        // int shift = n % arr.length;
        //если отрицательное:
        int shift = ((n % arr.length) + arr.length) % arr.length;
        reverse(arr, 0, arr.length-1);
        reverse(arr, 0, shift-1);
        reverse(arr, shift, arr.length-1);

        System.out.println(Arrays.toString(arr));
    }

    public static void main(String[] args) {
        shiftArray(4); // сдвиг на 2, например
    }
}
