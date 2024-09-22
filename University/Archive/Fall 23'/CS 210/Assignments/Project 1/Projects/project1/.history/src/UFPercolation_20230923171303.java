import dsa.WeightedQuickUnionUF;
import stdlib.In;
import stdlib.StdOut;

// An implementation of the Percolation API using the UF data structure.
public class UFPercolation implements Percolation {
    private final WeightedQuickUnionUF uf; // the UF data structure 
    private final int n;                   // n-by-n percolation system
    private int openSites;                 // number of open sites


    // Constructs an n x n percolation system, with all sites blocked.
    public UFPercolation(int n) {
        if (n <= 0) throw new IllegalArgumentException("n must be > 0");

        // create a new UF data structure with n^2 + 2 elements
        // n^2 for the sites, and 2 for the virtual top and bottom sites
        uf = new WeightedQuickUnionUF(n*n + 2);
        this.n = n;
        openSites = 0;

        // connect the virtual top site to the top row of sites
        for (int i = 0; i < n; i++) {
            uf.union(0, encode(0, i));
        }

        // connect the virtual bottom site to the bottom row of sites
        for (int i = 0; i < n; i++) {
            uf.union(n*n + 1, encode(n-1, i));
        }


    }

    // Opens site (i, j) if it is not already open.
    public void open(int i, int j) {
        if (i < 0 || i >= n) throw new IndexOutOfBoundsException("row index i out of bounds");
        if (j < 0 || j >= n) throw new IndexOutOfBoundsException("column index j out of bounds");

        // if site (i, j) is not open, set open[i][j] to true
        if (!isOpen(i, j)) {
            openSites++;
        }

        // connect site (i, j) to its open neighbors
        if (i > 0 && isOpen(i-1, j)) {
            uf.union(encode(i, j), encode(i-1, j));
        }
        if (i < n-1 && isOpen(i+1, j)) {
            uf.union(encode(i, j), encode(i+1, j));
        }
        if (j > 0 && isOpen(i, j-1)) {
            uf.union(encode(i, j), encode(i, j-1));
        }
        if (j < n-1 && isOpen(i, j+1)) {
            uf.union(encode(i, j), encode(i, j+1));
        }
    }

    // Returns true if site (i, j) is open, and false otherwise.
    public boolean isOpen(int i, int j) {
        if (i < 0 || i >= n) throw new IndexOutOfBoundsException("row index i out of bounds");
        if (j < 0 || j >= n) throw new IndexOutOfBoundsException("column index j out of bounds");

        // return true if open[i][j] is true
        return open[i][j];
    }

    // Returns true if site (i, j) is full, and false otherwise.
    public boolean isFull(int i, int j) {
        if (i < 0 || j<0 || i >= n || j>=n) throw new IndexOutOfBoundsException("row index i out of bounds");

        // if site (i, j) is open and full, return true
        if (isOpen(i, j)) {
            return true;
        }
        return false;
    }

    // Returns the number of open sites.
    public int numberOfOpenSites() {
        return openSites;
    }

    // Returns true if this system percolates, and false otherwise.
    public boolean percolates() {
        return uf.connected(0, n*n + 1);
    }

    // Returns an integer ID (1...n) for site (i, j).
    private int encode(int i, int j) {
        return i*n + j + 1;
    }

    // Unit tests the data type. [DO NOT EDIT]
    public static void main(String[] args) {
        String filename = args[0];
        In in = new In(filename);
        int n = in.readInt();
        UFPercolation perc = new UFPercolation(n);
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