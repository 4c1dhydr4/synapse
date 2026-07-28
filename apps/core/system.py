import re
import subprocess
from django.core.cache import cache

class Git:
	def get_last_commit(self):
		try:
			result = result = subprocess.run(["git", "log", "-1", "--pretty=%B"], stdout=subprocess.PIPE, check=True)
			result = result.stdout.decode("utf-8").strip()
			return result
		except subprocess.CalledProcessError:
			return None

	def get_tms_version(self):
		message = self.get_last_commit()
		if message is None:
			return '1.0'

		pattern = r'(\d+\.\d+\.\d+)'
		match = re.search(pattern, message)
		if match:
			return match.group(1)
		else:
			return 'In-progress work'

	def deploy_log(self):
		from apps.security.managers import (LogManager,) # App Registry

		git_command = 'git log -1'
		process = subprocess.Popen(git_command.split(), stdout=subprocess.PIPE)
		git_output, error = process.communicate()
		git_output = git_output.decode("utf-8").split('\n')
		git_output = [ m for m in git_output if m]
		
		cache_key = 'deploy_{}'.format(git_output[-1].split(':')[0].replace(" ", ""))

		cached = cache.get(cache_key)

		if not cached:
			
			cache.set(cache_key, True)
			
			LogManager().log_deploy(release=git_output[-1], git_output=git_output)
