// O(N) - по времени и O(1) по памяти 
public class App_5_2_max2 {
    public static int removeALLN(int[] arr, int n) {
        int L = 1;
        if (arr.length == 1) return 1;
        for (int R = 2; R < arr.length; R++) {
            int val = arr[R];
            if (arr[L-1] == val) continue;
                
            L++;
        }

        return L;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 2, 3, 3, 3, 4, 7, 7, 7, 7};
        int n = 2;
        int newLength = removeALLN(arr, n);
        System.out.println(newLength);
    }
}
