# Use Pycharm with a Run:AI Job

Once you launch a workload using Run:AI, you will want to connect to it. You can do so via command-line or via other tools such as a [Jupyter Notebook](../Walkthroughs/walkthrough-build-ports.md)

This document is about accessing the remote container created by Run:AI, from JetBrain's [PyCharm](https://www.jetbrains.com/pycharm/).


## Submit a Workload

You will need your image to run an SSH server  (e.g [OpenSSH](https://www.ssh.com/ssh/sshd/)). For the purposes of this document, we have created an image named `gcr.io/run-ai-demo/pycharm-demo`. The image runs both python and ssh. Details on how to create the image are [here](https://github.com/run-ai/docs/tree/master/quickstart/python%2Bssh). The image is configured to use the ``root`` user and password for SSH.

Run the following command to connect to the container as if it were running locally:

```
runai submit build-remote -i gcr.io/run-ai-demo/pycharm-demo --interactive  \
        --service-type=portforward --port 2222:22
```

The terminal will show the connection:

``` shell
The job 'build-remote' has been submitted successfully
You can run `runai get build-remote -p team-a` to check the job status
INFO[0007] Waiting for job to start
Waiting for job to start
Waiting for job to start
Waiting for job to start
INFO[0045] Job started
Open access point(s) to service from localhost:2222
Forwarding from [::1]:2222 -> 22
```

* The Job starts an sshd server on port 22.
* The connection is redirected to the local machine (127.0.0.1) on port 2222

!!! Note

        It is possible to connect to the container using a remote IP address. However, this would be less convinient as you will need to maintain port numbers manually and change them when remote accessing using the development tool. As an example, run:

        ```
        runai submit build-remote -i gcr.io/run-ai-demo/pycharm-demo -g 1 --interactive --service-type=nodeport --port 30022:22
        ```

        * The job starts an sshd server on port 22.
        * The job redirects the external port 30022 to port 22 and uses a [Node Port](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) service type.
        * Run: `runai list`

        * Next to the job, under the "Service URL" column you will find the IP address and port. The port is 30222


## PyCharm

* Under PyCharm | Preferences go to: Project | Python Interpreter
* Add a new SSH Interpreter.
* As Host, use the IP address above. Change the port to the above and use the Username `root`
* You will be prompted for a password. Enter `root`
* Apply settings and run the code via this interpreter. You will see your project uploaded to the container and running remotely.

## X11 Forwarding with PyCharm

X11 forwarding is possible with PyCharm remote interperter.
One can run show images and plot graphs right from the container running in the kubernetes cluster, having the graphics printed on his or her local machines.

#### Container

First, there are requirements to the container itself.
[Here's](../../../quickstart/x-forwarding/docker/Dockerfile) an example of a docker file with everything you need.

1. An SSH daemon needs to be properly set up in the container ([here's](https://docs.docker.com/engine/examples/running_ssh_service/) an official Docker tutorial)
2. X11 forwarding should be enabled in the container enabled. This could be done by adding the following commands to the docker file:

        RUN sed -i "s/^.*X11Forwarding.*$/X11Forwarding yes/" /etc/ssh/sshd_config
        RUN sed -i "s/^.*X11UseLocalhost.*$/X11UseLocalhost no/" /etc/ssh/sshd_config
        RUN sed -i "s/^.*X11DisplayOffset.*$/X11DisplayOffset 10/" /etc/ssh/sshd_config

#### Host

3. Submit the workload with port forwarding. In our example, we map the local port 2222 (NOTE: the job should be interactive for this to work)

        runai submit -i gcr.io/run-ai-demo/quickstart-x-forwarding \
                --interactive --service-type=portforward --port 2222:22 xforward

4. Now we need to set an X11 forwarding tunnel all the way to the container running in the cluster.
Open a terminal and connect to the local port with the following command:

        ssh -X root@127.0.0.1 -p 2222

    **NOTE:** This `ssh -X` session should always be active as it is responsible for the X11 remote tunnel

5. Print the `$DISPLAY` environment variable from the terminal and copy it:

        echo $DISPLAY

#### PyCharm

6. Open PyCharm and set up remote Python interperter.
    1. Go to Preferences->Project: <Project Name>->Python Interperter
    2. Click on the settings button to the right and select "Add..."
    3. Choose "SSH Interperter" in the sidebar on the left
    4. Set the server configuration to be:
        * Host: `localhost`
        * Port: The port you specified in the `runai submit` command. In our example it's 2222.
        * Username: The username within the container. In our case it's `root`.
    5. Enter the password in the next screen. In our case it's `root` as well.
    6. Make sure to set the correct path of the Python binary. In our case it's `/usr/local/bin/python`

7. Set the correct environment variables in the PyCharm configuration
    1. Press "Edit Configurations..."
    2. Add the `DISPLAY` environment variable you copied before
    3. Add the `HOME` environment variable. In our case it's `/root`. This is for the X11 authentication to work.

> Note: This was done with PyCharm Professional 2020.2 and might not be available for PyCharm community edition
