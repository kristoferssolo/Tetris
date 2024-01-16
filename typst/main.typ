#import "@preview/tablex:0.0.6": tablex, rowspanx, colspanx, cellx

#let indent = 1cm
#let indent-par(body) = par(h(indent) + body)

#let authors = ("Kristiāns Francis Cagulis, kc22015",)
#let title = [Kursa noslēguma projekts -- Tetris]

#set document(author: authors, title: title)
#set page(numbering: "1", number-align: center)
#set text( font: "New Computer Modern", lang: "lv", region: "LV")
#show link: set text(blue)
#show link: it => {underline(it)}
#show math.equation: set text(weight: 400)

  // Headings
#set heading(numbering: "1.1.")
  #show heading: it => {
    if it.level == 1 {
      text(14pt, align(center, upper(it)))
    } else {
      it
    }
}

#show figure: set par(justify: false) // disable justify for figures (tables)

#let indent = 1cm
#let indent-par(body) = par(h(indent) + body)

#set list(marker: ([•], [--], [\*], [·])) 
#set enum(numbering: "1aiA.")

  // Title row.
#align(center)[
  #block(text(weight: 700, 1.75em, title))
]

  // Author information.
#pad(
  top: 0.5em,
  bottom: 0.5em,
  x: 2em,
  grid(
    columns: (1fr,) * calc.min(3, authors.len()),
    gutter: 1em,
    ..authors.map(author => align(center, strong(author))),
  ),
)

#show par: set block(spacing: 1.5em) // Set 1.5em gap between paragraphs
#show heading: set block(spacing: 1.5em)
#set terms(separator: [ -- ])

  // Main body.
#set par(
  justify: true,
  leading: 1.5em,
  first-line-indent: indent,
)

/ Github: #link("https://github.com/kristoferssolo/Tetris")

= Apraksts
#indent-par([
Tetris ir klasiska spēle, kuru esmu izveidojis, izmantojot `pygame` bibliotēku.
Spēle spēlētājs var manipulēt ar krāsainām tetrimino #footnote[Tetramino ir polimino, kurš sastāv no četriem vienības kvadrātiem, kuri ir savienoti gar malām.] <tetromino> formām, cenšoties izveidot pilnas rindas, lai tās pazustu un gūtu punktus.
])

Spēles pamatfunkcijas:

+ *Grafika un dizains*: Spēle izmanto `pygame` bibliotēku, lai radītu vienkāršu lietotāja saskarni (@tetris).
+ *Kustība un kontroles*: Spēlētājs var vadīt tetrimino formas, izmantojot bulttaustiņus vai citas atbilstošas taustiņu kombinācijas (skat. `settings.toml` failu). Tetrimino var rotēties, pārvietoties pa labi vai pa kreisi, kā arī ātrāk nokrist uz leju.
+ *Punktu uzskaitīšana*: Spēlētājs nopelna punktus, izveidojot pilnas rindas. Jo vairāk rindas vienlaicīgi tiek izveidotas, jo lielāks ir punktu skaits.
+ *Spēles beigas*: Spēle beidzas, ja tetrimino formas sasniedz ekrāna augšējo malu un nevar turpināt nokrist.
+ *Dziesmas un skaņas efekti*: Spēlē ievietota dziesma un skaņas efekti.
+ *Augoša grūtības pakāpe*: Spēle piedāvā augošu grūtības pakāpi, kur ar pilnu rindu skaitu tetrimino kļūst ātrākas, radot spēlētājam arvien lielākus izaicinājumus.

#indent-par([
Sākotnēji plānoju arī iekļaut mākslīgo intelektu (AI), kas spētu patstāvīgi spēlēt Tetris.
AI ietvertu spēju izvēlēties optimālus gājienus un veikt stratēģiskus lēmumus, lai maksimāli palielinātu punktu skaitu.
Tomēr, saskāros ar tehniskām problēmām. Progress ir laikietilpīgāks nekā sākotnēji bija plānots un neuzspēju līdz galam to pabeig.
])



= Lietošanas instrukcija
== Palaišanas instrukcija

1. Klonējiet repozitoriju:
```bash
git clone https://github.com/kristoferssolo/Tetris
```

2. Pārejiet uz projekta direktoriju:
```bash
cd Tetris
```

3. Instalējiet nepieciešamās atkarības:
```bash
pip install .
```

4. Palaidiet spēli:
```bash
python main.py
```
vai
```bash
python -m tetris
```

== Iestatījumi
`settings.toml` ir konfigurācijas fails dažādu spēles aspektu pielāgošanai. Tajā var atrast un mainīt sekojošus parametrus.

=== Vispārīgi iestatījumi
#par(first-line-indent: 0cm, [
  / `pause`: definē taustiņu(-s), lai apturētu spēli.
  / `quit`: definē taustiņu(-s), lai izietu no spēles.
  / `colorscheme`: norāda spēles saskarnes krāsu shēmu. Iespējas ietver:
  - `tokyonight-day`
  - `tokyonight-moon`
  - `tokyonight-night`
  - `tokyonight-storm`
])

=== Kustību iestatījumi
#par(first-line-indent: 0cm, [
  / `left`: definē taustiņu(-s), lai pārvietotu tetromino @tetromino pa kreisi;
  / `right`: definē taustiņu(-s), lai pārvietotu tetromino pa labi;
  / `down`: definē taustiņu(-s), lai paātrinātu tetromino kustību uz leju (krišanu).
])

=== Rotācijas iestatījumi
#par(first-line-indent: 0cm, [
  / `cw (clockwise)`: definē taustiņu(-s), lai pagrieztu tetromino pulksteņrādītāja virzienā.
  / `ccw (counter-clockwise)`: definē taustiņu(-s), lai pagrieztu tetromino pretēji pulksteņrādītāja virzienam.
])

=== Papildus darbību iestatījumi
#par(first-line-indent: 0cm, [
  / `hold`: definē taustiņu(-s), lai uzglabātu tetromino (WIP #footnote[WIP (Work In Progress) -- nepabeigts darbs: darbs vai produkts, kas ir sākts, bet nav pabeigts vai gatavs.]<WIP>).
  / `drop`: definē taustiņ(-s), lai nekavējoties nomestu tetromino.
])

=== Skaņas iestatījumi
==== Mūzika
#par(first-line-indent: 0cm, [
  / `enabled`: norāda, vai mūzika ir iespējota.
  / `level`: norāda mūzikas skaļuma līmeni.
])

==== Skaņas efekti (SFX)
#par(first-line-indent: 0cm, [
  / `enabled`: norāda, vai ir iespējoti skaņas efekti.
  / `level`: norāda skaņas efektu skaļuma līmeni.
])


#figure(
  caption: [Tetris spēle ar `tokyonight-night` krāsu shēmu],
  placement: auto,
  image("img/tetris.png", width:70%)
) <tetris>
