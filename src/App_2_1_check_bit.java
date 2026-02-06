public class App_2_1_check_bit {
    public static void main(String[] args) throws Exception {
        byte a = 0x16;
        System.out.println(isBit(a));
    }

    public static boolean isBit(byte a) {
        // ...check if the bit is set
        byte result = (byte)(a&0x02);
        if(result != 0) return true;
        return false;
    }
}
