---
tags:
  - "#toc"
links:
  - "[[README]]"
---
a catch all for stats related notes
#my-tag 

```toc
```

# TOC

- [[_ Statistics Terms and Definitions|Statistics Terms & Definitions]] 
```dataview
list FROM #toc AND [[Statistics]] WHERE !contains(file.folder, "terms") SORT file.name ASC
```
- [[probability/probability.ipynb]] #cleanup
- [[reference_sheets/reference_sheets.ipynb]] #cleanup
- [[statistics/lecture_notes.ipynb]] #cleanup 
```dataview
list FROM [[Statistics]] and !#toc WHERE !contains(file.folder, "terms") SORT file.name ASC
```

# uncategorized notes 
#cleanup
### raw data --> cleaned_data --> information --> knowledge --> wisdom
- **raw data**: unprocessed data
- **cleaned data**: raw data that has been cleaned & normalized
- **information**: processed data
- **knowledge**: information that is useful
- **wisdom**: knowledge that is actionable

**descriptive statistics** is about the transformation of cleaned data into information  
?ai gen - **inferential statistics** is about the transformation of information into knowledge  
?ai gen - **prescriptive statistics** is about the transformation of knowledge into wisdom  
