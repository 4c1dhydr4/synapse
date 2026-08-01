from synapse.settings import DEBUG

def app_info(request):
	resolver = request.resolver_match
	context = {
		'DEBUG': DEBUG,
		'url_name': resolver.url_name if resolver else None,
		'app_name': resolver.app_name if resolver else None,
	}

	return context