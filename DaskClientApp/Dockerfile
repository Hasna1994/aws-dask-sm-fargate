FROM continuumio/miniconda3:4.3.14

RUN conda update conda && conda install "conda=4.4.7"
RUN conda install --yes \
    python-blosc \
    cytoolz \
    dask  \
    distributed \
    nomkl \
    numpy \
    pandas \
    s3fs \
    lz4 \
    cloudpickle \
    && conda clean -tipsy


RUN mkdir /opt/app /etc/dask
COPY dask.yaml /etc/dask/

ADD my_script.py /opt/app

CMD [ "python", "/opt/app/my_script.py" ]

