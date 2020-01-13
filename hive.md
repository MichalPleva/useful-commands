Drop tables name like:
```shell
hive -e "show tables 'temp_*'" | xargs -I '{}' hive -e 'drop table {}'
```
