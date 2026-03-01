// O(N) - по времени и O(1) по памяти 
// Дана строка в кодировке ASCII, состоящая из множества слов, разделенных пробелами.
// Сама строка не может начинаться и заканчиваться пробелом.
// Нужно вернуть количество слов, состоящих только из латинских букв

public class App_6_3_latinaWords {

    public static int countLatinWords(String str) {
        // алгоритм (латинские буквы - от 65 до 90 и от 97 до 122)
        int count = 0;
        boolean latin = true;
        for(int i =0; i < str.length(); i++){

            int code = str.charAt(i);
            
            if(code == ' '){
                if(latin) count++;
                latin=true;
            } else {
                if(code < 65 || code > 90 && code < 97 || code > 122){
                    latin = false;
                }
            }
        }
        if(latin) count++;

        return count;
    }

    public static void main(String[] args) {
        System.out.println(countLatinWords("hello world"));          // 2
        System.out.println(countLatinWords("hello world123 foo"));   // 2 (world123 — не только латиница)
        System.out.println(countLatinWords("123 456"));              // 0
        System.out.println(countLatinWords("Java"));                 // 1
        System.out.println(countLatinWords("cat one dog 1wo"));                 // 3
    }
}
