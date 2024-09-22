import stdlib.StdOut;

public class Sample {
    // Entry point.
    public static void main(String[] args) {
        int lo = Integer.parseInt(args[0]);
        int hi = Integer.parseInt(args[1]);
        int k = Integer.parseInt(args[2]);
        String mode = args[3];

        if (!mode.equals("+") && !mode.equals("-")) {
            throw new IllegalArgumentException("Illegal mode");
        }

        RandomQueue<Integer> queue = new RandomQueue<>();
        for (int i = lo; i <= hi; i++) {
            queue.enqueue(i);
        }

        if (mode.equals("+")) {
            for (int i = 0; i < k; i++) {
                StdOut.println(queue.sample());
            }
        } else {
            if (k > hi - lo + 1) {
                throw new IllegalArgumentException("k must be <= hi - lo + 1");
            }

            for (int i = 0; i < k; i++) {
                StdOut.println(queue.dequeue());
            }
        }    
    }
}



