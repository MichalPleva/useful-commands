Add/remove new kernel into Jupyter Notebook
```shell
#Add
source activate myenv  
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

#Remove
jupyter kernelspec uninstall myenv
``` 
