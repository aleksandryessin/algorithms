public class App_2_1_inversion {
    public static void main(String[] args) throws Exception {
        byte a = 0x16;
        a = (byte)(a ^ 0x08);
        System.out.println(a);
    }
}
