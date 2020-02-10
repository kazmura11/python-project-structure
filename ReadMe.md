## Development Environment
Windows +　VSCode + Anaconda3 + Python3 + MongoDB

### Anaconda3
Download and install Anaconda3

### MongoDB
Download 
mongodb-win32-x86_64-2008plus-ssl-3.6.17-signed.msi
and install

Create  
`C:\Program Files\MongoDB\Server\3.6\bin\mongodb.conf`  
and then write
```yaml
net:
  bindIp: 127.0.0.1
  port: 27017
storage:
  dbPath: C:\Program Files\MongoDB\Server\3.6\data
  journal:
    enabled: true
systemLog:
  destination: file
  path: C:\Program Files\MongoDB\Server\3.6\logs\mongodb.log
  logAppend: true
```

### Add PATH Variable
Add `C:\Program Files\MongoDB\Server\3.6\bin` to System Environment variables.

### Register as a windows service
Run command prompt as administrator
```
> cd C:\Program Files\MongoDB\Server\3.6
> mkdir data
> mkdir logs
> type nul > logs\mongdb.log
> cd bin
> mongod.exe --config "C:\Program Files\MongoDB\Server\3.6\bin\mongodb.conf" --install --serviceName MongoDB
```
Run from services.msc

### Install python packages
pip install -r requirements.txt
pip install flake8 autopep8 coverage

### Install VSCode Extensions
#### Python
Install Microsoft's Python Extention from VS Marketplace

#### autoDocString
Install `autoDocString` from VS Marketplace

#### Coverage Gutters
Install `Coverage Gutters` from VS Marketplace

#### customize
Open `settings.json` from `Settings` by clicking on that tiny "Open Settings (JSON)" icon.
If you can't find the button, you can edit directly `%APPDATA%\Code\user\settings.json`.
```json
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "python.linting.lintOnSave": true,
    "python.linting.pylintEnabled": false,
    "python.linting.pep8Enabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--ignore=W293, W504",
        "--max-line-length=150",
        "--max-complexity=20"
    ],
    "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": [
        "--aggressive", "--aggressive",
    ],
    "autoDocstring.docstringFormat": "google",
    "coverage-gutters.coverageReportFileName": "**/coverage.xml",
    "coverage-gutters.showLineCoverage": true,
    "coverage-gutters.showRulerCoverage": true
```

### References
https://qiita.com/firedfly/items/00c34018581c6cec9b84
https://github.com/pistatium/about_python_logging
https://docs.python-guide.org/writing/structure/
