// O(N) - по времени и O(1) по памяти 
// классическая "Container With Most Water"
// Дан массив целых положительных чисел. Каждое число в массиве обозначает высоту стенки в метрах.
// Расстояние между каждой стенкой равно 1-му метру.
// Сверху над стенками можно лить воду.
// Нужно вернуть максимальнуо возможную площадь прямоугольника с водой.

public class App_5_4_waterWall {

    public static int maxWaterArea(int[] walls) {
        // алгоритм
        int start = 0;
        int end = walls.length - 1;
        int max = 0;

        while (start < end) {
            int width = end - start;
            int height = Math.min(walls[start], walls[end]);
            max = Math.max(max, width * height);
            
            if(walls[start] < walls[end]) start ++;
            else end--;
        }
        return max;
    }

    public static void main(String[] args) {
        int[] walls = new int[]{2, 6, 7, 3, 5, 7, 4}; // 1, 8, 6, 2, 5, 4, 8, 3, 7
        int result = maxWaterArea(walls);
        System.out.println(result); // ожидаемый ответ: 49 для 1, 8, 6, 2, 5, 4, 8, 3, 7 и 24 для 2, 6, 7, 3, 5, 7, 4
    }
}
