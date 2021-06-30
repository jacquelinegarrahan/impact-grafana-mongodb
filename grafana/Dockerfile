
FROM grafana/grafana:latest-ubuntu

USER root
ADD ./provisioning /etc/grafana/provisioning
ADD ./config.ini /etc/grafana/config.ini
ADD ./dashboards /var/lib/grafana/dashboards
ADD run_image.sh /opt/run_image.sh

ENV GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS grafana-mongodb-datasource,ae3e-plotly-panel,briangann-datatable-panel

RUN apt-get update && apt-get install -y -q --no-install-recommends git npm yarn \
    && curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.35.3/install.sh -o install_nvm.sh \
    && bash install_nvm.sh \
    && git clone https://github.com/JamesOsgood/mongodb-grafana $GF_PATHS_PLUGINS/mongodb-grafana \
    && rm -rf $GF_PATHS_PLUGINS/mongodb-grafana\.git \
    && npm install --silent --prefix $GF_PATHS_PLUGINS/mongodb-grafana \
    && npm cache clean --force --prefix $GF_PATHS_PLUGINS/mongodb-grafana \
    && chmod +x /opt/run_image.sh 

ENV NVM_DIR /usr/local/nvm

WORKDIR /var/lib/grafana/plugins

RUN git clone https://github.com/jacquelinegarrahan/ae3e-plotly-panel.git \
    && cd ae3e-plotly-panel \
    && git checkout variable-update \
    && . $NVM_DIR/nvm.sh \
    && nvm install 10 \
    && nvm use 10 \
    && yarn install \
    && yarn build \
    && cd /var/lib/grafana/plugins \
    && apk del --no-cache git 

#COPY ae3e-plotly-panel $GF_PATHS_PLUGINS/ae3e-plotly-panel

USER grafana

CMD /opt/run_image.sh