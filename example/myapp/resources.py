from django_declarative_apis import machinery, models
from django_declarative_apis.machinery import filtering


class MeResourceMixin:
    """Resource mixin for create and get endpoints
    """
    @machinery.endpoint_resource(
        type=models.OauthConsumer,
        filter={
            models.OauthConsumer:{
                'key': filtering.ALWAYS,
                'name': filtering.ALWAYS,
            }
        }
    )
    def resource(self):
        return models.OauthConsumer.objects.get(id=self.resource_id)


class MeDefinition(MeResourceMixin, machinery.ResourceEndpointDefinition):
    resource_model = models.OauthConsumer

    def is_authorized(self):
        return True

    @property
    def resource_id(self):
        """Overridden resource ID

        The resource_id is typically extracted from the URL. However, because the URL for this endpoint is /me,
        it needs to be translated into something meaningful.
        """
        return self.consumer.id


class MeUpdateDefinition(MeResourceMixin, machinery.ResourceUpdateEndpointDefinition):
    resource_model = models.OauthConsumer
    name = machinery.resource_field(required=False, type=str)
    secret = machinery.resource_field(required=False, type=str)

    def is_authorized(self):
        return True

    @property
    def resource_id(self):
        """Overridden resource ID

        The resource_id is typically extracted from the URL. However, because the URL for this endpoint is /me,
        it needs to be translated into something meaningful.
        """
        return self.consumer.id

    @machinery.task
    def save(self):
        self.resource.save()


class PingDefinition(machinery.BaseEndpointDefinition):
    """A basic "ping" endpoint
    """
    def is_authorized(self):
        """User should always be authorized
        """
        return True

    @property
    def resource(self):
        """The endpoint resource

        Endpoint resources can be implemented as either properties or machinery.endpoint_resources. 
        The latter will require filters to be defined.
        """
        return {'ping': 'pong'}
