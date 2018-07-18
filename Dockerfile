FROM python:alpine AS dashboard-generator
RUN pip install grafanalib
COPY templates /tmp/templates
RUN mkdir /tmp/rendered && \
	generate-dashboards /tmp/templates/* && \
	mv /tmp/templates/*.json /tmp/rendered

FROM grafana/grafana:latest

COPY provisioning /etc/grafana/provisioning
COPY dashboards /var/lib/grafana/dashboards
COPY --from=dashboard-generator /tmp/rendered /var/lib/grafana/dashboards
