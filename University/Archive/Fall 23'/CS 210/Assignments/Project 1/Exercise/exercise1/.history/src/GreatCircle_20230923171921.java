import stdlib.StdOut;

public class GreatCircle {
    // Entry point.
    public static void main(String[] args) {
        // Accept x1 (double), y1 (double), x2 (double), and y2 (double) as command-line arguments.
        double x1 = Double.parseDouble(args[0]);
        double y1 = Double.parseDouble(args[1]);
        double x2 = Double.parseDouble(args[2]);
        double y2 = Double.parseDouble(args[3]);


        // Convert the angles to radians.
        x1 = Math.toRadians(x1);
        x2 = Math.toRadians(x2);
        y1 = Math.toRadians(y1);
        y2 = Math.toRadians(y2);


        // Calculate great-circle distance d.
        double func1 = Math.sin((x2 - x1) / 2);
        double func2 = Math.sin((y2 - y1) / 2);
        double func3 = Math.cos(x1);
        double func4 = Math.cos(x2);
        double func5 = Math.pow(func1, 2);
        double func6 = Math.pow(func2, 2);
        double func7 = func3 * func4 * func6;
        double func8 = func5 + func7;
        double func9 = Math.sqrt(func8);
        double d = 2 * 6371.0 * Math.asin(func9);


        // Write d to standard output.
        StdOut.println(d);
    }
}