Add/remove new kernel into Jupyter Notebook
```shell
#Add
source activate myenv  
python -m ipykernel install --user --name <myenv> --display-name "Python (<myenv>)"

#Remove
jupyter kernelspec uninstall <myenv>
``` 

Common Directories and File Locations:

  * `JUPYTER_CONFIG_DIR` for config file location  
  * `JUPYTER_PATH` for datafile directory locations  
  * `JUPYTER_DATA_DIR` for data file location  
  * `JUPYTER_RUNTIME_DIR` for runtime file location  

Accessing through shell:
```shell
#All
jupyter --paths

#Specifically
jupyter --config-dir
jupyter --data-dir
jupyter --runtime-dir
```
