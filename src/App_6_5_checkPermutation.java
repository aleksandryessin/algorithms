// O(N) - по времени и O(1) по памяти 
// Даны две строки из латинских букв нижнего регистра.
// Нужно опредеелить, является одна строка перестановкой другой.
// всего уникальных символов может быть 26 - массив на 26 элементов, который будем сравнивать с кодом буквы по ASCII.

public class App_6_5_checkPermutation {

    public static boolean isPermutation(String s1, String s2) {
        // алгоритм
        if (s1.length() != s2.length()) return false;
        
        int[] countLetters = new int[26];
        for (int i = 0; i < s1.length(); i++){
            countLetters[s1.charAt(i) - 'a']++; // 'a' = 97 позиция индекса (начиная с 97 кода - а нам надо, чтобы они начинались с 0)
            countLetters[s2.charAt(i) - 'a']--; 
        }

        // если строки по символам совпадут - то в массиве-счетчике все символы будут равны 0.
        for(int i = 0; i < countLetters.length; i++){
            if (countLetters[i] != 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPermutation("abc", "cba"));     // true
        System.out.println(isPermutation("abc", "abc"));     // true
        System.out.println(isPermutation("abc", "abd"));     // false
        System.out.println(isPermutation("aab", "aba"));     // true
        System.out.println(isPermutation("abc", "abcd"));    // false
    }
}
