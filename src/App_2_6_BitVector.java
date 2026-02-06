public class App_2_6_BitVector {

    private int[] bitVector;
    private long maxIndex;

    public App_2_6_BitVector(long bits) throws Exception {
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

    public void unsetBit(long index) throws Exception {
        checkIndex(index);
        int row = getRow(index);
        int col = getCol(index);
        int mask = ~(1 << col);
        bitVector[row] &= mask;
    }

    public void inverseBit(long index) throws Exception {
        checkIndex(index);
        int row = getRow(index);
        int col = getCol(index);
        int mask = 1 << col;
        bitVector[row] ^= mask;
    }

    public boolean isSetBit(long index) throws Exception {
        checkIndex(index);
        int row = getRow(index);
        int col = getCol(index);
        int mask = 1 << col;
        int bit = bitVector[row] & mask;
        return bit != 0;
    }

    // Вложенный класс с main
    public static class Main {
        public static void main(String[] args) throws Exception {
            App_2_6_BitVector bitVector = new App_2_6_BitVector(96);
            bitVector.setBit(70);
            System.out.println(bitVector.isSetBit(70));
        }
    }
}
