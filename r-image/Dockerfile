FROM r-base:latest

COPY . /r-image
RUN Rscript -e "install.packages('plumber', repos='https://cran.ma.imperial.ac.uk/')"
EXPOSE 8000
CMD ["Rscript", "./r-image/entry.R"]
