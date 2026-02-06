public class App_5_1_del_n {
    public static int removeALLN(int[] arr, int n) {
        int L = 0;

        for (int R = 0; R < arr.length; R++) {
            int val = arr[R];
            if (val == n) {
                continue;
            }
            arr[L] = val;
            L++;
        }

        return L;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 2, 3, 4, 2, 5, 2, 6, 10};
        int n = 2;
        int newLength = removeALLN(arr, n);
        System.out.println(newLength);
    }
}
