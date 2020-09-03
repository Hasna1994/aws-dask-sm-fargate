FROM continuumio/miniconda3:4.3.14

# Dumb init
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN conda update conda && conda install "conda=4.4.7"
RUN conda install --yes \
    python-blosc \
    python==3.7.7 \
    cytoolz \
    dask==2.25  \
    distributed==2.25 \
    nomkl \
    numpy \
    pandas \
    && conda clean -tipsy
RUN conda install --yes s3fs==0.3.0 -c conda-forge
RUN conda install --yes joblib==0.16 -c conda-forge
RUN conda install --yes scikit-learn==0.23 -c conda-forge
RUN conda install --yes dask-glm==0.2.0 -c conda-forge
COPY prepare.sh /usr/bin/prepare.sh
RUN chmod +x /usr/bin/prepare.sh

RUN mkdir /opt/app /etc/dask
COPY dask.yaml /etc/dask/

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/bin/prepare.sh"]