# impact-grafana-mongodb

This repository hosts a toy example of a Grafana dashboard with mongodb datasource for impact simulations. 

Requirements:
- MongoDB
- conda


First create the project python environment. This will install the pymongo driver.

```
$ conda env create -f environment.yml
```

Now activate: 

```
$ conda activate impact-dashboard
```


Now, for surfacing the MongoDB data with Grafana, we require a designated data source. The Grafana [MongoDB plugin](https://grafana.com/grafana/plugins/grafana-mongodb-datasource/?tab=installation) is at present enterprise; however, a proxy plugin can be found in this [repository](https://github.com/JamesOsgood/mongodb-grafana).

To register this plugin with Grafana, use the following steps:

```
$ cd /usr/local/var/lib/grafana/plugins 
$ git clone https://github.com/JamesOsgood/mongodb-grafana.git
$ brew services restart grafana 
$ cd /usr/local/var/lib/grafana/plugins/mongodb-grafana
$ npm run server
```

The MongoDB plugin will now be available in the datasource dropdown menu.