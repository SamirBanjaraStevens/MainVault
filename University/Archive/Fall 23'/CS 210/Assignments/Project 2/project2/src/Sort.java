import dsa.LinkedStack;

import stdlib.StdIn;
import stdlib.StdOut;

public class Sort {
    // Entry point.
    public static void main(String[] args) {
        LinkedDeque<String> d = new LinkedDeque<>();
        while (!StdIn.isEmpty()) {
            String w = StdIn.readString();
            if (d.isEmpty()) {
                d.addFirst(w);
            } else if (less(w, d.peekFirst()) || w.equals(d.peekFirst())) {
                d.addFirst(w);
            } else if (less(d.peekLast(), w) || w.equals(d.peekLast())) {
                d.addLast(w);
            } else {
                LinkedStack<String> s = new LinkedStack<>();
                while (less(d.peekFirst(), w)) {
                    s.push(d.removeFirst());
                }
                d.addFirst(w);
                while (!s.isEmpty()) {
                    d.addFirst(s.pop());
                }
            }
        }
        for (String i : d) {
            StdOut.println(i);
        }
    }

    // Returns true if v is less than w according to their lexicographic order, and false otherwise.
    private static boolean less(String v, String w) {
        return v.compareTo(w) < 0;
    }
}
