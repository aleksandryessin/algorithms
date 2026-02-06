public class App_2_7_Duplicates {
    
    private int[] bitVector;
    private long maxIndex;

    public App_2_7_Duplicates(long bits) throws Exception {
        if (bits <= 0 || bits > 68719476704L)
            throw new Exception("");
        maxIndex = bits - 1;
        int size = (int)(((bits - 1) >> 5) + 1);
        bitVector = new int[size];
    }

    private void checkIndex(long index) throws Exception {
        if (index < 0 || index > maxIndex)
            throw new Exception("");
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

    void printDuplicates(int[] numbers) throws Exception {
        App_2_7_Duplicates bitVector = new App_2_7_Duplicates(32000);
        for (int i = 0; i<numbers.length; i++){
            if(bitVector.isSetBit(numbers[i]-1))
                System.out.println(numbers[i]);
            else bitVector.setBit(numbers[i]-1);
        }
    }
    
    // Вложенный класс с main
    public static class Main {
        public static void main(String[] args) throws Exception {
            App_2_7_Duplicates bit = new App_2_7_Duplicates(32000);
            int[] numbers = new int[]{1, 5, 4, 5, 4, 10, 11, 12, 21,  3, 3, 5, 7, 22, 21};
            bit.printDuplicates(numbers);
        }
    }
}


// class BitVector:
//     def __init__(self, bits: int):
//         if bits <= 0 or bits > 68719476704:
//             raise Exception("Invalid size")
//         self.max_index = bits - 1
//         size = ((bits - 1) >> 5) + 1  # делим на 32
//         self.bit_vector = [0] * size

//     def _check_index(self, index: int):
//         if index < 0 or index > self.max_index:
//             raise Exception("Index out of range")

//     def _get_row(self, index: int) -> int:
//         return index >> 5  # index // 32

//     def _get_col(self, index: int) -> int:
//         return index % 32

//     def set_bit(self, index: int):
//         self._check_index(index)
//         row = self._get_row(index)
//         col = self._get_col(index)
//         mask = 1 << col
//         self.bit_vector[row] |= mask

//     def is_set_bit(self, index: int) -> bool:
//         self._check_index(index)
//         row = self._get_row(index)
//         col = self._get_col(index)
//         mask = 1 << col
//         bit = self.bit_vector[row] & mask
//         return bit != 0


// class Duplicates:
//     def __init__(self):
//         self.bit_vector = BitVector(32000)

//     def print_duplicates(self, numbers):
//         for num in numbers:
//             idx = num - 1
//             if self.bit_vector.is_set_bit(idx):
//                 print(num)
//             else:
//                 self.bit_vector.set_bit(idx)


// if __name__ == "__main__":
//     dup = Duplicates()
//     numbers = [1, 5, 3, 3, 5, 7]
//     dup.print_duplicates(numbers)
