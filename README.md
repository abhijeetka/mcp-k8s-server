# MCP Kubernetes Client

This is an MCP (Model Context Protocol) server for Kubernetes that provides programmatic control over Kubernetes clusters through simple API calls.

## Overview

This client allows you to perform common Kubernetes operations through MCP tools. It wraps `kubectl` commands to provide a simple interface for managing Kubernetes resources. The Model Context Protocol (MCP) enables seamless interaction between language models and Kubernetes operations.

## What is MCP?

Model Context Protocol (MCP) is a framework that enables Language Models to interact with external tools and services in a structured way. It provides:
- A standardized way to expose functionality to language models
- Context management for operations
- Tool discovery and documentation
- Type-safe interactions between models and tools

## Available Functions

### Deployment Management

#### `create_deployment(name: str, image: str, namespace: str = "default", replicas: int = 1)`
Creates a new Kubernetes deployment.
- **Parameters:**
  - `name`: Name of the deployment
  - `image`: Container image to deploy
  - `namespace`: Kubernetes namespace (defaults to "default")
  - `replicas`: Number of pod replicas (defaults to 1)

#### `update_deployment(name: str, namespace: str = "default", replicas: int = None, image: str = None)`
Updates an existing Kubernetes deployment.
- **Parameters:**
  - `name`: Name of the deployment to update
  - `namespace`: Kubernetes namespace (defaults to "default")
  - `replicas`: New number of replicas (optional)
  - `image`: New container image (optional)

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
