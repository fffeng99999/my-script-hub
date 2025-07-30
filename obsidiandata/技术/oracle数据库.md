```sql

CREATE OR REPLACE DIRECTORY DATA_PUMP_DIR AS 'E:\export_dir';
GRANT READ, WRITE ON DIRECTORY DATA_PUMP_DIR TO yonbip3;



```

```bash
set ORACLE_SID=ORCL
expdp yonbip3/NCC10 dumpfile=NNC_FULL.dmp logfile=expdp_NNC.log directory=DATA_PUMP_DIR full=y
```