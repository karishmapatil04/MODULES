
import java.util.Arrays;

class DataSet {
    private double[] data;
    private int dataSize;
    private double sum;

    public DataSet() {
        data = new double[100];
        dataSize = 0;
        sum = 0;
    }

    public void add(double value) {
        // Optional safety check
        if (dataSize == data.length) {
            System.out.println("DataSet is full!");
            return;
        }
        data[dataSize] = value;
        dataSize++;
        sum += value;
    }

    public double getAverage() {
        return (dataSize == 0 ? 0 : sum / dataSize);
    }

    // Part (a): Calculate standard deviation
    public double getStandardDeviation() {
        if (dataSize == 0)
            return 0;

        double mean = getAverage();
        double sumOfSquares = 0.0;

        for (int i = 0; i < dataSize; i++) {
            double diff = data[i] - mean;
            sumOfSquares += diff * diff; // more efficient than Math.pow(diff, 2)
        }

        return Math.sqrt(sumOfSquares / dataSize);
    }

    // Part (b): Static method to compute average of averages
    public static double calculateAverage(DataSet[] datasets) {
        double total = 0.0;
        for (DataSet ds : datasets) {
            total += ds.getAverage();
        }
        return total / datasets.length;
    }

    @Override
    public String toString() {
        return "DataSet{" +
                "data=" + Arrays.toString(data) +
                ", dataSize=" + dataSize +
                ", sum=" + sum +
                '}';
    }
}

public class Main {
    public static void main(String[] args) {

        // Test Part (a): Standard Deviation
        DataSet dataset = new DataSet();
        dataset.add(10.0);
        dataset.add(3.7);
        dataset.add(4.5);
        System.out.println("Standard Deviation: " + dataset.getStandardDeviation());

        // Test Part (b): Average of Averages
        DataSet d1 = new DataSet();
        d1.add(20.0);
        d1.add(30.0);
        d1.add(40.0);

        DataSet d2 = new DataSet();
        d2.add(10.0);
        d2.add(20.0);
        d2.add(30.0);

        DataSet d3 = new DataSet();
        d3.add(50.0);
        d3.add(60.0);
        d3.add(70.0);

        DataSet[] datasets = { d1, d2, d3 };

        System.out.println("Average of Averages: " + DataSet.calculateAverage(datasets));
    }
}
