The 16 non-bracket reference lists whose parsed-entry count fell below 0.8 of the year-token count were inspected by reading the reference section of the PDF and counting entry starts. Year tokens over-count entries because DOIs, URLs and date ranges contain years; once DOI and URL strings are removed, the token count is close to the entry count for complete lists.

| Submission | Parsed entries (before inspection) | Entries counted on inspection | Outcome |
|--:|--:|--:|:--|
| 54 | 10 | 10 | complete (DOIs inflate year tokens) |
| 78 | 17 | 17 | complete |
| 89 | 4 | 4 | complete |
| 127 | 23 | 23 | complete |
| 137 | 26 | 26 formatted entries plus the raw LaTeX bibliography source printed in the PDF | complete; source lines are not references |
| 173 | 20 | 20 | complete (appendix text follows the list) |
| 174 | 12 | 14 | 2 references merged by the parser; re-parsed with the author-pattern segmentation (14) |
| 214 | 23 | 23 | complete |
| 216 | 20 | 20 | complete (appendix text follows the list) |
| 237 | 25 | 25 | complete (appendix tables follow the list) |
| 273 | 1 | 3 | 2 references lost because the section-end heading was not recognised; re-parsed (3) |
| 274 | 2 | 3 | 1 reference missed in a three-entry bracket list; not recovered |
| 287 | 39 | 39 | complete |
| 289 | 23 | 23 | complete |
| 316 | 14 | 14 | complete |
| 329 | 6 | 6 | complete (appendix text follows the list) |

Of 16 inspected lists, 13 were complete and 3 had omissions totalling 5 references, of which 4 were recovered by re-parsing; 1 remains missing (submission 274).
