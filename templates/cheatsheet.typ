#import "components.typ": *

#let sheet-id = sys.inputs.at("sheet", default: "")
#if sheet-id == "" { panic("missing --input sheet=ID") }
#let data = yaml("../content/" + sheet-id + ".yaml")

#set page(
  paper: "a4",
  margin: (x: 12mm, top: 10mm, bottom: 10mm),
  footer: context [
    #set text(size: 6pt, fill: muted)
    #data.at("footer", default: data.title)
    #h(1fr)#counter(page).display("1 / 1", both: true)
  ],
)
#set text(font: "DejaVu Sans", size: 7.2pt, fill: ink, lang: "en")
#set par(leading: 1.5pt, justify: false)
#show raw: set text(font: "DejaVu Sans Mono", size: 6.6pt)

#let render-block(block-data) = {
  let kind = block-data.type
  if kind == "entries" { command-table(block-data.items) }
  else if kind == "text" { text(size: 7pt, block-data.text) }
  else if kind == "note" { callout(block-data.at("kind", default: "info"), block-data.text) }
  else if kind == "code" { code-block(block-data.text) }
  else if kind == "table" { compact-table(block-data.headers, block-data.rows) }
}

#let render-section(section) = {
  block(width: 100%, sticky: true, inset: (bottom: 2pt), stroke: (bottom: .8pt + ink))[
    #text(size: 9pt, weight: "bold", section.title)
  ]
  for item in section.blocks {
    v(2.5pt)
    render-block(item)
  }
  v(5pt)
}

#block(width: 100%)[
  #text(size: 20pt, weight: "bold", data.title)
  #if "subtitle" in data { [#h(5pt)#text(size: 9pt, fill: muted, data.subtitle)] }
  #line(length: 100%, stroke: 1.2pt + ink)
  #grid(columns: (1fr, auto), gutter: 5mm,
    text(size: 6.5pt, fill: muted, data.at("intro", default: "")),
    align(right)[
      #text(size: 6pt, fill: muted)[
        #if "version" in data { [v#data.version · ] }
        #if "updated" in data { [updated #data.updated] }
      ]
    ],
  )
  #if "verified_on" in data {
    let v = data.verified_on
    text(size: 5.8pt, fill: muted)[Verified #v.date#if "software" in v { [ · #v.software] }#if "host" in v { [ · #v.host] }]
  }
]
#v(4pt)

#columns(2, gutter: 6mm)[
  #for section in data.sections { render-section(section) }
]
