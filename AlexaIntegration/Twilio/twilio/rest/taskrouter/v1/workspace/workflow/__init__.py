# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics import WorkflowCumulativeStatisticsList
from twilio.rest.taskrouter.v1.workspace.workflow.workflow_real_time_statistics import WorkflowRealTimeStatisticsList
from twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics import WorkflowStatisticsList


class WorkflowList(ListResource):
    """  """

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkflowList

        :param Version version: Version that contains the resource
        :param workspace_sid: The ID of the Workspace that contains this Workflow

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowList
        """
        super(WorkflowList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workflows'.format(**self._solution)

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams WorkflowInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: Human readable description of this Workflow
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists WorkflowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: Human readable description of this Workflow
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance]
        """
        return list(self.stream(friendly_name=friendly_name, limit=limit, page_size=page_size, ))

    def page(self, friendly_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkflowInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Human readable description of this Workflow
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowPage
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return WorkflowPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkflowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WorkflowPage(self._version, response, self._solution)

    def create(self, friendly_name, configuration,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               task_reservation_timeout=values.unset):
        """
        Create a new WorkflowInstance

        :param unicode friendly_name: A string representing a human readable name for this Workflow.
        :param unicode configuration: JSON document configuring the rules for this Workflow.
        :param unicode assignment_callback_url: A valid URL for the application that will process task assignment events.
        :param unicode fallback_assignment_callback_url: If the request to the AssignmentCallbackUrl fails, the assignment callback will be made to this URL.
        :param unicode task_reservation_timeout: An integer value controlling how long in seconds TaskRouter will wait for a confirmation response from your application after assigning a Task to a worker.

        :returns: Newly created WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Configuration': configuration,
            'AssignmentCallbackUrl': assignment_callback_url,
            'FallbackAssignmentCallbackUrl': fallback_assignment_callback_url,
            'TaskReservationTimeout': task_reservation_timeout,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return WorkflowInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], )

    def get(self, sid):
        """
        Constructs a WorkflowContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowContext
        """
        return WorkflowContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a WorkflowContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowContext
        """
        return WorkflowContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowList>'


class WorkflowPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WorkflowPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The ID of the Workspace that contains this Workflow

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowPage
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowPage
        """
        super(WorkflowPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkflowInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        """
        return WorkflowInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowPage>'


class WorkflowContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the WorkflowContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowContext
        """
        super(WorkflowContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'sid': sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workflows/{sid}'.format(**self._solution)

        # Dependents
        self._statistics = None
        self._real_time_statistics = None
        self._cumulative_statistics = None

    def fetch(self):
        """
        Fetch a WorkflowInstance

        :returns: Fetched WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WorkflowInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        """
        Update the WorkflowInstance

        :param unicode friendly_name: A string representing a human readable name for this Workflow.
        :param unicode assignment_callback_url: A valid URL for the application that will process task assignment events.
        :param unicode fallback_assignment_callback_url: If the request to the AssignmentCallbackUrl fails, the assignment callback will be made to this URL.
        :param unicode configuration: JSON document configuring the rules for this Workflow.
        :param unicode task_reservation_timeout: An integer value controlling how long in seconds TaskRouter will wait for a confirmation response from your application after assigning a Task to a worker.

        :returns: Updated WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'AssignmentCallbackUrl': assignment_callback_url,
            'FallbackAssignmentCallbackUrl': fallback_assignment_callback_url,
            'Configuration': configuration,
            'TaskReservationTimeout': task_reservation_timeout,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return WorkflowInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the WorkflowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkflowStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                workflow_sid=self._solution['sid'],
            )
        return self._statistics

    @property
    def real_time_statistics(self):
        """
        Access the real_time_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_real_time_statistics.WorkflowRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_real_time_statistics.WorkflowRealTimeStatisticsList
        """
        if self._real_time_statistics is None:
            self._real_time_statistics = WorkflowRealTimeStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                workflow_sid=self._solution['sid'],
            )
        return self._real_time_statistics

    @property
    def cumulative_statistics(self):
        """
        Access the cumulative_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsList
        """
        if self._cumulative_statistics is None:
            self._cumulative_statistics = WorkflowCumulativeStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                workflow_sid=self._solution['sid'],
            )
        return self._cumulative_statistics

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowContext {}>'.format(context)


class WorkflowInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid, sid=None):
        """
        Initialize the WorkflowInstance

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        """
        super(WorkflowInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'assignment_callback_url': payload['assignment_callback_url'],
            'configuration': payload['configuration'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'document_content_type': payload['document_content_type'],
            'fallback_assignment_callback_url': payload['fallback_assignment_callback_url'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'task_reservation_timeout': deserialize.integer(payload['task_reservation_timeout']),
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkflowContext for this WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowContext
        """
        if self._context is None:
            self._context = WorkflowContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The ID of the account that owns this Workflow
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def assignment_callback_url(self):
        """
        :returns: The URL that will be called whenever a task managed by this Workflow is assigned to a Worker.
        :rtype: unicode
        """
        return self._properties['assignment_callback_url']

    @property
    def configuration(self):
        """
        :returns: JSON document configuring the rules for this Workflow.
        :rtype: unicode
        """
        return self._properties['configuration']

    @property
    def date_created(self):
        """
        :returns: The date this workflow was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this workflow was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def document_content_type(self):
        """
        :returns: The document_content_type
        :rtype: unicode
        """
        return self._properties['document_content_type']

    @property
    def fallback_assignment_callback_url(self):
        """
        :returns: If the request to the AssignmentCallbackUrl fails, the assignment callback will be made to this URL.
        :rtype: unicode
        """
        return self._properties['fallback_assignment_callback_url']

    @property
    def friendly_name(self):
        """
        :returns: Human readable description of this Workflow
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The unique ID of the Workflow
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def task_reservation_timeout(self):
        """
        :returns: Determines how long TaskRouter will wait for a confirmation response from your application after assigning a Task to a worker.
        :rtype: unicode
        """
        return self._properties['task_reservation_timeout']

    @property
    def workspace_sid(self):
        """
        :returns: The ID of the Workspace that contains this Workflow
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a WorkflowInstance

        :returns: Fetched WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        """
        Update the WorkflowInstance

        :param unicode friendly_name: A string representing a human readable name for this Workflow.
        :param unicode assignment_callback_url: A valid URL for the application that will process task assignment events.
        :param unicode fallback_assignment_callback_url: If the request to the AssignmentCallbackUrl fails, the assignment callback will be made to this URL.
        :param unicode configuration: JSON document configuring the rules for this Workflow.
        :param unicode task_reservation_timeout: An integer value controlling how long in seconds TaskRouter will wait for a confirmation response from your application after assigning a Task to a worker.

        :returns: Updated WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            assignment_callback_url=assignment_callback_url,
            fallback_assignment_callback_url=fallback_assignment_callback_url,
            configuration=configuration,
            task_reservation_timeout=task_reservation_timeout,
        )

    def delete(self):
        """
        Deletes the WorkflowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsList
        """
        return self._proxy.statistics

    @property
    def real_time_statistics(self):
        """
        Access the real_time_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_real_time_statistics.WorkflowRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_real_time_statistics.WorkflowRealTimeStatisticsList
        """
        return self._proxy.real_time_statistics

    @property
    def cumulative_statistics(self):
        """
        Access the cumulative_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsList
        """
        return self._proxy.cumulative_statistics

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowInstance {}>'.format(context)
