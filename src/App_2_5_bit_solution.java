public class App_2_5_bit_solution {
    public static void main(String[] args) throws Exception {
        // 285724330
        int A = 285689642;
        int B = 1132478069;
        int start = 16;
        int end = 5;
        
        // Ставим в единицы старшие биты до start
        int maskL = (int)(-1L << (start + 1));
        // Ставим в единицы младшие биты после end
        int maskR = (1 << end) - 1;
        int maskA = maskL | maskR;
        A &= maskA;
        // Пододвигаем к нашему диапазону младшие биты.
        B <<= end;
        // Ставим в единицы все биты в B после start (Скобки имеют значение)
        int maskB = (int)((1L << (start + 1)) - 1);
        B &= maskB;

        System.out.println(A|B);

    }
}
