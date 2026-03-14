# Language Design

Book Code: CORE-04
Version: Core.Fundamentals.04.00
Last Updated: 2026-03-14
Status: Draft Complete

Bagian ini membahas prinsip desain bahasa Python, alasan di balik keputusan sintaks, serta trade-off yang membentuk pengalaman menulis kode Python.

## Tujuan Bagian Ini

- memahami filosofi desain Python dari perspektif bahasa
- menghubungkan keputusan desain dengan praktik coding sehari-hari
- membangun intuisi idiomatic Python berbasis prinsip, bukan hafalan
- mempersiapkan pembaca untuk topik runtime, object model, dan ecosystem

## Struktur Materi

| Urutan | Chapter Code | Topik | Lokasi |
|---|---|---|---|
| 01 | CORE-04-01 | Design Goals and Philosophy | [`01_design_goals_and_philosophy/`](01_design_goals_and_philosophy/README.md) |
| 02 | CORE-04-02 | The Zen of Python | [`02_the_zen_of_python/`](02_the_zen_of_python/README.md) |
| 03 | CORE-04-03 | Readability and Explicitness | [`03_readability_and_explicitness/`](03_readability_and_explicitness/README.md) |
| 04 | CORE-04-04 | Consistency and Practicality | [`04_consistency_and_practicality/`](04_consistency_and_practicality/README.md) |
| 05 | CORE-04-05 | Simple vs Complex | [`05_simple_vs_complex/`](05_simple_vs_complex/README.md) |
| 06 | CORE-04-06 | Mutability and Object Thinking | [`06_mutability_and_object_thinking/`](06_mutability_and_object_thinking/README.md) |
| 07 | CORE-04-07 | Duck Typing and Protocols | [`07_duck_typing_and_protocols/`](07_duck_typing_and_protocols/README.md) |
| 08 | CORE-04-08 | Errors as Part of Design | [`08_errors_as_part_of_design/`](08_errors_as_part_of_design/README.md) |
| 09 | CORE-04-09 | Batteries-included Mindset | [`09_batteries_included_mindset/`](09_batteries_included_mindset/README.md) |
| 10 | CORE-04-10 | Backward Compatibility and PEPs | [`10_backward_compatibility_and_peps/`](10_backward_compatibility_and_peps/README.md) |
| 11 | CORE-04-11 | Idiomatic Python and Style | [`11_idiomatic_python_and_style/`](11_idiomatic_python_and_style/README.md) |
| 12 | CORE-04-12 | Language Design Tradeoffs | [`12_language_design_tradeoffs/`](12_language_design_tradeoffs/README.md) |

## Aset Visual

Semua diagram bab disimpan pada:

- `core/02_language_design/assets/`

Format penamaan:

- `NN_<chapter_slug>.svg`

## Hubungan dengan Bagian Core Lainnya

Language Design menjadi fondasi konseptual untuk:

| Topik Lanjutan | Hubungan |
|---|---|
| Execution Model | memahami konsekuensi desain pada proses eksekusi |
| Object Model | memahami mengapa objek menjadi pusat desain Python |
| Modules and Import System | memahami keputusan namespace dan modularitas |
| Tooling | memahami alasan gaya idiomatik dan standardisasi |

## Referensi

- Python Tutorial
- Python Language Reference
- The Zen of Python (`import this`)
- Python Enhancement Proposals (PEP)
