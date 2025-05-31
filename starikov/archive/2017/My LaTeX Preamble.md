# My LaTeX Preamble
One of the most valuable skills I have learned in the past year is undoubtedly [LaTeX](https://www.latex-project.org) — so much so that I have moved almost all of my notetaking and document writing to LaTeX or [Pandoc](http://pandoc.org).

However, with almost any markup language, I did run into friction: constantly importing headers and defining commands I used on an every-document basis. Some commands have become muscle memory; when I got compiler errors every time I forgot to redefine them, I became quite frustrated. So I caved: I made a preamble that I pre-appended to all of my LaTeX docs.

```LaTeX
\RequirePackage[l2tabu, orthodox]{nag}
\documentclass[12pt]{article}

\usepackage{amssymb,amsmath,verbatim,graphicx,microtype,units,booktabs}
\usepackage[margin=10pt, font=small, labelfont=bf, labelsep=endash]{caption}
\usepackage[colorlinks=true, pdfborder={0 0 0}]{hyperref}
\usepackage[utf8]{inputenc}

\usepackage{xcolor}
\newcommand{\shellcmd}[1]{\texttt{\colorbox{gray!30}{#1}}} % highlight shell or code commands
\newcommand{\todo}[2]{\textbf{\colorbox{red!50}{#1}}{\footnote{#2}}} % placeholder for something to do
\newcommand{\gray}{\rowcolor[gray]{.9}} % format a table row to make it more visible

\usepackage[left=1.15in, right=1.15in]{geometry}
\usepackage{titleps}
\newpagestyle{main}{
    \setheadrule{.4pt}
    \sethead{\sectiontitle}
            {}
            {Illya Starikov}
}
\pagestyle{main}

% *-------------------- Modify This As Needed --------------------* %
% \usepackage[top=0.5in, bottom=0.5in, left=0.5in, right=0.5in]{geometry}
% \pagestyle{empty}

\title{\todo{Title}{Insert title here.}}
\date{\today}
\author{Illya Starikov}
```

Then, I took it one step further. I occasionally make practice tests for students in Calculus and Physics, so I decided to make a command that acts as extensions of my preamble for tests.

```LaTeX
\usepackage{lastpage,ifthen}
\newboolean{key}
\setboolean{key}{true} % prints questions and answers
% \setboolean{key}{false} % prints questions only
\newcommand{\question}[2]{\item (#1 Points) #2}
\newcommand{\answer}[1]{\ifthenelse{\boolean{key}}{#1}{}}

% This must be filled out
\newcommand{\points}{0} % total number of points for the exam
\newcommand{\capped}{0\ } % the capping score, to offer a point or two bonus
\newcommand{\difference}{0\ } % the difference of the two
\newcommand{\timeallotted}{0 hour} % duration of the exam

\begin{document}
\section*{\answer{Key}}
Complete the following problems. 
In order to receive full credit,
please show all of your work and justify your answers.
You do not need to simplify your answers unless specifically instructed to do so.
You have \timeallotted. 
This is a closed-book, closed-notes exam.
No calculators or other electronic aids will be permitted.
If you are caught cheating, you will receive a zero grade for this exam.
Please check that your copy of this exam contains \pageref{LastPage} numbered pages and is correctly stapled.
The sum of the max points for all the questions is \points,
but note that the max exam score will be capped at \capped
(i.e., there is \difference bonus point(s), but you can't score more than 100\%). 
Best of luck.

\begin{enumerate}
\question{}{}
\answer{}

\end{enumerate}
\end{document}
```

Files with samples can be found on my [GitHub](https://github.com/IllyaStarikov), specifically [here](https://github.com/IllyaStarikov/latex_preamble).