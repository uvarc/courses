# Introduction to Docker - Workshop

In this workshop you will learn how to create and use Docker containers. Follow the lab instructions below at your own pace. Please raise your hand or get the attention of an instructor if you have any questions.

* Docker Operations
  * [Docker Commands](#docker-commands)
  * Creating Containers
  * Running Containers

- - -

## Docker Containers

### Install Docker
Docker is available for Windows, Mac, and Linux. Download the appropriate Docker Edition for your platform directly from Docker. We suggest the CE "Community Edition."

[Download Docker](https://www.docker.com/)

### Docker Commands
1. Make sure Docker is running. You should see an icon in your toolbar that indicates Docker's status.
2. Open a terminal or command-line prompt for the following steps.
3. Docker command reference. This will show you all the possible commands:

```bash
docker
```

4. List all container images you have downloaded:

```bash
docker images
```

5. Pull a container you want to run. In this case, let's run the `nginx` web server:

```bash
docker pull nginx
```

6. List all container images you have downloaded. You should now see the nginx image:

```
docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
nginx               latest              6b914bbcb89e        3 months ago        182 MB
```

7. Run a container image:

```bash
docker run -d nginx
```

This runs the container as a daemon (service). But you may want to expose the container to a specific port locally, so that you can interact with it.
For example, if you wanted to expose nginx locally over port 80, enter this:

```bash
docker run -d -p 8080:80 nginx
```

The -p 8080:80 flag publishes your local computer's port 8080 with the container's port 80.

Another useful flag for runtime is a volume mapping, so that your running container can read or write to portions of your local computer's filesystem.
So, extending the earlier command:

```bash
docker run -d -p 8080:80 -v /User/local/dir:/var/www/html nginx
```

8. View all running containers:

```
docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                    PORTS                    NAMES
1d17f542be53        rocker/rstudio      "/init"                  18 hours ago        Up 18 hours               0.0.0.0:8787->8787/tcp   elegant_banach
```

### Creating Containers

### Running Containers

### Conclusion
Congratulations! You have successfully done the following in Docker:

* A
* B
* C

