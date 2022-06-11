# a. Start a base image with From
FROM python:3.8
# b. Update package manager and installed required packages

WORKDIR  /app
# d. Use COPY to copy files into /app directory
COPY . .
# b1. Pip install upgrade without cache requirements

# ENV name=63724_build

RUN pip install --upgrade --no-cache-dir -r ./requirements.txt
# i. Use VOLUME to allow the container to save data


# f. Use entry point to run default command

ENTRYPOINT ["uvicorn", "main:app"]
# g. Use CMD to run another default command

CMD ["--host", "0.0.0.0", "--port", "3000"]
# h. Use EXPOSE to docement the port the container exposes

EXPOSE 63724

VOLUME /database_volume

# j. Build docker image with $docker build -t mydockers .

# k. Run docker image $docker run -d --name mikeandtina -p 80:3000

# l. Build the docker image and upload it to DockerHub. Add the DockerHub 
# locations to a comment
# https://hub.docker.com/repository/docker/chobecalmbar/mydockerapp

