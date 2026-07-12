public static int findColumnWithMinZeros(int[][] arr) {

    int minZeros = Integer.MAX_VALUE;
    int columnIndex = -1;

    for (int j = 0; j < arr[0].length; j++) {
        int zeroCount = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i][j] == 0) {
                zeroCount++;
            }
        }

        if (zeroCount < minZeros) {
            minZeros = zeroCount;
            columnIndex = j;
        }
    }

    return columnIndex;
}