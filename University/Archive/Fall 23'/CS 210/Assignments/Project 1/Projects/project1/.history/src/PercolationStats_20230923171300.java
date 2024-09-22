import stdlib.StdOut;
import stdlib.StdRandom;
import stdlib.StdStats;

public class PercolationStats {
    // Constructs an n x n percolation system, with all sites blocked.
    private double[] thresholds; // thresholds[i] = percolation threshold for experiment i
    private final int m; // # of experiments

    // Performs m independent experiments on an n x n percolation system.
    public PercolationStats(int n, int m) {
        if (n <= 0) throw new IllegalArgumentException("n must be > 0");
        if (m <= 0) throw new IllegalArgumentException("m must be > 0");

        this.m = m;
        thresholds = new double[m];

        for (int i = 0; i < this.m; i++) {
            Percolation perc = new Percolation(n);
            while (!perc.percolates()) {
                int row = StdRandom.uniform(n);
                int col = StdRandom.uniform(n);
                perc.open(row, col);
            }
            thresholds[i] = (double) perc.numberOfOpenSites() / (n*n);
        }
    }

    // Returns sample mean of percolation threshold.
    public double mean() {
        return StdStats.mean(thresholds);
    }

    // Returns sample standard deviation of percolation threshold.
    public double stddev() {
        return StdStats.stddev(thresholds);
    }

    // Returns low endpoint of the 95% confidence interval.
    public double confidenceLow() {
        return mean() - (1.96 * stddev()) / Math.sqrt(m);
    }

    // Returns high endpoint of the 95% confidence interval.
    public double confidenceHigh() {
        return mean() + (1.96 * stddev()) / Math.sqrt(m);
    }

    // Unit tests the data type. [DO NOT EDIT]
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int m = Integer.parseInt(args[1]);
        PercolationStats stats = new PercolationStats(n, m);
        StdOut.printf("Percolation threshold for a %d x %d system:\n", n, n);
        StdOut.printf("  Mean                = %.3f\n", stats.mean());
        StdOut.printf("  Standard deviation  = %.3f\n", stats.stddev());
        StdOut.printf("  Confidence interval = [%.3f, %.3f]\n", stats.confidenceLow(),
                stats.confidenceHigh());
    }
}