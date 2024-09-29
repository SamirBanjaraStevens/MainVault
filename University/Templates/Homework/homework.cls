%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Homework Class
% Maintainer: Samir Banjara
% 
% Document class to produce simple yet stylish homework submissions 
%
% This package is public domain, according to :
%    The Unlicense <https://unlicense.org>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Identification
\ProvidesClass{homework}[2024/09/28] 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Preliminary declarations:

% Define macros for instructor, course, and institution
\newcommand{\professor}[1]{ \newcommand{\professorloc}{#1} }
\newcommand{\class}[1]{ \newcommand{\classlocal}{#1} }
\newcommand{\institute}[1]{ \newcommand{\instituteloc}{#1} }
\newcommand{\pledge}[1]{ \newcommand{\pledgeloc}{#1} }

% Language customizations
\newcommand{\CourseLang}{Course}
\newcommand{\DateLang}{Due date}
\newcommand{\StudentLang}{Student name}
\newcommand{\ProfessorLang}{Professor}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Options

\DeclareOption{twocolumn}{\OptionNotUsed}
\DeclareOption{twoside}{\OptionNotUsed}

% Language customization options
\DeclareOption{spanish}{
    \renewcommand{\CourseLang}{Curso}
    \renewcommand{\ProfessorLang}{Docente}
    \renewcommand{\DateLang}{Fecha de entrega}
    \renewcommand{\StudentLang}{Nombre estudiante}
}

\PassOptionsToClass{a4paper}{article}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessOptions\relax

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Bulk Declarations

% Load the article class
\LoadClass{article}

% Require necessary packages
\RequirePackage{fontspec} % For system fonts with XeLaTeX
\RequirePackage{geometry} % For page size and margins
\RequirePackage{fancyhdr} % For custom headers and footers
\RequirePackage{titlesec} % For customizing section titles
\RequirePackage{listings} % For code listings
\RequirePackage{xcolor}   % For colors in code listings

% Geometry settings for decent margins
\geometry{left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm}

% Header and footer setup with fancyhdr
\fancyhead{}
\fancyfoot{}
\pagestyle{fancy}
\renewcommand{\headrulewidth}{0.4pt} 
\renewcommand{\footrulewidth}{0.4pt}
\fancyhead[RO] {\footnotesize\thepage}
\fancyhead[LO] {\footnotesize{\ifx\classlocal\undefined{}\else\itshape\classlocal{} --{} \fi}\makeatletter\@title\makeatother }
\fancyfoot[RO] {\footnotesize\itshape\makeatletter\@author\makeatother}

% Customizing the sections and subsections
\titleformat{\section}[block]{\normalsize\bfseries\filcenter}{\thesection.}{.3cm}{} 
\titleformat{\subsection}[runin]{\bfseries}{ \thesubsection.}{1mm}{}[.\quad]
\titleformat{\subsubsection}[runin]{\bfseries\itshape}{ \thesubsubsection.}{1mm}{}[.\quad]

% Define system fonts for XeLaTeX
\setmainfont{TeX Gyre Termes}   % Main font

% Custom title page
\renewcommand{\maketitle}{%
    \thispagestyle{plain}
    \begin{center}
        \ifx\instituteloc\undefined{}\else
            % Use main font with a different font size for the institute name
            {\fontsize{14pt}{16pt}\itshape \instituteloc} \\[4pt] % Change font size here
        \fi
        \ifx\pledgeloc\undefined{}\else
            {\itshape \pledgeloc} \\[12pt]
        \fi
        \hrule
        \vspace{15pt}
        {\LARGE \bfseries \@title} \\[5pt]
        \StudentLang: {\itshape \@author}
        \vspace{8pt}
        \hrule
        \vspace{10pt}
        \ifx\classlocal\undefined{}\else\CourseLang: {\itshape \classlocal{} \fi}
        \vspace{20pt}
    \end{center}
}

% Code listing environment setup
\lstset{
  basicstyle=\ttfamily,
  numbers=left,
  numberstyle=\tiny,
  stepnumber=1,
  numbersep=5pt,
  backgroundcolor=\color{lightgray},
  tabsize=2,
  showstringspaces=false,
  breaklines=true
}

% Environment for problems (centered, boxed, with padding)
\newsavebox{\problembox}
\newenvironment{problem}
    {\begin{center} \begin{lrbox}{\problembox}\begin{minipage}{.98\textwidth} \centering
     \vspace{10pt} % Add padding at the top
    }
    {\vspace{10pt} % Add padding at the bottom
    \end{minipage}\end{lrbox}\fbox{\usebox{\problembox}} \end{center} }

%%% End of the class file
\endinput