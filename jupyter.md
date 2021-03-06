Add/remove new kernel into Jupyter Notebook
```shell
#Add
source activate myenv  
#Install ipykernel
pip install ipykernel
python -m ipykernel install --user --name <myenv> --display-name "Python (<myenv>)"

#Remove
jupyter kernelspec uninstall <myenv>
``` 

Rendering notebook with scrolling ability:
```shell
jupyter nbconvert <ntname>.ipynb --to slides --SlidesExporter.reveal_scroll=True
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

Symbolic or soft link (files or directories, more flexible and self documenting):
```shell
#     Source                             Link
ln -s /home/myfolder/project /home/myfolder/xxx
```
Hard link (files only, less flexible and not self documenting):
```shell
#   Source                             Link
ln /home/myfolder/project /home/myfolder/xxx
```
