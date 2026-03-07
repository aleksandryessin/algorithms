// O(A*B) - по времени  (так как перебираем во вложенных циклах два параметра) и O(1) по памяти (так как ничего не создаем)
// Даны две ASCII строки - длинная и короткая.
// Нужно вернуть индекс первого вхождения короткой строки в длинной.
// Если же длина второй строки (короткой) все-таки длинее - возвращаем -1.


// Метод substringSearch принимает длинную строку text и короткую pattern, возвращает индекс первого вхождения или -1.

// Подсказка: наивный подход — для каждой позиции в text проверять, совпадает ли подстрока длиной pattern.length(). Подумай:

// до какого индекса в text имеет смысл проверять?
// как выйти из внутренней проверки пораньше, если символы не совпали?


public class App_6_7_subraw_search {

    public static int substringSearch(String s1, String s2) {
        // алгоритм
        if(s2.length() > s1.length()) return -1;

        for(int L = 0; L <= s1.length() - s2.length(); L++){
            int S = 0;
            while (S < s2.length()){
                if(s2.charAt(S) != s1.charAt(L+S)) break;
                S++;
            }
            if(S == s2.length()) return L;
        }

        return -1;
    }
 
    public static void main(String[] args) {
        System.out.println(substringSearch("hello world", "world"));   // 6
        System.out.println(substringSearch("hello world", "hello"));   // 0
        System.out.println(substringSearch("hello world", "xyz"));     // -1
        System.out.println(substringSearch("aaabaaab", "aaab"));       // 0
        System.out.println(substringSearch("abc", "abcdef"));          // -1 (pattern длиннее)
        System.out.println(substringSearch("program", "ram"));         // 4
    }
}
