// O(N) - по времени и O(N) по памяти 
// Дана строка с пробелами, необходимо вернуть строку, где вместо пробелов используется символ %20.

public class App_6_4_substituteEmpty {

    public static String replaceSpaces(String str) {
        // алгоритм
        int countSpaces = 0;
        // Посчитать все пробелы
        for (int i = 0; i < str.length(); i++){
            if(str.charAt(i) == ' ') countSpaces++;
        }
        // можем посчитать длигну новой строки
        char[] resArr = new char[str.length() + countSpaces * 2];
        int freeIndex = 0;
        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) == ' '){
                resArr[freeIndex++] = '%';
                resArr[freeIndex++] = '2';
                resArr[freeIndex++] = '0';
                
            } else {
                resArr[freeIndex++] = str.charAt(i);
            }

        }
        return new String(resArr);
    }

    public static void main(String[] args) {
        System.out.println(replaceSpaces("hello world"));        // hello%20world
        System.out.println(replaceSpaces("a b c"));              // a%20b%20c
        System.out.println(replaceSpaces("nospaces"));           // nospaces
        System.out.println(replaceSpaces(" hi "));               // %20hi%20
    }
}
