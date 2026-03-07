// O(N) - по времени и O(1) по памяти 
// Даны две ASCII строки одинаковой длины из латинских букв.
// Нужно опредеелить, является одна строка изоморфной по отношению к другой.

// Метод isIsomorphic проверяет, можно ли заменить символы в s1 так, чтобы получить s2, при условии:

// каждый символ s1 отображается ровно в один символ s2
// разные символы s1 не могут отображаться в один и тот же символ s2
// Например, "egg" и "add" — изоморфны (e→a, g→d), а "ab" и "aa" — нет (и a, и b пытаются отобразиться в a).

// Подсказка: тебе нужно отслеживать маппинг в обе стороны — из s1 в s2 и из s2 в s1. 
// Подумай, какие структуры размером 26 (или 128 для ASCII) помогут это сделать.

public class App_6_6_isomorph {

    public static boolean isIsomorphic(String s1, String s2) {
        // алгоритм
        
        int[] numS1 = new int[95];
        int[] numS2 = new int[95];

        for(int i = 0; i < s1.length(); i++){
            int letterS1 = s1.charAt(i)-32;
            int letterS2 = s2.charAt(i)-32;
            if(numS1[letterS1] != numS2[letterS2]) return false;

            numS1[letterS1] = i + 1;
            numS2[letterS2] = i + 1;
        
    }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(isIsomorphic("egg", "add"));       // true  (e->a, g->d)
        System.out.println(isIsomorphic("foo", "bar"));       // false (o->a и o->r — конфликт)
        System.out.println(isIsomorphic("paper", "title"));   // true  (p->t, a->i, e->l, r->e)
        System.out.println(isIsomorphic("ab", "aa"));         // false (a->a, b->a — два символа на один)
        System.out.println(isIsomorphic("abc", "abc"));       // true
    }
}
