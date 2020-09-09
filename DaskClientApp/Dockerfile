FROM continuumio/miniconda3:4.3.14

RUN conda update conda && conda install "conda=4.8.4"
RUN conda install --yes \
    python==3.6.10 \
    cytoolz==0.8.2 \
    dask==2.14  \
    distributed==2.14 \
    dask-glm==0.2.0 \
    nomkl \
    numpy \
    pandas=1.0.1 \
    && conda clean -tipsy
RUN conda install --yes s3fs==0.4.0 -c conda-forge

RUN mkdir /opt/app /etc/dask
COPY dask.yaml /etc/dask/

ADD my_script.py /opt/app

CMD [ "python", "/opt/app/my_script.py" ]

