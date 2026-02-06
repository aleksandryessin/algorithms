public class App_2_1_set_zero {
    public static void main(String[] args) throws Exception {
        byte a = 0x16;
        a = (byte)(a & 0xFB);
        System.out.println(a);
    }
}
