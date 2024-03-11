#### dataviews:

###### example: query #research-topic

blocks should be assigned the `dataview` type in order to run the query. I want to show the query itself though, so the `dataview` type is not added to the following code blocks

```
list from #research-topic
```

```
LIST
FROM ![[Statistics]] 
	AND !#toc 
WHERE contains(file.folder, this.file.folder)
	AND !contains(file.folder, "terms") 
SORT file.name ASC
```
