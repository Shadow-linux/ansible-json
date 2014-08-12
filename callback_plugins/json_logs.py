# adapted from https://gist.github.com/cliffano/9868180
import os
import time
import json
from datetime import datetime
from json import JSONEncoder

datenow = datetime.now()
datenow = datenow.strftime('%Y-%m-%d-%T')

if not os.path.exists("/var/log/ansible/hosts/json"):
    os.makedirs("/var/log/ansible/hosts/json")

def json_log(res, host):
  if type(res) == type(dict()):
    if 'verbose_override' not in res:
      res.update({"host": host})
      combined_json = JSONEncoder().encode(res)
      print(combined_json)
      filename = ("/var/log/ansible/hosts/json/"+host+datenow+".json")
      path = os.path.join(filename)
      fd = open(path, "a")
      fd.write(combined_json)
      fd.close()

class CallbackModule(object):

  def on_any(self, *args, **kwargs):
    pass

  def runner_on_failed(self, host, res, ignore_errors=False):
    json_log(res, host)

  def runner_on_ok(self, host, res):
    json_log(res, host)

  def runner_on_error(self, host, msg):
    pass

  def runner_on_skipped(self, host, item=None):
    pass

  def runner_on_unreachable(self, host, res):
    json_log(res, host)

  def runner_on_no_hosts(self):
    pass

  def runner_on_async_poll(self, host, res, jid, clock):
    json_log(res, host)

  def runner_on_async_ok(self, host, res, jid):
    json_log(res, host)

  def runner_on_async_failed(self, host, res, jid):
    json_log(res, host)

  def playbook_on_start(self):
    pass

  def playbook_on_notify(self, host, handler):
    pass

  def playbook_on_no_hosts_matched(self):
    pass

  def playbook_on_no_hosts_remaining(self):
    pass

  def playbook_on_task_start(self, name, is_conditional):
    pass

  def playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
    pass

  def playbook_on_setup(self):
    pass

  def playbook_on_import_for_host(self, host, imported_file):
    pass

  def playbook_on_not_import_for_host(self, host, missing_file):
    pass

  def playbook_on_play_start(self, pattern):
    pass

  def playbook_on_stats(self, stats):
    pass