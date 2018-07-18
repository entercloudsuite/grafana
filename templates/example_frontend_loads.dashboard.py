from grafanalib.core import *

dashboard = Dashboard(
  title="Example Frontend Stats",
  rows=[
    Row(panels=[
      Graph(
        title="Load",
        dataSource='Prometheus',
        targets=[
          Target(
            expr='avg(node_load1{job="haproxy"}) / count(count(node_cpu{job="haproxy"}) by (cpu))',
            legendFormat="Load 1",
            refId='A',
          ),
          Target(
            expr='avg(node_load5{job="haproxy"}) / count(count(node_cpu{job="haproxy"}) by (cpu))',
            legendFormat="Load 5",
            refId='B',
          ),
          Target(
            expr='avg(node_load15{job="haproxy"}) /  count(count(node_cpu{job="haproxy"}) by (cpu))',
            legendFormat="Load 15",
            refId='C',
          ),
        ],
        yAxes=single_y_axis(format=PERCENT_UNIT_FORMAT)
      ),
      Graph(
        title="Memory",
        dataSource='Prometheus',
        targets=[
          Target(
            expr='node_memory_MemTotal{job="haproxy"}',
            legendFormat="Total",
            refId='A',
          ),
          Target(
            expr='node_memory_MemAvailable{job="haproxy"}',
            legendFormat="Available",
            refId='B',
          )
        ],
        yAxes=single_y_axis(format=BYTES_FORMAT)
      ),
    ]),
    Row(panels=[
      Graph(
        title="Frontend responses by HTTP code",
        dataSource='Prometheus',
        targets=[
          Target(
            expr='sum(rate(haproxy_frontend_http_responses_total[5m])) by (code)',
            legendFormat="{{ code }}",
            refId='A',
          )
        ],
        yAxes=single_y_axis(format=SHORT_FORMAT)
      ),
      Graph(
        title="Backend responses by HTTP code",
        dataSource='Prometheus',
        targets=[
          Target(
            expr='sum(rate(haproxy_backend_http_responses_total[5m])) by (code)',
            legendFormat="{{ code }}",
            refId='A',
          )
        ],
        yAxes=single_y_axis(format=SHORT_FORMAT)
      ),
    ]),
  ],
).auto_panel_ids()
