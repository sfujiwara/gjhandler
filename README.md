# gjhandler

gjhandler is a simple log handler which generates new line delimited JSON for Cloud Logging and google-fluentd.

## Example

```python
import logging
import gjhandler

logger = logging.getLogger("gj_logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(gjhandler.GoogleJsonHandler(filename="log_test.json"))

logger.info("this is info")
logger.error("this is error")
```

### Resulting Outputs

```json
{"timestamp": {"seconds": 1472657255, "nanos": 154423952}, "message": "this is info", "severity": "INFO", "thread": 140735257141248}
{"timestamp": {"seconds": 1472657255, "nanos": 155013084}, "message": "this is error", "severity": "ERROR", "thread": 140735257141248}
```

## Setting for google-fluentd

```xml
<source>
  type tail
  format json
  path /var/log/python/*.log,/var/log/python/*.json
  read_from_head true
  tag python
</source>
```
