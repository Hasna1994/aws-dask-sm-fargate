FROM daskdev/dask:2022.1.1-py3.8

ENV PYTHONHASHSEED 0
ENV PYTHONIOENCODING UTF-8

RUN pip install boto3==1.20.46

RUN conda install --yes -c conda-forge \
    dask-ml \
    s3fs

# Dumb init
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

# RUN mkdir -p /opt/app /etc/dask
# COPY dask_config/dask.yaml /etc/dask/

# Set up bootstrapping program and Spark configuration
# COPY program /opt/program
# RUN chmod +x /opt/program/bootstrap.py
#ENTRYPOINT ["/opt/program/bootstrap.py"]

COPY prepare.sh /usr/bin/prepare.sh
RUN chmod +x /usr/bin/prepare.sh

RUN mkdir /opt/app /etc/dask
COPY dask.yaml /etc/dask/

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/bin/prepare.sh"]

# FROM continuumio/miniconda3:4.3.14

# # Dumb init
# RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
# RUN chmod +x /usr/local/bin/dumb-init

# RUN conda update conda && conda install "conda=4.8.4"
# RUN conda install --yes \
#     python==3.6.10 \
#     cytoolz==0.8.2 \
#     dask==2.14  \
#     distributed==2.14 \
#     dask-glm==0.2.0 \
#     nomkl \
#     numpy \
#     pandas=1.0.1 \
#     && conda clean -tipsy
# RUN conda install --yes s3fs==0.4.0 -c conda-forge
# COPY prepare.sh /usr/bin/prepare.sh
# RUN chmod +x /usr/bin/prepare.sh

# RUN mkdir /opt/app /etc/dask
# COPY dask.yaml /etc/dask/

# ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/bin/prepare.sh"]
