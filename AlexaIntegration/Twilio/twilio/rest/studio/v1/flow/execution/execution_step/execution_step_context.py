# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ExecutionStepContextList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, flow_sid, execution_sid, step_sid):
        """
        Initialize the ExecutionStepContextList

        :param Version version: Version that contains the resource
        :param flow_sid: The flow_sid
        :param execution_sid: The execution_sid
        :param step_sid: The step_sid

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        """
        super(ExecutionStepContextList, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, 'step_sid': step_sid, }

    def get(self):
        """
        Constructs a ExecutionStepContextContext

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        return ExecutionStepContextContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __call__(self):
        """
        Constructs a ExecutionStepContextContext

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        return ExecutionStepContextContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionStepContextList>'


class ExecutionStepContextPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the ExecutionStepContextPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param flow_sid: The flow_sid
        :param execution_sid: The execution_sid
        :param step_sid: The step_sid

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextPage
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextPage
        """
        super(ExecutionStepContextPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ExecutionStepContextInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        """
        return ExecutionStepContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionStepContextPage>'


class ExecutionStepContextContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, flow_sid, execution_sid, step_sid):
        """
        Initialize the ExecutionStepContextContext

        :param Version version: Version that contains the resource
        :param flow_sid: The flow_sid
        :param execution_sid: The execution_sid
        :param step_sid: The step_sid

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        super(ExecutionStepContextContext, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, 'step_sid': step_sid, }
        self._uri = '/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ExecutionStepContextInstance

        :returns: Fetched ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ExecutionStepContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            step_sid=self._solution['step_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionStepContextContext {}>'.format(context)


class ExecutionStepContextInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, flow_sid, execution_sid, step_sid):
        """
        Initialize the ExecutionStepContextInstance

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        """
        super(ExecutionStepContextInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'context': payload['context'],
            'execution_sid': payload['execution_sid'],
            'flow_sid': payload['flow_sid'],
            'step_sid': payload['step_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, 'step_sid': step_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ExecutionStepContextContext for this ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        if self._context is None:
            self._context = ExecutionStepContextContext(
                self._version,
                flow_sid=self._solution['flow_sid'],
                execution_sid=self._solution['execution_sid'],
                step_sid=self._solution['step_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def context(self):
        """
        :returns: The context
        :rtype: dict
        """
        return self._properties['context']

    @property
    def execution_sid(self):
        """
        :returns: The execution_sid
        :rtype: unicode
        """
        return self._properties['execution_sid']

    @property
    def flow_sid(self):
        """
        :returns: The flow_sid
        :rtype: unicode
        """
        return self._properties['flow_sid']

    @property
    def step_sid(self):
        """
        :returns: The step_sid
        :rtype: unicode
        """
        return self._properties['step_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a ExecutionStepContextInstance

        :returns: Fetched ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionStepContextInstance {}>'.format(context)
