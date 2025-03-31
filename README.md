# MCP Kubernetes Server

![](https://badge.mcpx.dev?type=server 'MCP Server')
[![smithery badge](https://smithery.ai/badge/@abhijeetka/mcp-k8s-server)](https://smithery.ai/server/@abhijeetka/mcp-k8s-server)

This is an MCP (Model Context Protocol) server for Kubernetes that provides control over Kubernetes clusters through interactions with LLMs.

## Overview

This client allows you to perform common Kubernetes operations through MCP tools. It wraps `kubectl` commands to provide a simple interface for managing Kubernetes resources. The Model Context Protocol (MCP) enables seamless interaction between language models and Kubernetes operations.

## What is MCP?

Model Context Protocol (MCP) is a framework that enables Language Models to interact with external tools and services in a structured way. It provides:
- A standardized way to expose functionality to language models
- Context management for operations
- Tool discovery and documentation
- Type-safe interactions between models and tools

## Usage Examples

- Create a new deployment for me with name nginx-app and image nginx:latest in the production namespace with 3 replicas.
- Update the deployment nginx-app to version 1.19 in the production namespace.
- Scale the deployment nginx-app to 5 replicas in the production namespace.
- Get me the pods in the production namespace.
- Get me all namespaces in the cluster.
- Get me all nodes in the cluster.
- Get me all services in the cluster.
- Get me all deployments in the cluster.
- Get me all jobs in the cluster.
- Get me all cronjobs in the cluster.
- Get me all statefulsets in the cluster.
- Get me all daemonsets in the cluster.
- What is the current context.
- list all contexts.
- switch to context <context-name>.
- Get me the logs of pod <pod-name> in the production namespace.
- Get me the events in the production namespace.
- annotate pod <pod-name> with key1=value1 in the production namespace.
- remove annotation key1 from pod <pod-name> in the production namespace.
- add label key1=value1 to pod <pod-name> in the production namespace.
- remove label key1 from pod <pod-name> in the production namespace.
- expose deployment nginx-app in the production namespace on port 80.
- port-forward pod,deployment,service with name <resource-name> in the production namespace to local port 8080.
- delete pod, deployment, service, job, cronjob, statefulset, daemonset with name <resource-name> in the production namespace.

## Upcoming Features
- Create cluster role.
- delete cluster role.
- create cluster role binding.
- delete cluster role binding.
- create namespace.
- delete namespace.
- create service account.
- delete service account.
- create role.
- delete role.
- create role binding.a
- delete role binding.

## LLM Integration

This MCP client is designed to work seamlessly with Large Language Models (LLMs). The functions are decorated with `@mcp.tool()`, making them accessible to LLMs through the Model Context Protocol framework.

### Example LLM Prompts

LLMs can interact with your Kubernetes cluster using natural language. Here are some example prompts:

- "Create a new nginx deployment with 3 replicas in the production namespace"
- "Scale the nginx-app deployment to 5 replicas"
- "Update the image of nginx-app to version 1.19"

The LLM will interpret these natural language requests and call the appropriate MCP functions with the correct parameters.

### Benefits of LLM Integration

1. **Natural Language Interface**: Manage Kubernetes resources using conversational language
2. **Reduced Command Complexity**: No need to remember exact kubectl syntax
3. **Error Prevention**: LLMs can validate inputs and provide helpful error messages
4. **Context Awareness**: LLMs can maintain context across multiple operations
5. **Structured Interactions**: MCP ensures type-safe and documented interactions between LLMs and tools

## Requirements

- Kubernetes cluster access configured via `kubectl`
- Python 3.x
- MCP framework installed and configured

## Security Note

When using this client with LLMs, ensure that:
- Proper access controls are in place for your Kubernetes cluster
- The MCP server is running in a secure environment
- API access is properly authenticated and authorized

## Usage with Claude Desktop

```
{
    "mcpServers": {
        "Kubernetes": {
            "command": "uv",
            "args": [
                "--directory",
                "~/mcp/mcp-k8s-server",
                "run",
                "kubernetes.py"
            ]
        }
    }
}
```

## Contributing

We welcome contributions to the MCP Kubernetes Server! If you'd like to contribute:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write or update tests as needed
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request


For major changes, please open an issue first to discuss what you would like to change.
### Installing via Smithery

To install Kubernetes Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@abhijeetka/mcp-k8s-server):

```bash
npx -y @smithery/cli install @abhijeetka/mcp-k8s-server --client claude
```
