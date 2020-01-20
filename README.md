# pyspark-sql-project-template

With pipenv installed on Mac/Linux machine

Run:

`make run JOB_NAME=csvDataTransform CONF_PATH=/your_path/your_project_name/src/jobs `

on terminal to run a job, in this case `csvDataTransform`. The `CONF_PATH` indicate the directory
of jobs, which also contain the resources folder.

This is an improvement of [BogdanCojocar pyspark-project-template](https://github.com/BogdanCojocar/medium-articles/tree/master/pyspark-project-template) which used RDD. You can learn more about it [here](https://towardsdatascience.com/how-to-setup-the-pyspark-environment-for-development-with-good-software-engineering-practices-5fb457433a86).
