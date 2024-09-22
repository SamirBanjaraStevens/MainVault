import java.util.Iterator;

import stdlib.StdOut;

// An immutable data type to systematically iterate over the first n primes.
public class Primes implements Iterable<Integer> {
    private int n; // need first n primes

    // Constructs a Primes object given the number of primes needed.
    public Primes(int n) {
        ...
    }

    // Returns an iterator to iterate over the first n primes.
    public Iterator<Integer> iterator() {
        ...
    }

    // Primes iterator.
    private class PrimesIterator implements Iterator<Integer> {
        private int count; // number of primes returned so far
        private int p;     // current prime

        // Constructs an iterator.
        public PrimesIterator() {
            ...
        }

        // Returns true if there are anymore primes to be iterated, and false otherwise.
        public boolean hasNext() {
            ...
        }

        // Returns the next prime.
        public Integer next() {
            // Increment count by 1.
            ...

            // As long as p is not prime, increment p by 1.
            ...

            // Return current value of p and increment it by 1.
            ...
        }

        // Returns true if x is a prime, and false otherwise.
        private boolean isPrime(int x) {
            for (int i = 2; i <= x / i; i++) {
                if (x % i == 0) {
                    return false;
                }
            }
            return true;
        }
    }

    // Unit tests the data type. [DO NOT EDIT]
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        for (int i : new Primes(n)) {
            StdOut.println(i);
        }
    }
}
