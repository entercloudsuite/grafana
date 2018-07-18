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
            expr='avg(node_load1{job="haproxy"}) / count(count(node_cpu{job="haproxy"}) by (cpu)) * 100',
            legendFormat="Load 1",
            refId='A',
          ),
          Target(
            expr='avg(node_load5{job="haproxy"}) / count(count(node_cpu{job="haproxy"}) by (cpu)) * 100',
            legendFormat="Load 5",
            refId='B',
          ),
          Target(
            expr='avg(node_load15{job="haproxy"}) /  count(count(node_cpu{job="haproxy"}) by (cpu)) * 100',
            legendFormat="Load 15",
            refId='C',
          ),
        ],
        yAxes=single_y_axis(format=PERCENT_UNIT_FORMAT)
      ),
    ]),
    Row(panels=[
      Graph(
        title="Frontend memory",
        dataSource='Prometheus',
        targets=[
          Target(
            expr='node_memory_MemTotal{job="haproxy"}',
            legendFormat="Total",
            refId='A',
          ),
          Target(
            expr='node_memory_MemFree{job="haproxy"}',
            legendFormat="Free",
            refId='B',
          )
        ],
        yAxes=single_y_axis(format=BYTES_FORMAT)
      ),
    ]),
  ],
).auto_panel_ids()
