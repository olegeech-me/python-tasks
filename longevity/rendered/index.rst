
.. _openstack_control_plane_longevity_report_mcp_2019.2.3:

**********************************************************
OpenStack control plane longevity report for MCP 2019.2.3
**********************************************************

:Abstract:

  This document includes OpenStack control plane longevity test results for MCP version 2019.2.3.
  All tests have been performed regarding
  :ref:`openstack_control_plane_longevity_test_plan`


Environment description
=======================

Hardware description
--------------------

MCP cluster was deployed on top of internal Mirantis OpenStack cluster (FIXME: internal-cloud-v2-us).
The following flavor were used:

.. table:: Flavors which were used to spawn MCP cluster

   +----------------+------------------------+------------+----------------+
   |DevCloud flavor |CPU vCores per instance |Memory (GB) |Disk space (GB) |
   +================+========================+============+================+
   |compact.ctl     |8                       |32          |35              |
   +----------------+------------------------+------------+----------------+
   |compact.msg     |8                       |32          |8               |
   +----------------+------------------------+------------+----------------+
   |compact.dbs     |8                       |16          |20              |
   +----------------+------------------------+------------+----------------+
   |compact.prx     |4                       |8           |8               |
   +----------------+------------------------+------------+----------------+
   |compact.cfg     |4                       |16          |80              |
   +----------------+------------------------+------------+----------------+
   |compact.mon     |4                       |8           |70              |
   +----------------+------------------------+------------+----------------+
   |compact.mtr     |4                       |8           |200             |
   +----------------+------------------------+------------+----------------+
   |compact.log     |4                       |8           |400             |
   +----------------+------------------------+------------+----------------+
   |compact.cid     |4                       |32          |100             |
   +----------------+------------------------+------------+----------------+
   |compact.cmp     |1                       |4           |50              |
   +----------------+------------------------+------------+----------------+
   |compact.gtw     |4                       |16          |20              |
   +----------------+------------------------+------------+----------------+
   |compact.kvm     |2                       |4           |20              |
   +----------------+------------------------+------------+----------------+


The following overcommmit ratios are set for compute nodes of underlay OpenStack cluster:

.. table:: overcommit ratios of underlay OpenStack

   +-----------------+-----------------+
   |Type of resource |Overcommit ratio |
   +=================+=================+
   |CPU_OVERCOMMIT   |FIXME            |
   +-----------------+-----------------+
   |RAM_OVERCOMMIT   |FIXME            |
   +-----------------+-----------------+
   |DISK_OVERCOMMIT  |FIXME            |
   +-----------------+-----------------+

Software description
--------------------

Initial context from `Cookiecutter initial context`_ application was used to generate MCP cluster model.

Deployment testing
==================

Time which was spend for deployment:

.. image:: raw_results/deployment-time.png
      :scale: 60


Functional testing
==================

To be sure that cluster works fine after deployment functional testing was performed using Rally scenarios with small
number of "times" and "concurrency".

| :download:`report-rally-nova.html <raw_results/functional-test-results.html>`

Testing process
===============

`Rally`_ tool was used to test the environment. `Rally`_ scenarios from `Rally scenarios`_ application were running at
the same time. `Rally`_ job parameters from `Rally job parameters`_ application were used.

As a result of this part we got the following HTML files:

From test run #1

  
| :download:`report-rally-nova-1.html <raw_results/report-rally-nova-1.html>`
| :download:`report-rally-neutron-1.html <raw_results/report-rally-neutron-1.html>`
| :download:`report-rally-cinder-1.html <raw_results/report-rally-cinder-1.html>`
| :download:`report-rally-glance-1.html <raw_results/report-rally-glance-1.html>`
| :download:`report-rally-grafana-1.html <raw_results/report-rally-grafana-1.html>`
| :download:`report-rally-elasticsearch-1.html <raw_results/report-rally-elasticsearch-1.html>`

