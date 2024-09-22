import stdlib.In;
import stdlib.StdOut;

// An implementation of the Percolation API using a 2D array.
public class ArrayPercolation implements Percolation {
    private final boolean[][] open; // open[i][j] = is site (i, j) open?
    private final boolean[][] full;
    private final int n;            // n-by-n percolation system


    // Constructs an n x n percolation system, with all sites blocked.
    public ArrayPercolation(int n) {
        if (n <= 0) throw new IllegalArgumentException("Illegal n");
        this.n = n;
        open = new boolean[n][n];
        full = new boolean[n][n];
    }

    // Opens site (i, j) if it is not already open.
    public void open(int i, int j) {
        boundaryCheck(i, j);
        
        // if site (i, j) is not open, set open[i][j] to true
        if (!isOpen(i, j)) {
            open[i][j] = true;
            floodFill(i, j);
        }
    }

    // Returns true if site (i, j) is open, and false otherwise.
    public boolean isOpen(int i, int j) {
        boundaryCheck(i, j);
        // return true if open[i][j] is true
        return open[i][j];
    }

    // Returns true if site (i, j) is full, and false otherwise.
    public boolean isFull(int i, int j) {
        boundaryCheck(i, j); 
        return full[i][j];
    }

    // Returns the number of open sites.
    public int numberOfOpenSites() {
        int count = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (open[i][j]) count++;
        return count;
    }

    // Returns true if this system percolates, and false otherwise.
    public boolean percolates() {
        for (int i = 0; i < n; i++)
            if (isFull(n - 1, i)) return true;
        return false;
        }

    // Recursively flood fills full[][] using depth-first exploration, starting at (i, j).
    private void floodFill(int i, int j) {
        if (i < 0 || i >= n || j < 0 || j >= n || !open[i][j] || full[i][j]) return;
        full[i][j] = true;
        floodFill(i+1, j);
        floodFill(i-1, j);
        floodFill(i, j+1);
        floodFill(i, j-1);
    }

    private void boundaryCheck(int i, int j) {
        if (i < 0 || i >= n || j < 0 || j >= n)
            throw new IndexOutOfBoundsException("Illegal i or j");
    }


    // Unit tests the data type. [DO NOT EDIT]
    public static void main(String[] args) {
        String filename = args[0];
        In in = new In(filename);
        int n = in.readInt();
        ArrayPercolation perc = new ArrayPercolation(n);
        while (!in.isEmpty()) {
            int i = in.readInt();
            int j = in.readInt();
            perc.open(i, j);
        }
        StdOut.printf("%d x %d system:\n", n, n);
        StdOut.printf("  Open sites = %d\n", perc.numberOfOpenSites());
        StdOut.printf("  Percolates = %b\n", perc.percolates());
        if (args.length == 3) {
            int i = Integer.parseInt(args[1]);
            int j = Integer.parseInt(args[2]);
            StdOut.printf("  isFull(%d, %d) = %b\n", i, j, perc.isFull(i, j));
        }
    }
}