import dsa.WeightedQuickUnionUF;

import stdlib.In;

import stdlib.StdOut;


// An implementation of the Percolation API using the UF data structure.

public class UFPercolation implements Percolation {

    private final int n; // sys size

    private final boolean[][] open; // perc sys

    private int openSites; // # of open sites

    private final WeightedQuickUnionUF uf; // union find of perc sys

    private final WeightedQuickUnionUF backWash; // backwash

    private final int source; // top of site

    private final int sink; // bottom of site



    // Constructs an n x n percolation system, with all sites blocked.

    public UFPercolation(int n) {

        if (n <= 0) {

            throw new IllegalArgumentException("Illegal n");

        }

        this.n = n;

        this.open = new boolean[this.n][this.n];

        openSites = 0;

        uf = new WeightedQuickUnionUF((this.n * this.n + 2));

        backWash = new WeightedQuickUnionUF((this.n * this.n + 1));

        source = 0;

        sink = (this.n * this.n + 1);

    }


    // Opens site (i, j) if it is not already open.

    public void open(int i, int j) {

        if (i < 0 || j < 0 || i >= this.n || j >= this.n) {

            throw new IndexOutOfBoundsException("Illegal i or j");

        }

        if (!isOpen(i, j)) {

            open[i][j] = true;

            openSites++;

        }

        if (i == 0) {

            uf.union(encode(i, j), source);

            backWash.union(encode(i, j), source);

        }

        if (i == this.n -1) {

            uf.union(encode(i, j), sink);

        }

        if (i + 1 < this.n) {

            if (isOpen(i + 1, j)) {

                uf.union(encode(i, j), encode(i + 1, j));

                backWash.union(encode(i, j), encode(i + 1, j));

            }

        }

        if (j + 1 < this.n) {

            if (isOpen(i, j +1)) {

                uf.union(encode(i, j), encode(i, j + 1));

                backWash.union(encode(i, j), encode(i, j + 1));

            }

        }

        if (j - 1 >= 0) {

            if (isOpen(i, j - 1)) {

                uf.union(encode(i, j), encode(i, j - 1));

                backWash.union(encode(i, j), encode(i, j - 1));

            }

        }

        if (i - 1 >= 0) {

            if (isOpen(i - 1, j)) {

                uf.union(encode(i, j), encode(i - 1, j));

                backWash.union(encode(i, j), encode(i - 1, j));

            }

        }

    }


    // Returns true if site (i, j) is open, and false otherwise.

    public boolean isOpen(int i, int j) {

        if (i < 0 || j < 0 || i >= this.n || j >= this.n) {

            throw new IndexOutOfBoundsException("Illegal i or j");

        }

        return open[i][j];

    }


    // Returns true if site (i, j) is full, and false otherwise.

    public boolean isFull(int i, int j) {

        if (i < 0 || j < 0 || i >= this.n || j >= this.n) {

            throw new IndexOutOfBoundsException("Illegal i or j");

        }

        if (isOpen(i, j)) {

            return backWash.connected(encode(i, j), source);

        }

        return false;

    }


    // Returns the number of open sites.

    public int numberOfOpenSites() {

        return openSites;

    }


    // Returns true if this system percolates, and false otherwise.

    public boolean percolates() {

        return uf.connected(source, sink);

    }


    // Returns an integer ID (1...n) for site (i, j).

    private int encode(int i, int j) {

        return this.n * i + j + 1;

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
