FROM python:3

# User creation code from https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user
ARG USERNAME=transparen-c
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

WORKDIR /transparen-c

COPY requirements.txt requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

USER $USERNAME

CMD ["sleep","3600"]
