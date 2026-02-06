public class App_2_1_task_i_in_k_bits {
    public static void main(String[] args) throws Exception {
        byte a = 0x63; // 0110 0011. k = 3, i = 3.
        byte result = (byte)((a | 8) & 0xFF);
        System.out.println(result);
    }
}
