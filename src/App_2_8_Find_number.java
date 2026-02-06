// Дано 3 млрд неотрицательных чисел. Необходимо вывести 1 число, которого нету в файле.
// Ограничение по памяти - 512 Мб.
// Внутрь метода передадим локальный путь до файла с числами.

// Можно было бы перебрать все числа из файлов: создать массив boolean;
//  по индексу установить true и вывести первое число у которого false.

// киби = 1024 байта 
// меби = 1024 кибибайта
// гиби = 1024 мебибайта
// теби = 1024 гибибайта


// Но в 3 000 000 000 * 4 = 12 000 000 000 байт или 12 000 000 000 / 1024 / 1024 / 1024 = 11.17 гибибайт

// поэтому нужно использовать битовый вектор на 3 млрд значений.  Повезло, так как у нас неотрицательные числа - индексы битов не могут принимать отрицательные значения. 
// Тогда бы было бы тяжелее решить.

// Создавать битовый вектор на 3 млрд значений сразу - получается тоже неоптимально.
// Диапазон хранения типа int (знаковый) поэтому - количество чисел составляет не 2^32, а 2^31. 
// 2 147 583 648 / 8 / 1024/ 1024 = 256 мибибайт. Остальные числа значит дубликаты. А дублей 852 516 352 - поэтому надо создать битовйы вектор на 2^31

// Сколько всего числе в массиве?
// 2 147 483 648/32 = 67 108 864 числа типа int

// Для чтения и перебора файла используется Scanner 

import java.io.FileReader;
import java.util.Scanner;

public class App_2_8_Find_number {
    
    private int[] bitVector;
    private long maxIndex;

    public App_2_8_Find_number(long bits) throws Exception {
        if (bits <= 0 || bits > 68719476704L)
            throw new Exception("Bit vector size must be positive and not exceed 68719476704L.");
        maxIndex = bits - 1;
        int size = (int)(((bits - 1) >> 5) + 1);
        bitVector = new int[size];
    }

    private void checkIndex(long index) throws Exception {
        if (index < 0 || index > maxIndex)
            throw new Exception("Index " + index + " is out of bounds [0, " + maxIndex + "].");
    }

    private int getRow(long index) {
        return (int)(index >> 5);
    }

    private int getCol(long index) {
        return (int)(index % 32);
    }

    public void setBit(long index) throws Exception {
        checkIndex(index);
        int row = getRow(index);
        int col = getCol(index);
        int mask = 1 << col;
        bitVector[row] |= mask;
    }

    public boolean isSetBit(long index) throws Exception {
        checkIndex(index);
        int row = getRow(index);
        int col = getCol(index);
        int mask = 1 << col;
        int bit = bitVector[row] & mask;
        return bit != 0;
    }
    
    public int findMissingNumber(String path) throws Exception {
        App_2_8_Find_number bitVector = new App_2_8_Find_number(2_147_483_648L);
        Scanner scanner = new Scanner(new FileReader(path));
        while (scanner.hasNextInt()) bitVector.setBit(scanner.nextInt());
        scanner.close();
        for(long i = 0; i < 2_147_483_648L; i++) {
            if(!bitVector.isSetBit(i)) {
                return (int)i;
            }
        }
        throw new Exception("No missing number found within the range.");
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.out.println("Usage: java App_2_8_Find_number <inputFilePath>");
            return;
        }
        String inputFilePath = args[0];
        App_2_8_Find_number finder = new App_2_8_Find_number(2_147_483_648L);
        try {
            int missingNumber = finder.findMissingNumber(inputFilePath);
            System.out.println("The missing number is: " + missingNumber);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
