#let ink = rgb("#17212b")
#let muted = rgb("#56616d")
#let rule = rgb("#c9cfd4")
#let pale = rgb("#f1f3f5")

#let command-table(items) = table(
  columns: (42%, 58%),
  inset: (x: 2.2pt, y: 1.6pt),
  stroke: (x: none, y: .35pt + rule),
  align: (left, left),
  ..items.map(item => (
    text(font: "DejaVu Sans Mono", size: 6.8pt, fill: ink, item.command),
    text(size: 7pt, item.description),
  )).flatten(),
)

#let callout(kind, body) = {
  let colors = (
    info: (rgb("#e9f2f8"), rgb("#316b8d")),
    tip: (rgb("#edf5ed"), rgb("#367044")),
    warning: (rgb("#f8eeee"), rgb("#9a3e3e")),
  )
  let pair = colors.at(kind, default: colors.info)
  block(width: 100%, inset: 4pt, fill: pair.at(0), stroke: (left: 2pt + pair.at(1)), radius: 1pt)[
    #text(size: 7pt, weight: "semibold", fill: pair.at(1), upper(kind))
    #h(3pt)#text(size: 7pt, body)
  ]
}

#let compact-table(headers, rows) = table(
  columns: headers.len(),
  inset: 2pt,
  stroke: .35pt + rule,
  table.header(..headers.map(h => text(size: 6.8pt, weight: "bold", h))),
  ..rows.flatten().map(cell => text(size: 6.6pt, str(cell))),
)

#let code-block(body) = block(width: 100%, inset: 4pt, fill: pale, radius: 2pt)[
  #text(font: "DejaVu Sans Mono", size: 6.6pt, body)
]

