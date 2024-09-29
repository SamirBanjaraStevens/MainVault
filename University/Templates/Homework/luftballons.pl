# !/usr/bin/perl
use strict;
use warnings;

for (1..99) { print $_ . " Luftballons\n"; }

my $string = "Hello World!";
print $string . "\n\n";

$string =~ s/Hello/Goodbye Cruel/;
print $string . "\n\n";

finale();
exit;

sub finale { print "Fin.\n"; }
\end{lstlisting}

\subsection{1. How many luftballons will be output by the Listing 1 above?}
Answer. 99 luftballons.

\subsection{2. Explain the regular expression in Listing 1.}
Answer. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent porttitor arcu luctus, imperdiet urna iaculis, mattis eros.

\end{document}