% Clase de Carta de Presentación - Maldito ATS
\ProvidesClass{carta}[2026/08/26 Clase de Carta de Presentación]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}
}
\ProcessOptions\relax
\LoadClass{article}

% Paquetes
\usepackage[hmargin=2.2cm, vmargin=2.2cm]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage[usenames,dvipsnames]{xcolor}
\usepackage{titlesec}
\usepackage[absolute]{textpos}
\usepackage{fontspec,xltxtra,xunicode}

% Colores
\definecolor{fecha}{HTML}{666666}
\definecolor{primario}{HTML}{2b2b2b}
\definecolor{titulos}{HTML}{1a365d}
\definecolor{subtitulos}{HTML}{333333}

% Fuentes
\setmainfont[Color=primario, Path = OpenFonts/fonts/lato/,BoldItalicFont=Lato-RegIta,BoldFont=Lato-Reg,ItalicFont=Lato-LigIta]{Lato-Lig}
\setsansfont[Scale=MatchLowercase,Mapping=tex-text, Path = OpenFonts/fonts/raleway/]{Raleway-ExtraLight}

% Encabezado con Nombre y Contacto
\newcommand{\encabezadocarta}[3]{
\centering{
\fontsize{32pt}{40pt}
\fontspec[Path = OpenFonts/fonts/lato/]{Lato-Hai}\selectfont #1 
\fontspec[Path = OpenFonts/fonts/lato/]{Lato-Lig}\selectfont #2
} \\[4pt]
\centering{
\color{subtitulos}
\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Medium}\fontsize{10.5pt}{13pt}\selectfont #3}
\vspace{10pt}
\hrule height 0.5pt
\vspace{12pt}
}

% Destinatario
\newcommand{\destinatario}[2]{
\raggedright{
\color{subtitulos}
\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Bold}\fontsize{11pt}{14pt}\selectfont #1
\par
\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Regular}\fontsize{10.5pt}{13pt}\selectfont #2
}
\vspace{12pt}
}

% Cuerpo de la carta
\newcommand{\cuerpocarta}[1]{
\raggedright{
\color{primario}
\fontspec[Path = OpenFonts/fonts/lato/]{Lato-Lig}\fontsize{11pt}{15pt}\selectfont #1
}
\vspace{10pt}
}

% Despedida y Firma
\newcommand{\firmacarta}[2]{
\vspace{12pt}
\raggedright{
\color{primario}
\fontspec[Path = OpenFonts/fonts/lato/]{Lato-Lig}\fontsize{11pt}{15pt}\selectfont #1
\vspace{10pt}
\par
\fontspec[Path = OpenFonts/fonts/lato/]{Lato-Reg}\fontsize{11pt}{15pt}\selectfont #2
}
}
