// O(N) - по времени и O(1) по памяти 
// Дана строка в кодировке ASCII, состоящая из печатных символов.
// Проверить - содержит ли она только уникальные символы или нет?
// True- уникальные, иначе False. Пример: A и a - это разные символы.
// Подсказка: 128 - 33 = 95 максимальных символов (уникальных) в строке.

public class App_6_2_uniqueSym {

    public static boolean isUnique(String str) {
        // алгоритм 
        if(str.length() > 95) return false;
        boolean[] chars = new boolean[95];
        for (int i = 0; i < str.length(); i++){
            int code = str.charAt(i) - 32;
            if(chars[code]) return false;
            chars[code] = true;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isUnique("abcdef"));   // true
        System.out.println(isUnique("abcdea"));   // false
        System.out.println(isUnique("aA"));        // true (разные символы)
        System.out.println(isUnique(""));           // true
    }
}
