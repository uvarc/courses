# Introduction to Docker - Workshop

In this workshop you will learn how to create and use Docker containers. Follow the lab instructions below at your own pace. Please raise your hand or get the attention of an instructor if you have any questions.

* [Install Docker](#install-docker)
* [Docker Commands](#docker-commands)
* [Running Containers](#running-containers)
* [Creating Containers](#creating-containers)

- - -

## Docker Containers

### Install Docker
Docker is available for Windows, Mac, and Linux. Download the appropriate Docker Edition for your platform directly from Docker. We suggest the CE "Community Edition."

[Download Docker](https://www.docker.com/)

### Docker Commands
1. Make sure Docker is running. You should see an icon in your toolbar that indicates Docker's status.
2. Open a terminal or command-line prompt for the following steps.
3. Docker command reference. This will show you all possible commands:

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

8. View all running containers:

```
docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                    PORTS                    NAMES
1d17f542be53        rocker/rstudio      "/init"                  18 hours ago        Up 18 hours               0.0.0.0:8787->8787/tcp   elegant_banach
```

9. Stop a container:

```bash
docker stop 1d17f
```

10. Remove a container image:

```bash
docker rmi nginx
```

### Running Containers

11. **Detached and Interactive Modes** - Notice that in the earlier `nginx` example, you ran it with the `-d` flag, which means the container runs independently in detached or daemon mode. The other option is to run it in interactive mode, which is equivalent to logging into the container and working from within it.

Detached mode:

```bash
docker run -d nginx
```

```bash
docker run -it nginx /bin/bash
root@7ee278e39202:/#
```

Interactive mode requires that you specify a shell to enter, in this case the common `bash` shell. Note that the command immediately drops you into the shell session. Type `exit` to leave the container.

12. **Ports** - You may want to expose the container to a specific port locally, so that you can interact with it.
For example, if you wanted to expose nginx locally over port 80, enter this:

```bash
docker run -d -p 8080:80 nginx
```

The -p 8080:80 flag maps your local computer's port 8080 with the container's port 80. Browse to http://localhost:8080/ and see the results.

**BONUS** - Map your container to a different port and test the results. Remember that the `nginx` container will always listen for requests on port 80.

13. **Volumes** - Another useful flag for runtime is a volume mapping, so that your running container can read or write to portions of your local computer's filesystem.
So, extending the earlier command:

```bash
docker run -d -p 8080:80 -v /User/local/dir:/var/www/html nginx
```

### Creating Containers

### Conclusion
Congratulations! You have successfully done the following in Docker:

* A
* B
* C

