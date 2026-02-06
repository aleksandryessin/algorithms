public class App_2_2_is_bit_set {
    public static void main(String[] args) throws Exception {
        byte a = 0x6B;
        a = (byte)(a & 0xF0);
        System.out.println(a);
    }
}
