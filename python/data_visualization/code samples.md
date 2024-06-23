
# hist box
``` python
# Defining the hist_box() function
def hist_box(data, col):
    f, (ax_box, ax_hist) = plt.subplots(
	    2, 
	    sharex=True, 
	    gridspec_kw={'height_ratios': (0.15, 0.85)}, 
	    figsize=(12, 6)
	)
    # Adding a graph in each part
    sns.boxplot(data=data, x=col, ax=ax_box, showmeans=True)
    sns.histplot(data=data, x=col, kde=True, ax=ax_hist)
    plt.show()
```
![[Pasted image 20240325030603.png]]

# heat map
``` python
cols_list = df.select_dtypes(include=np.number).columns.tolist()

plt.figure(figsize=(12, 7))
sns.heatmap(
	data[cols_list].corr(), 
	annot=True, 
	vmin=-1, 
	vmax=1, 
	fmt=".2f", 
	cmap="Spectral"
)
plt.show()
```
![[Pasted image 20240325031725.png]]

# stacked bar plot
``` python
# Defining the stacked_barplot() function
def stacked_barplot(data, predictor, target, figsize=(10,6)):
	(
		pd.crosstab(
			data[predictor],
			data[target],
			normalize='index'
		) * 100
	).plot(
		kind='bar',
		figsize=figsize,
		stacked=True
	)
	plt.legend(loc="lower right")
	plt.ylabel(target)
```
![[Pasted image 20240325044758.png]]