From test run #2

  
| :download:`report-rally-nova-2.html <raw_results/report-rally-nova-2.html>`
| :download:`report-rally-neutron-2.html <raw_results/report-rally-neutron-2.html>`
| :download:`report-rally-cinder-2.html <raw_results/report-rally-cinder-2.html>`
| :download:`report-rally-glance-2.html <raw_results/report-rally-glance-2.html>`
| :download:`report-rally-grafana-2.html <raw_results/report-rally-grafana-2.html>`
| :download:`report-rally-elasticsearch-2.html <raw_results/report-rally-elasticsearch-2.html>`


Test results
============


Test run #1
-----------

FIX OR DELETEME: During the #1 run the following issues were found ...


Nova
````

.. image:: raw_results/nova-overview-1.png
      :scale: 100

.. image:: raw_results/nova-details-1.png
      :scale: 100

Neutron
```````

.. image:: raw_results/neutron-overview-1.png
      :scale: 100

.. image:: raw_results/neutron-details-1.png
      :scale: 100

Cinder
``````

.. image:: raw_results/cinder-overview-1.png
      :scale: 100

.. image:: raw_results/cinder-details-1.png
      :scale: 100

Glance
``````

.. image:: raw_results/glance-overview-1.png
      :scale: 100

.. image:: raw_results/glance-details-1.png
      :scale: 100

Grafana
```````

.. image:: raw_results/grafana-overview-1.png
      :scale: 100

.. image:: raw_results/grafana-details-1.png
      :scale: 100

Elasticsearch
`````````````

.. image:: raw_results/elasticsearch-overview-1.png
      :scale: 100

.. image:: raw_results/elasticsearch-details-1.png
      :scale: 100


Test run #2
-----------

FIX OR DELETEME: During the #2 run the following issues were found ...


Nova
````

.. image:: raw_results/nova-overview-2.png
      :scale: 100

.. image:: raw_results/nova-details-2.png
      :scale: 100

Neutron
```````

.. image:: raw_results/neutron-overview-2.png
      :scale: 100

.. image:: raw_results/neutron-details-2.png
      :scale: 100

Cinder
``````

.. image:: raw_results/cinder-overview-2.png
      :scale: 100

.. image:: raw_results/cinder-details-2.png
      :scale: 100

Glance
``````

.. image:: raw_results/glance-overview-2.png
      :scale: 100

.. image:: raw_results/glance-details-2.png
      :scale: 100

Grafana
```````

.. image:: raw_results/grafana-overview-2.png
      :scale: 100

.. image:: raw_results/grafana-details-2.png
      :scale: 100

Elasticsearch
`````````````

.. image:: raw_results/elasticsearch-overview-2.png
      :scale: 100

.. image:: raw_results/elasticsearch-details-2.png
      :scale: 100


Product issues which have been found during the tests
=====================================================

.. table:: Product issues which have been found during the tests

 +-------------------------------+---------------------------------------------+
 |Issue description              |Root cause, Link                             |
 +===============================+=============================================+
 || FIXME OR DELETEME            || FIXME OR DELETEME                          |
 +-------------------------------+---------------------------------------------+

Applications
============

Cookiecutter initial context
----------------------------

.. literalinclude:: configs/MCP/initial_context.yaml
    :language: yaml

Rally job parameters
--------------------

.. literalinclude:: configs/rally/job-params-long.yaml
    :language: yaml

Rally scenarios
---------------

- Nova

.. literalinclude:: configs/rally/nova.yaml
    :language: yaml

- Neutron

.. literalinclude:: configs/rally/neutron.yaml
    :language: yaml

- Cinder

.. literalinclude:: configs/rally/cinder.yaml
    :language: yaml

- Glance

.. literalinclude:: configs/rally/glance.yaml
    :language: yaml

- Grafana

.. literalinclude:: configs/rally/grafana.yaml
    :language: yaml

- Elasticsearch

.. literalinclude:: configs/rally/elasticsearch.yaml
    :language: yaml


.. references:

.. _Rally: https://rally.readthedocs.io
.. _PROD-26960: https://mirantis.jira.com/browse/PROD-26960
.. _PROD-25130: https://mirantis.jira.com/browse/PROD-25130
.. _PROD-27159: https://mirantis.jira.com/browse/PROD-27159