# PromptEngineeringInAI

This project is created to store information related to Prompt Engineering. 
We are using the Ollama - Llama3 model to run locally on a macOS laptop.

Below are the steps to inform how this model was integrated locally and utilized, saving the costs associated with using a paid version of LLM.

## Contents
1. Downloading OLLAMA file using Homebrew
2. Prepare a Git Repository and clone it locally
3. Make a folder `LLM_Integration` to keep the local model separate from other deployments/projects
4. Set up a Python environment if you plan to add more to this project
5. Download Docker and pull the Docker image for Ollama

## Steps to Set Up

### 1. Download OLLAMA using Homebrew

Refer to this site to learn how to use Homebrew for downloading Ollama: [Homebrew Formulae for Ollama](https://formulae.brew.sh/formula/ollama)

Use the VS Code terminal to start downloading the Ollama model:

```
brew install ollama
```

Next check the version of installation: 
```
ollama -v
```

And for me the output was: ollama version is 0.1.44

### 2. Prepare a Git Repository

Initialize a Git repository or clone an existing one.
Create a folder named LLM_Integration to keep the local model separate from other deployments/projects.

### 3. Set Up a Python Environment
If you plan to add more to this project, set up a Python environment:

```
python3 -m venv venv_llm
```

```
source venv_llm/bin/activate
```

### 4. Download Docker and Pull the Docker Image for Ollama
Install Docker if you haven't already.

### 5: Pull the Ollama Docker image:

```
docker pull ollama/ollama
```

Run the Docker container:

```
docker run -d -v ~/.ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

P.S. You can also run the image from Docker software.

### 5. Generate SSH Key

To resolve potential SSH key issues, follow these steps:
Generate a new SSH key without a passphrase:

P.S. Press enter so you don't need to use a passkey, directly the model will be accessible which otherwise won't be if you give a passkey.

```
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -C "hindupur.v@northeastern.edu"
```

When prompted, leave the passphrase fields empty to remove the passphrase.

Copy the SSH key to the .ollama directory:


```
mkdir -p ~/.ollama
```

```
cp ~/.ssh/id_ed25519 ~/.ollama/
```

Set the OLLAMA_HOME environment variable:

```
export OLLAMA_HOME=~/.ollama
```

```
echo 'export OLLAMA_HOME=~/.ollama' >> ~/.zshrc
```

```
source ~/.zshrc
```

Ensure correct permissions for the SSH key:

```
chmod  ~/.ollama/id_ed25519
```

### 6. Run Ollama with Llama3 Model
Run the following command to start the Llama3 model:

```
ollama run llama3
```

If you encounter an error related to the SSH key, such as input/output error, ensure that the SSH key is properly set up and the permissions are correct. If the issue persists, you may need to delete the existing container and recreate it using the Docker commands provided.

#### Troubleshooting:

If you face any issues, try the following steps:

Check Environment Variable: Ensure OLLAMA_HOME is set correctly:

```
echo $OLLAMA_HOME
```

Verify SSH Key: Ensure the SSH key exists and has the correct permissions:

```
ls -l ~/.ollama/id_ed25519
```
```
chmod 600 ~/.ollama/id_ed25519
```

Recreate Docker Container: If necessary, delete and recreate the Docker container:

```
docker rm -f ollama
```

```
docker run -d -v ~/.ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Check Docker Logs: View the logs of the Docker container for any errors:

```
docker logs ollama
```

By following these steps, you should be able to set up and run the Llama3 model locally on your macOS laptop. If you encounter any issues, please refer to the troubleshooting section or seek help from the Ollama community.

This `README.md` provides clear instructions on setting up the project, generating SSH keys, configuring Docker, and troubleshooting common issues.