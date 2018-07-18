from grafanalib.core import *


dashboard = Dashboard(
  title="Example Frontend Stats",
  rows=[
    Row(panels=[
      Graph(
        title="Frontend loads",
        dataSource='Prometheus',
        targets=[
          Target(
            expr='node_load1{job="haproxy"}',
            legendFormat="Load 1",
            refId='A',
          ),
          Target(
            expr='node_load5{job="haproxy"}',
            legendFormat="Load 5",
            refId='B',
          ),
          Target(
            expr='node_load15{job="haproxy"}',
            legendFormat="Load 15",
            refId='C',
          ),
        ],
        yAxes=[
          YAxis(format=OPS_FORMAT),
          YAxis(format=SHORT_FORMAT),
        ],
      ),
    ]),
  ],
).auto_panel_ids()
